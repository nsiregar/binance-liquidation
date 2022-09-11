import logging

from client.binance import BinanceWSClient

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level='INFO',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger()


symbols = [
    {"pair": "BTCDOMUSDT", "usd_limit": 50},
    {"pair": "BTCUSDT", "usd_limit": 50},
    {"pair": "DEFIUSDT", "usd_limit": 50},
    {"pair": "ETHUSDT", "usd_limit": 50},
    {"pair": "FOOTBALLUSDT", "usd_limit": 50},
    {"pair": "WAVESUSDT", "usd_limit": 10},
    {"pair": "ETCUSDT", "usd_limit": 10},
    {"pair": "MATICUSDT", "usd_limit": 10},
]


if __name__ == "__main__":
    client = BinanceWSClient(symbols)
    client.connect()
