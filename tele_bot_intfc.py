import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import os
from dotenv import load_dotenv
from utils import filter_data
from datetime import datetime, timedelta
import pprint
load_dotenv()

from leetcode_scraper import LeetcodeScraper

START_PAGE, END_PAGE = range(2)

# Initialize the scraper
scraper = LeetcodeScraper()

# Dictionary to store the last scrape time for each user
last_scrape_time = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "Welcome to the LeetCode Scraper Bot!\n"
        "You can use the following commands:\n"
        "/scrape - Scrape rankings from a range of pages.\n"
    )
    await update.message.reply_text(message)

async def scrape(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    current_time = datetime.now()

    # Check if the user has scraped in the last 5 minutes
    if user_id in last_scrape_time:
        time_diff = current_time - last_scrape_time[user_id]
        if time_diff < timedelta(minutes=5):
            wait_time = timedelta(minutes=5) - time_diff
            await update.message.reply_text(f"Please wait {wait_time.seconds // 60} minutes and {wait_time.seconds % 60} seconds before scraping again.")
            return ConversationHandler.END

    await update.message.reply_text("Please enter the first page in the range to scrape:")
    return START_PAGE

async def start_page(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    start_page = int(update.message.text)
    if start_page < 1 :
        await update.message.reply_text("Start page must be between 1 and 100. Please enter a valid start page:")
        return START_PAGE
    context.user_data['start_page'] = start_page
    await update.message.reply_text("Please enter the end page in the range to scrape:")
    return END_PAGE

async def end_page(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    end_page = int(update.message.text)
    start_page = context.user_data['start_page']
    if end_page < start_page or end_page - start_page > 100:
        await update.message.reply_text("End page must be greater than or equal to start page and less than or equal to 100. Please enter a valid end page:")
        return END_PAGE
    context.user_data['end_page'] = end_page
    
    await update.message.reply_text(f"Scraping rankings from page {start_page} to {end_page}...")

    # Scrape the data
    rankings = scraper.scrape_all_global_ranking_users_selection(start_page, end_page)

    # Filter the data
    df_filtered = filter_data(rankings)

    # create a filename with the date and time with the word 'rankings' in it
    filename = f'rankings_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
    
    # Save DataFrame to CSV file
    df_filtered.to_csv(filename, index=False)
    
    # Send CSV file to the user
    with open(filename, 'rb') as file:
        await update.message.reply_document(document=file, filename=filename)

    # Update the last scrape time for the user
    user_id = update.message.from_user.id
    last_scrape_time[user_id] = datetime.now()

    return ConversationHandler.END

def main() -> None:
    application = ApplicationBuilder().token(f'{os.getenv("TELEGRAM_BOT_TOKEN")}').build()

    start_handler = CommandHandler('start', start)
    
    scrape_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('scrape', scrape)],
        states={
            START_PAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, start_page)],
            END_PAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, end_page)],
        },
        fallbacks=[]
    )

    application.add_handler(start_handler)
    application.add_handler(scrape_conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
