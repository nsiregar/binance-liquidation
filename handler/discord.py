from discord_webhook import DiscordWebhook

from config import config


class DiscordHandler:
    def __init__(self):
        self.webhook = DiscordWebhook(url=config.DISCORD_WEBHOOK)

    def send_msg(self, msg):
        self.webhook.set_content(msg)
        self.webhook.execute()
