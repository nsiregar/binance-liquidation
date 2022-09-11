import emoji

from handler.discord import DiscordHandler
from handler.telegram import TelegramHandler
from utils.humanize import humanize_number


class MessageDispatcher:
    def __init__(self):
        self.discord_handler = DiscordHandler()
        self.telegram_handler = TelegramHandler()

    def send_msg(self, msg_data):
        self.discord_handler.send_msg(str(DiscordMessage(**msg_data)))
        self.telegram_handler.send_msg(str(TelegramMessage(**msg_data)))


class Message:
    def __init__(self, start_emoji, pair, direction, usd, price, funding_rate):
        self.start_emoji = start_emoji
        self.pair = pair
        self.direction = direction
        self.usd = usd
        self.price = price
        self.funding_rate = funding_rate


class TelegramMessage(Message):
    def __str__(self):
        formatted_usd = humanize_number(self.usd)
        log_msg = f"{self.start_emoji} **Liq. {self.direction}** | #{self.pair} | ${formatted_usd} at ${self.price:.2f} | Funding Rate: {self.funding_rate:.3f}%"
        return emoji.emojize(log_msg)


class DiscordMessage(Message):
    def __str__(self):
        formatted_usd = humanize_number(self.usd)
        log_msg = f"{self.start_emoji} **Liq. {self.direction}** | {self.pair} | ${formatted_usd} at ${self.price:.2f} | Funding Rate: {self.funding_rate:.3f}%"
        return emoji.emojize(log_msg)
