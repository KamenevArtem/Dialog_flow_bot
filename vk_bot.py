import os
import random

import vk_api as vk

from dialogflow_API import detect_intent_texts
from dotenv import load_dotenv
from google.cloud import dialogflow_v2beta1 as dialogflow
from vk_api.longpoll import VkLongPoll, VkEventType


def echo(event, vk_api, project_id):
    intent = detect_intent_texts(
        project_id=project_id,
        session_id=event.user_id,
        text=event.text,
        language_code='ru'
    )
    if not intent.query_result.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=intent.query_result.fulfillment_text,
            random_id=random.randint(1,1000)
        )


def main():
    load_dotenv()
    project_id = os.environ['PROJECT_ID']
    vk_api_key = os.environ['VK_API_KEY']
    vk_session = vk.VkApi(token=vk_api_key)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api, project_id)


if __name__ == "__main__":
    main()
