import logging
import os

from dialogflow_API import detect_intent_texts

from dotenv import load_dotenv
from telegram import ForceReply
from telegram import Update
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Updater


logger = logging.getLogger('Logger')


def start(
        update: Update,
        context=CallbackContext):
    user = update.effective_user
    logger.info(
        "User %s started the conversation.",
        user.mention_markdown_v2()
        )
    update.message.reply_markdown_v2(
        fr'Бот запущен\!',
        reply_markup=ForceReply(selective=True)
    )


def reply(
        update: Update,
        context=CallbackContext):
    project_id = os.environ['PROJECT_ID']
    chat_id = update.effective_chat.id
    text = update.message.text
    intent = detect_intent_texts(
        project_id=project_id,
        session_id=chat_id,
        text=text,
        language_code='ru'
    )
    context.bot.send_message(
        chat_id=chat_id,
        text=intent.query_result.fulfillment_text
    )


def main():
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
    updater = Updater(
        token=bot_token,
        use_context=True
        )
    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        CommandHandler(
            'start',
            start
            )
        )
    echo_handler = MessageHandler(
        Filters.text & (~Filters.command),
        reply
        )
    dispatcher.add_handler(
        echo_handler
        )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
