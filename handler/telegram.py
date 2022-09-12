from telegram import Bot
from config import config

telegram_bot = Bot(config.TELEGRAM_BOT_TOKEN)


class TelegramHandler:
    def __init__(self):
        self.chat_id = config.TELEGRAM_CHANNEL_ID

    def send_msg(self, msg):
        telegram_bot.send_message(
            self.chat_id,
            msg,
            parse_mode="MARKDOWN",
        )
