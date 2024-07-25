from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    print(f"Chat ID: {chat_id}")
    await update.message.reply_text(f"Hello! Your chat ID is {chat_id}")

def main():
    # Create the Application and pass it your bot's token
    app = ApplicationBuilder().token(TOKEN).build()

    # Register the start command handler
    app.add_handler(CommandHandler("start", start))

    # Start the Bot
    app.run_polling()

if __name__ == '__main__':
    main()
