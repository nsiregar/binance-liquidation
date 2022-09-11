import logging
import threading

from client.binance import BinanceWSClient
from binance_symbols import SYMBOLS
from utils.chunk import make_chunks

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level="INFO",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger()

CHUNKSIZE = 10

if __name__ == "__main__":
    for symbols in make_chunks(SYMBOLS, chunk_size=CHUNKSIZE):
        client = BinanceWSClient(symbols)
        threading.Thread(target=client.connect).start()
