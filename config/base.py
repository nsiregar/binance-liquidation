import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
    MASTODON_INSTANCE_URL = os.getenv("MASTODON_INSTANCE_URL")
    MASTODON_CLIENT_ID = os.getenv("MASTODON_CLIENT_ID")
    MASTODON_CLIENT_SECRET = os.getenv("MASTODON_CLIENT_SECRET")
    MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
