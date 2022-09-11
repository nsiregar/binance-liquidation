from telegram import Bot

from config import config


class TelegramHandler:
    def __init__(self):
        self.bot = Bot(token=config.TELEGRAM_BOT_TOKEN)

    def send_msg(self, msg):
        self.bot.sendMessage(
            config.TELEGRAM_CHANNEL_ID,
            msg,
            parse_mode="MARKDOWN",
        )
