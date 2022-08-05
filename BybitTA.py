import json


import pandas as pd

# Incorrectly marked as unused
import pandas_ta as ta

import connections
from Trading import Trading



class BybitTA(object):
    candle_data_json = ""
    session_auth = ""
    BUY= "Buy"
    SELL = "Sell"
    test_value=0.014


    def updateTA(self, new_value):
        print("wtf")
        if new_value["start"] != self.candle_data_json[-1]["start"]:
            print("adding new value")
            self.addLastValue(new_value)
            self.analyzeStrategies()

    def addLastValue(self, new_value):
        #self.candle_data_json.pop(0)
        self.candle_data_json.append(new_value)

    # RSI = 100 - (100 / (1 + RS))
    # overbought 70
    # oversold 30
    # neutral 50

    def calculateRSI(self):

        df = pd.read_json(json.dumps(self.candle_data_json), orient="records")
        df.ta.rsi(close='close', length=self.rsi_length, append=True, index="start")

        #print(df.tail(1).query("RSI_14 < 30"))

        print(df.tail())
        return(df.tail(5))
    # Money Flow Index
    # MFI = 100 - (100 / (1 + MFR)) Money Flow Ratio
    # overbought 80
    # oversold 20
    # neutral 50


    def calculateMFI(self):
        df = pd.read_json(json.dumps(self.candle_data_json), orient="records")
        df.ta.mfi(close='close', length=self.rsi_length, append=True, index="start")
        #print(df)
        print(df.tail())
        return df.tail(5)
       # print(df.tail())

    def calculateTrade(self, side, qty,type):

        Trading.openTradeMarket(self,self.SYMBOL, qty=qty, side=side)

           # self.session_auth.position_stream(
            #    self.handle_message
            #)
    def analyzeStrategies(self):
        ## Initial thoughts
        print("Analyzing strategies")
        rsi_strat = self.calculateRSI()

        if rsi_strat.query("RSI_%s < 30" %self.rsi_length).size != 0:
            print("RSI buying opportunity")
            print(rsi_strat)
            self.calculateTrade(self.BUY, self.test_value, "market")


        elif rsi_strat.query("RSI_%s > 70" %self.rsi_length).size != 0:
            print("RSI selling opportunity")
            print(rsi_strat)
            self.calculateTrade(self.SELL, self.test_value, "market")


        mfi_strat = self.calculateMFI()

        if mfi_strat.query("MFI_%s < 20" %self.rsi_length).size != 0:
            print("MFI buying opportunity")
            print(mfi_strat)
            self.calculateTrade(self.BUY, self.test_value, "market")
        elif mfi_strat.query("MFI_%s > 80" %self.rsi_length).size != 0:
            print("MFI selling opportunity")
            print(mfi_strat)
            self.calculateTrade(self.SELL, self.test_value, "market")
        #Trading.getSymbolsData(self)

    def __init__(self, candle_data, rsi_length):
        self.rsi_length = rsi_length

        self.candle_data_json = candle_data

        print(candle_data)

        self.calculateRSI()
