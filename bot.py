import logging
import os

from dotenv import load_dotenv
from telegram import ForceReply
from telegram import Update
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Updater


logger = logging.getLogger('Logger')


def start(update: Update, context=CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True)
    )
    

def echo(update: Update, context=CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )


def main():
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    chat_id = os.environ['CHAT_ID']
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    updater = Updater(
        token=bot_token,
        use_context=True
        )
    dispatcher = updater.dispatcher
    start_handler = CommandHandler(
        'start',
        start
        )
    echo_handler = MessageHandler(
        Filters.text & (~Filters.command),
        echo
    )
    dispatcher.add_handler(
        start_handler
        )
    dispatcher.add_handler(
        echo_handler
    )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()