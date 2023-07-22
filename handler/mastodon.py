from mastodon import Mastodon

from config import config


class MastodonHandler:
    def __init__(self) -> None:
        self.app = Mastodon(
            access_token=config.MASTODON_ACCESS_TOKEN,
            api_base_url=config.MASTODON_INSTANCE_URL,
        )

    def send_msg(self, msg):
        self.app.status_post(msg)
