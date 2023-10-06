from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    input_text = dialogflow.TextInput(
        text=text,
        language_code=language_code
    )
    input_query = dialogflow.QueryInput(
        text=input_text
    )
    intent = session_client.detect_intent(
        request={
            "session": session,
            "query_input": input_query
        }
    )
    return intent

