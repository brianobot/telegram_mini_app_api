import os
import json # noqa
import django
import requests
import logging


logging.basicConfig(
    filename='broadcast.log',  # Log file name
    filemode='a',              # Append to the file (use 'w' to overwrite on each run)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO         # Log level (INFO, DEBUG, ERROR, etc.)
)


BOT_TOKEN = ""
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()


# use this for testing the message in isolation of real users
user_ids = [
    "7315758175",
    "7315758175",
    "7315758175",
    "7315758175",
] 


def send_push_notification(message: str, user_ids: list = user_ids):
    for index, user_id in enumerate(user_ids, start=1):
        url = f"{BASE_URL}/sendMessage"
        
        # reply_markup = {
        #     "inline_keyboard": [
        #         [
        #             {
        #                 "text": "Follow Channel!",
        #                 "url": "https://t.me/buzmode",
        #             }
        #         ]
        #     ]
        # }

        payload = {
            "chat_id": user_id,
            "text": message,
            # "reply_markup": json.dumps(reply_markup)
        }

            
        response = requests.post(url, data=payload)
            
        if response.status_code != 200:
            logging.error(f"❌ Failed to send message to %s: %s", user_id, getattr(response, "text", None))
        else:
            logging.info(f"✅ Message Sent to {user_id}")
                


def get_user_ids():
    from users.models import User

    return list(User.objects.all().values_list("id", flat=True))


def sent_to_user():
    """
    this checks the users that have already received a message for the current active message session
    """
    import re

    pattern = r"Sent to (\d+)$"

    with open("broadcast.log") as file:
        log_data = file.read()

        # Extract all matching IDs
        ids = re.findall(pattern, log_data, re.MULTILINE)
    
    return ids


def main():
    user_ids = get_user_ids()
    # message = "🐝 Have you followed our Telegram Channel?"

    message = "🚀 BUZ up your Monday! 🎉 Join our Telegram for a shot at winning $420 USDT 💸 Winner revealed this Monday—don’t miss out! 🕶️🔥 [https://t.me/buzmode]"

    user_ids_recvd = sent_to_user()
    print(f"✅ {user_ids_recvd = }")

    fresh_user_ids = list(set(user_ids) - set(user_ids_recvd))
    print(f"{len(fresh_user_ids) = }")
    print(f"{len(user_ids_recvd) = }")
    print(f"{len(user_ids) = }")

    # Send a notification to all users
    send_push_notification(message, user_ids)


if __name__ == "__main__":
    main()