from mastodon import Mastodon

from config import config

mastodon_app = Mastodon(
    client_id=config.MASTODON_CLIENT_ID,
    client_secret=config.MASTODON_CLIENT_SECRET,
    access_token=config.MASTODON_ACCESS_TOKEN,
    api_base_url=config.MASTODON_INSTANCE_URL,
)


class MastodonHandler:
    def send_msg(self, msg):
        mastodon_app.status_post(msg)
