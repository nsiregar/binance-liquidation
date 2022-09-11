import requests
from config import config


class TelegramHandler:
    def __init__(self):
        self.chat_id = config.TELEGRAM_CHANNEL_ID
        self.token = config.TELEGRAM_BOT_TOKEN

    def send_msg(self, msg):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        json_data = {
            "chat_id": self.chat_id,
            "text": msg,
        }
        headers = {
            "Content-Type": "application/json"
        }
        resp = requests.post(url, json=json_data, headers=headers)
        resp.raise_for_status()
