import uuid


def generateData(text):
    data = {
        "event_name": "message",
        "payload": {
            "content": {
                "text": text,
                "type": "text",
            },
            "meta":
                {
                    "chat_id": "*",
                    "timestamp": "*",
                    "bot_id": "*",
                    "chat_id": "*",
                    "client_token": str(uuid.uuid1()),
                }
        },
        "token": "*",
        "auth": {
            "user_id": "*",
            "auth_token": "*",
            "device_id": "*",
        }
    }
    return data
