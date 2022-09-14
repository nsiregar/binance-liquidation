import json
import threading
import datetime

import websocket
import logging

from handler.dispatcher import MessageDispatcher, Message

logger = logging.getLogger()


class BinanceWSClient:
    def __init__(self, symbols):
        self.symbols = {}

        for symbol in symbols:
            pair = symbol["pair"]
            usd_limit = symbol["usd_limit"]
            self.symbols[pair] = PairData(
                pair=pair, funding_rate=0, usd_limit=usd_limit
            )

        self.socket = self.generate_socket()
        self.dispatcher = MessageDispatcher()

    def connect(self):
        ws = websocket.WebSocketApp(self.socket, on_message=self.parse_msg)
        ws.run_forever()

    def parse_msg(self, ws, msg):
        try:
            data = json.loads(msg)["data"]
            if data["e"] == "markPriceUpdate":
                threading.Thread(target=self._parse_price_update, args=[data]).start()
            elif data["e"] == "forceOrder":
                threading.Thread(target=self._parse_force_order, args=[data]).start()
            else:
                logger.error("[PARSE MSG][ERROR] Stream data not recognized")
        except Exception as exc:
            logger.error(f"[PARSE MSG][ERROR] {exc}")

    def generate_socket(self):
        base_url = "wss://fstream.binance.com/stream?streams="
        streams = (
            f"{pair.lower()}@forceOrder/{pair.lower()}@markPrice@1s"
            for pair in self.symbols.keys()
        )
        stream_string = "/".join(streams)
        return f"{base_url}{stream_string}"

    def _parse_price_update(self, data):
        current_time = datetime.datetime.now().timestamp() * 1000.0
        pair_data = self.symbols.get(data["s"], None)

        if (pair_data is None) or (current_time < pair_data.next_funding_time):
            return

        pair_data.funding_rate = float(data["r"]) * 100
        pair_data.next_funding_time = int(data["T"])
        logger.info(pair_data)

    def _parse_force_order(self, data):
        timestamp = datetime.datetime.now()
        data = data["o"]
        pair_symbol = data["s"]
        pair_data = self.symbols.get(pair_symbol, None)
        if pair_data is None:
            return

        side = data["S"]
        price = float(data["ap"])
        amount = float(data["q"])
        trade_time = datetime.datetime.fromtimestamp(int(data["T"]) / 1000.0)

        delay = timestamp - trade_time
        delay = int(1000 * delay.total_seconds())  # In milliseconds
        usd = amount * price

        direction = "LONG" if side == "SELL" else "SHORT"
        start_emoji = ":red_circle:" if direction == "LONG" else ":green_circle:"
        message = Message(
            start_emoji=start_emoji,
            pair=pair_symbol,
            direction=direction,
            usd=usd,
            price=price,
            funding_rate=pair_data.funding_rate,
        )
        logger.info(f"Delay: {delay} ms | {message.discord_msg}")

        if (usd / 1000) > pair_data.usd_limit:
            self.dispatcher.send_msg(message=message)


class PairData:
    def __init__(self, pair, usd_limit, funding_rate=0, next_funding_time=0):
        self.pair = pair
        self.usd_limit = usd_limit
        self.funding_rate = funding_rate
        self.next_funding_time = next_funding_time

    def __str__(self):
        msg = f"[{self.pair}] New Funding Rate: {self.funding_rate:.3f}%"
        return msg
