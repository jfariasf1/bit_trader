# Bit Trader

A simple Bybit bot for trading by using the RSI and TSI indicators. 

It implements basic technical analysis by using the Pandas TA library and the Bybit HTTP and websockets APIs. To
reduce HTTP requests it will continue using websockets information to include in the analysis.

Given the indicators ROI performance this basic bot might be replaced by a TV webhook to use with the Bybit APIs.