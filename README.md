### README for LeetCode Scraper Bot

This README provides a comprehensive guide on how to download, install, and utilize the LeetCode Scraper Bot. The bot scrapes LeetCode rankings from a specified range of pages and sends the data as a CSV file to the user through Telegram. 

#### Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Code Overview](#code-overview)
4. [Functionality and Flow](#functionality-and-flow)
5. [Usage](#usage)

---

### Installation

#### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- Telegram account
- A Telegram Bot token

#### Steps

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment and activate it**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    - Create a `.env` file in the root directory of your project.
    - Add your Telegram Bot token to the `.env` file:
    ```
    TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
    ```

---

### Configuration

1. **Configure your Telegram Bot**
    - Go to [BotFather](https://t.me/botfather) on Telegram.
    - Create a new bot and get the token.
    - Add the token to your `.env` file as mentioned above.

---

### Code Overview

The project consists of the following main files:

1. **main.py** - The main entry point for the bot.
2. **leetcode_scraper.py** - Contains the `LeetcodeScraper` class which handles the scraping logic.
3. **tele_bot_intfc.py** - Manages the Telegram bot interface and handles commands and messages.
4. **utils.py** - Contains utility functions used across the project.

#### leetcode_scraper.py

This file defines the `LeetcodeScraper` class, which is responsible for scraping the LeetCode website.

#### tele_bot_intfc.py

This file manages the interaction with the Telegram bot, including command handlers and message responses.

#### utils.py

This file contains utility functions for data processing and filtering.

---

### Functionality and Flow

1. **Start Command**
    - When a user sends the `/start` command, the bot welcomes the user and provides information on available commands.

2. **Scrape Command**
    - When a user sends the `/scrape` command, the bot initiates a conversation asking for the start page.
    - The bot checks the time of the last scrape to ensure a 5-minute interval between scrapes.
    - The bot then asks for the end page and validates the input.
    - Upon receiving valid inputs, the bot scrapes the specified range of pages, filters the data, and sends the data back to the user as a CSV file.

#### Detailed Code Flow

- **`start` Function**: Sends a welcome message with command instructions.
- **`scrape` Function**: Initiates the scraping process by asking the user for the start page and checks the last scrape time.
- **`start_page` Function**: Validates and stores the start page provided by the user.
- **`end_page` Function**: Validates and stores the end page, performs scraping, filters the data, and sends the result as a CSV file to the user.

---

### Usage

1. **Start the Bot**
    - Run the main script:
    ```bash
    python main.py
    ```

2. **Interact with the Bot**
    - Open Telegram and search for your bot.
    - Start a conversation with the `/start` command.
    - Use the `/scrape` command to scrape LeetCode rankings by providing the start and end pages.

#### Example Interaction

1. **User**: `/start`
    - **Bot**: "Welcome to the LeetCode Scraper Bot! You can use the following commands: /scrape - Scrape rankings from a range of pages."

2. **User**: `/scrape`
    - **Bot**: "Please enter the first page in the range to scrape:"

3. **User**: `1`
    - **Bot**: "Please enter the end page in the range to scrape:"

4. **User**: `10`
    - **Bot**: "Scraping rankings from page 1 to 10..."
    - **Bot**: Sends the CSV file with the scraped data.

---

Feel free to modify the code as per your requirements. For any issues or contributions, please refer to the repository on GitHub.

---

### Additional Files

Ensure that the following files are present in your project directory:

- **leetcode_scraper.py**
- **tele_bot_intfc.py**
- **utils.py**
- **requirements.txt**
- **.env**

For detailed explanations and code snippets, please refer to the corresponding files.