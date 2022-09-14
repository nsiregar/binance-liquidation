import emoji

from handler.discord import DiscordHandler
from handler.telegram import TelegramHandler
from utils.humanize import humanize_number
from rq import Queue, Retry
from redis import Redis


class Message:
    def __init__(self, start_emoji: str, pair: str, direction: str, usd: float, price: float, funding_rate: float):
        self.start_emoji = start_emoji
        self.pair = pair
        self.direction = direction
        self.usd = usd
        self.price = price
        self.funding_rate = funding_rate

    def send_to_telegram(self) -> None:
        handler = TelegramHandler()
        handler.send_msg(self.telegram_msg)

    def send_to_discord(self) -> None:
        handler = DiscordHandler()
        handler.send_msg(self.discord_msg)

    @property
    def formatted_usd(self) -> str:
        return humanize_number(self.usd, strip_trailing_zeros=False)

    @property
    def telegram_msg(self) -> str:
        messages = [
            f"{self.start_emoji} **Liq. {self.direction}**",
            f"#{self.pair}",
            f"${self.formatted_usd} at ${self.price:.2f}",
            f"Funding Rate: {self.funding_rate:.3f}%",
        ]
        log_msg = " | ".join(messages)
        return emoji.emojize(log_msg)

    @property
    def discord_msg(self) -> str:
        messages = [
            f"{self.start_emoji} **Liq. {self.direction}**",
            self.pair,
            f"${self.formatted_usd} at ${self.price:.2f}",
            f"Funding Rate: {self.funding_rate:.3f}%",
        ]
        log_msg = " | ".join(messages)
        return emoji.emojize(log_msg)


class MessageDispatcher:
    def __init__(self):
        self.queue = Queue(connection=Redis())

    def send_msg(self, message: Message) -> None:
        retry = Retry(max=3, interval=[10, 30, 60])
        self.queue.enqueue_many(
            [
                Queue.prepare_data(
                    message.send_to_discord,
                    retry=retry,
                ),
                Queue.prepare_data(
                    message.send_to_telegram,
                    retry=retry,
                ),
            ],
        )
