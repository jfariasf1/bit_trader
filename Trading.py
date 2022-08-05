import json
import sys
import connections

class Trading:
    symbols_data = ""
#https://bybit-exchange.github.io/docs/linear/?python--pybit#t-placeactive

    # All trading options only happen on HTTP api

    def openTradeLimit(self, symbol, qty, price, volume):
        session_auth = connections.getEndpoint((connections.session_trading))
        session_auth.place_active_order(
            symbol=symbol,
            side="Sell",
            order_type="Limit",
            qty=qty,
            price=price,
            time_in_force="GoodTillCancel",
            reduce_only=False,
            close_on_trigger=False
        )

    def openTradeMarket(self, symbol, qty, side):
        session_auth = connections.getEndpoint(connections.session_trading)
        print(symbol, qty, side)
        print(session_auth.__class__.__name__)
        session_auth.place_active_order(
            symbol=symbol,
            side=side,
            order_type="Market",
            qty=qty,
            reduce_only=False,
            close_on_trigger=False,
            time_in_force="GoodTillCancel"
        )

    def closeTrade(self, symbol):
        # Closing trades seems to use ImmediateOrCancel. Dangerous if fails.
        session_auth = connections.getEndpoint((connections.session_trading))
        session_auth.close_position()(
            symbol=symbol
        )

    def getActiveOrders(self, symbol):
        session_auth = connections.getEndpoint((connections.session_trading))
        session_auth.get_active_order(
            symbol=symbol
        )

    def setLeverage(self, symbol, buy_leverage, sell_leverage):
        session_auth = connections.getEndpoint((connections.session_trading))
        session_auth.set_leverage(
            symbol="symbol",
            buy_leverage=buy_leverage,
            sell_leverage=sell_leverage
        )

    def getLeverage(self, symbol):
        session_auth = connections.getEndpoint((connections.session_trading))
        session_auth.get_leverage(
            symbol=symbol
        )

    def setIsolatedMode(self, symbol, buy_leverage, sell_leverage):
        session_auth = connections.getEndpoint((connections.session_trading))
        session_auth.cross_isolated_margin_switch(
            symbol=symbol,
            is_isolated=True,
            buy_leverage=buy_leverage,
            sell_leverage=sell_leverage
        )
    def getSymbolsData(self):
        connections.session_noauth = connections.unauthUsdtHTTP()
        self.symbols_data=connections.session_noauth.query_symbol()["result"]
        print("size of symbols data", sys.getsizeof(self.symbols_data))
