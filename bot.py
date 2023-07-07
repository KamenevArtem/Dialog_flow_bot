import os

import telegram

from dotenv import load_dotenv


def main():
    load_dotenv()
    bot_token = os.environ('BOT_TOKEN')
    bot = telegram.Bot(token=bot_token)


if __name__ == '__main__':
    main()