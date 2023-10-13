# Dialog_flow_bot

Реализовано два бота для телеграмма и Вконтакте, способных в автоматическом режиме отвечать на ряд заданных администратором вопросов. Администратор имеет возможность добавлять и удалять перечень обрабатываемых ботом фраз. Механизм определения вопроса и выдачи ответа реализон на базе Dialog Flow API

## Как установить

Python3 версии 3.11 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Подготовка к запуску

Необходим: 
 1. создать проект [Dilalog Flow](https://cloud.google.com/dialogflow/es/docs/quick/setup) следуя инструкции;
 2. создать [агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent);
 3. [включить API](https://cloud.google.com/dialogflow/es/docs/quick/setup#api) в Google-аккаунте;
 4. скачать репозиторий проекта, затем создать файл `.env` в корневой папке проекта. В данный файл необходимо внести переменные окружения:

* `PROJECT_ID` - ID проекта в Google-аккаунте. Можно найти в настройках Dialog Flow агента в графе "Google Project";
* `TG_BOT_TOKEN` - токен бота. Он может быть получен сразу после создания бота. [Инструкция по созданию бота](https://habr.com/ru/articles/262247/);
* `VK_API_KEY` - токен группы Вконтакте;
* `GOOGLE_APPLICATION_CREDENTIALS` - путь к файлу key.json с GOOGLE_APPLICATION_CREDENTIALS>.


## Запуск 

Для запуска телеграм бота используйте следующую команду:
```
python telegram_bot.py
```

![alt text](https://dvmn.org/filer/canonical/1569214094/323/)

Для запуска вконтакте бота используйте следующую команду:
```
python vk_bot.py 
```

![alt text](https://dvmn.org/filer/canonical/1569214089/322/)

### Расширения перечня ответов пользователям

Для запуска выполните команду:
```
python create_intents.py
```
Пример json файла:

```
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },  ...
```
