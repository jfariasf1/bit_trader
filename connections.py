from config import api
from pybit import usdt_perpetual  # <-- import HTTP & WSS for inverse perp
from pybit import inverse_perpetual
from pybit import spot
from pybit import HTTP

session_auth_ws = ""
session_auth_http = ""
session_noauth = ""

session_trading = ""
active_trade = False


def unauthUsdtHTTP():
    return usdt_perpetual.HTTP(endpoint=api.TEST_ENDPOINT)


def unauthInverseperpHTTP():
    return inverse_perpetual.HTTP(endpoint=api.TEST_ENDPOINT)


def usdtPerpHTTP():
    return usdt_perpetual.HTTP(
        endpoint=getEndpointType(),
        api_key=api.API_KEY,
        api_secret=api.API_SECRET
    )


def inversePerpHTTP():
    return inverse_perpetual.HTTP(
        endpoint=getEndpointType(),
        api_key=api.API_KEY,
        api_secret=api.API_SECRET
    )


def usdtSpotHTTP():
    return spot.HTTP(
        endpoint=getEndpointType(),
        api_key=api.API_KEY,
        api_secret=api.API_SECRET
    )


def usdtSpotWSS():
    return spot.WebSocket(
        test=api.TESTNET,
        api_key=api.API_KEY,  # omit the api_key & secret to connect w/o authentication
        api_secret=api.API_SECRET,
        ping_interval=api.WS_INTERVAL,  # the default is 30
        ping_timeout=api.WS_TIMEOUT  # the default is 10
    )


def usdtPerpWSS():
    return usdt_perpetual.WebSocket(
        test=api.TESTNET,
        api_key=api.API_KEY,  # omit the api_key & secret to connect w/o authentication
        api_secret=api.API_SECRET,
        ping_interval=api.WS_INTERVAL,  # the default is 30
        ping_timeout=api.WS_TIMEOUT  # the default is 10
    )


def inversePerpWSS():
    return inverse_perpetual.WebSocket(
        test=api.TESTNET,
        api_key=api.API_KEY,  # omit the api_key & secret to connect w/o authentication
        api_secret=api.API_SECRET,
        ping_interval=api.WS_INTERVAL,  # the default is 30
        ping_timeout=api.WS_TIMEOUT  # the default is 10
    )


def isTest():
    return api.TESTNET


def getEndpointType():
    if api.TESTNET:
        return api.TEST_ENDPOINT
    else:
        return api.PRODUCTION_ENDPOINT


def getEndpoint(connectionType):
    if connectionType == api.HTTP_PERPETUALS:
        return usdtPerpHTTP()
    elif connectionType == api.HTTP_INVERSE_PERPETUALS:
        return inversePerpHTTP()
    elif connectionType == api.HTTP_SPOT:
        return usdtSpotHTTP()
    elif connectionType == api.WS_PERPETUALS:
        return usdtPerpWSS()
    elif connectionType == api.WS_SPOT:
        return usdtSpotWSS()
    elif connectionType == api.UNAUTH_HTTP:
        return unauthUsdtHTTP()
    else:
        raise Exception("Unknown connection type")
