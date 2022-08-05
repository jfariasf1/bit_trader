import logging
from http_api import BybitHTTP
from websockets_api import BybitWebsocket
from BybitTA import BybitTA
from config import api
import connections
import pybit

if __name__ == '__main__':
    symbols = "BTCUSDT"
    history_size = 20
    rsi_length = 14
    interval = 1 # 1 minute

    # Data refresh interval. Enum : 1 3 5 15 30 60 120 240 360 720 "D" "M" "W"
    logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s %(message)s")

    # Get historic using HTTP API
    candle_data = BybitHTTP(api.HTTP_PERPETUALS, symbols, interval=interval, limit=history_size).load_data()

    # Do first RSI TA
    BybitTA(candle_data, rsi_length)

    # Connect with websockets API and keep doing TA in real time
    BybitWebsocket(api.WS_PERPETUALS, candle_data, symbols, interval, rsi_length)


