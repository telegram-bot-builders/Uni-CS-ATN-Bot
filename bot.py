import time
from utils import get_narrative_list, send_to_telegram
import asyncio

async def main():
    narratives = get_narrative_list()
    for i, narrative in enumerate(narratives):
        await send_to_telegram(narrative)
        print(f"Message {i + 1} sent...")
        time.sleep(2700)

if __name__ == "__main__":
    asyncio.run(main())