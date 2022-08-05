import BybitTA
from http_api import BybitHTTP
from datetime import datetime
from config import api
from pybit import usdt_perpetual
from time import sleep
from pybit import spot
from BybitTA import BybitTA
import connections


class BybitWebsocket(BybitTA):
    candle_start = 0

    # {'start': 1656557640, 'end': 1656557700, 'period': '1', 'open': 20059.5, 'close': 20061.5, 'high': 20069.5, 'low': 20059, 'volume': '1.033', 'turnover': '20730.817', 'confirm': False, 'cross_seq': 7159789733, 'timestamp': 1656557667363972}

    def print_formatted(self, message):
        print("WS",
              "close", message["close"],
              "volume", message["volume"],
              "time", datetime.fromtimestamp(message["start"]).strftime('%H:%M %p'))

    def update(self, data):
        self.print_formatted(data)
        self.updateTA({
            "start": data["start"],
            "close": data["close"],
            "high": data["high"],
            "low": data["low"],
            "volume": data["volume"]
                        })

    def handle_kline(self, message):
        # I will be called every time there is new kline data!
        data_start = message["data"][0]["start"]
        candle_close = message["data"][0]

        if self.candle_start == 0:
            self.candle_start = data_start
            self.update(candle_close)
        elif self.candle_start != data_start:
            print(message["data"])
            self.update(candle_close)
            self.candle_start = data_start

    def load_data(self):
        connections.session_auth_ws.kline_stream(self.handle_kline, self.SYMBOL, self.interval)

    def handle_position(msg):
        print(msg)


    # Press the green button in the gutter to run the script.
    def __init__(self, connection_type, candle_data, symbol, interval,rsi_length):
        self.SYMBOL = symbol
        self.rsi_length=rsi_length
        self.candle_data_json = candle_data
        self.interval = interval
        # Connect with authentication!
        connections.session_auth_ws = connections.getEndpoint(connection_type)
        self.load_data()
        while True:
            # This while loop is required for the program to run. You may execute
            # additional code for your trading logic here.
            sleep(1)
        # Now, we can subscribe to the orderbook stream and pass our arguments:
        # our function and our selected symbol.
        # To subscribe to multiple symbols, pass a list: ["BTCUSD", "ETHUSD"]
        # To subscribe to all symbols, pass "*".
        # ws_usdt.orderbook_25_stream(handle_orderbook, "BTCUSDT")

        # ws_usdt.position_stream(handle_position)

        # Similarly, if you want to listen to the WebSockets of other markets:
    #  ws_spot = spot.WebSocket(test=True)
    # handle_orderbook() will now be called for both inverse and spot data.
    # To keep the data separate, simply create another function and pass it below.

    # ws_spot.depth_v2_stream(handle_orderbook_spot, "BTCUSDT")

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
