import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
