from __future__ import annotations
import asyncio
import numpy as np
from app.models import OrderBook
from app.static_models.common_symbols import SharedSymbol, SharedSymbols
from third_party.bitpinpy.web_socket_client._ws_client import BitpinWebSocketClient
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient


class OrderBookStreaming():
    def __init__(self,symbol : SharedSymbol, ):
        self.symbol = symbol
        self.bitpin = BitpinWebSocketClient()
        self.nobitex = NobipyWebSocketClient()

    async def run(self):
        await self.bitpin.connect()
        await self.nobitex.connect()

        gen_nobitex = self.nobitex.channel_order_book(self.symbol.nobitex_name, yield_as_dict=True)
        gen_bitpin = self.bitpin.channel_order_book(self.symbol.bitpin_name, yield_as_dict=True)
        np.set_printoptions(suppress=True)

        while True:

            ob_nobitex = OrderBook.from_nobitex(await anext(gen_nobitex))
            ob_bitpin = OrderBook.from_bitpin(await anext(gen_bitpin))

            if ob_nobitex.last_bid[0] > ob_bitpin.last_ask[0]:
                print(f"Trigger Nobitex : {ob_nobitex.last_bid} > {ob_bitpin.last_ask}")

            if ob_bitpin.last_bid[0] > ob_nobitex.last_ask[0]:
                print(f"Trigger Bitpin : {ob_bitpin.last_bid} > {ob_nobitex.last_ask}")

            print("Running")

o = OrderBookStreaming(SharedSymbols.TRXUSDT)
asyncio.run(o.run())
