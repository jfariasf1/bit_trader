"""
To see which endpoints are available, you can read the API docs at
https://bybit-exchange.github.io/docs/inverse/#t-introduction
Some methods will have required parameters, while others may be optional.
The arguments in pybit methods match those provided in the Bybit API
documentation.
The following functions are available:
exit()
Public Methods:
------------------------
"""

# Import pybit and define the HTTP object.
from pybit import HTTP  # supports inverse perp & futures, usdt perp, spot.
from pybit.spot import HTTP
from datetime import datetime
import connections
import numpy

#removelater
import timeit

class BybitHTTP:
# Unauthenticated
   # session_unauth = usdt_perpetual.HTTP(endpoint="https://api.bybit.com")

    # Authenticated



    def load_data(self):
        ## TODO: TIME LATER WITH NUMPY

        # npdt = numpy.datetime(datetime.utcnow())
        # dt = npdt.astype(datetime)
        #  print("date:", dt_obj)
        values = []
        for close_candle in self.session["result"]:
            values.append({
                "start": close_candle["start_at"],
                "close": close_candle["close"],
                "volume": close_candle["volume"],
                "high": close_candle["high"],
                "low": close_candle["low"]
                })
            print("close", close_candle["close"], "volume", close_candle["volume"], "time",
                  datetime.fromtimestamp(close_candle["open_time"]).strftime('%H:%M %p'))
        return values

    def __init__(self, connection_type, symbol, interval, limit):

        connections.session_auth_http = connections.getEndpoint(connection_type)
        connections.session_trading = connection_type
        server_time = int(connections.session_auth_http.server_time()["time_now"].split(".")[0]) - limit * (60*interval)

        self.session =  connections.session_auth_http.query_kline(
            symbol=symbol,
            interval=interval,
            limit=limit,
            from_time=server_time
        )
        # Let's get market information about EOSUSD. Note that "symbol" is
        # a required parameter as per the Bybit API documentation.
        #session_unauth.latest_information_for_symbol(symbol="BTCUSDT")


        # We can fetch our wallet balance using an auth'd session.
        #session_auth.get_wallet_balance(coin="BTC")


    """
    Spot & other APIs.
    from pybit import HTTP  <-- supports inverse perp & futures, usdt perp, spot.
    from pybit.spot import HTTP   <-- exclusively supports spot.
    """

    # Reassign session_auth to exclusively use spot

    """
    session_auth = spot.HTTP(
        endpoint="https://api.bybit.com",
        api_key="...",
        api_secret="..."
    )
    
    
    # Prefer spot endpoint via the `spot` arg
    
    
    # Require spot endpoint (`spot` arg unnecessary)
    session_auth.get_wallet_balance(coin="BTC")"""