import json, pprint, os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def structure_narrative_list():
    with open("narratives.json", "r") as narratives:
        narratives = narratives.read()
        narratives_input_json = json.loads(narratives)


    days = ["day1", "day2", "day3"]
    times=["8:00 AM", "8:45 AM", "9:30 AM", "10:15 AM", "11:00 AM", "11:45 AM", "12:30 PM", "1:15 PM", "2:00 PM", "2:45 PM", "3:30 PM", "4:15 PM", "5:00 PM", "5:45 PM"]
    narrative_list = []

    for day in days:
        for time in times:
            if time in narratives_input_json[day]:
                narrative_list.append(narratives_input_json[day][time])

    with open("Narratives_List.json", "w") as output_file:
        narrative_list_json = json.dump(narrative_list, output_file, indent=4 )
        print("Saved Narratives as a list")


def get_narrative_list():
    with open("Narratives_List.json", "r") as nl_file:
        narrative_list = nl_file.read()
        narrative_list_json = json.loads(narrative_list)
    return narrative_list_json

async def send_to_telegram(message, chat_id="-1002163164940"):
    bot = Bot(token=TOKEN)
    text = f"📙 *Affirmative Thought Narrative*\n"
    message_lines = [
        text,
        f"**`{message}`**\n",
    ]
    message = '\n'.join(message_lines)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode="MarkdownV2")

if __name__ == "__main__":
    # pprint.pprint(get_narrative_list())
    pass