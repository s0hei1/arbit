from __future__ import annotations
import asyncio
import numpy as np
from app.models import OrderBook
from app.static_models.common_symbols import SharedSymbol, SharedSymbols
from app.static_models.exchanges import Exchange, SupportedExchanges
from third_party.bitpinpy.web_socket_client._ws_client import BitpinWebSocketClient
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient
from dataclasses import dataclass
from random import randint


@dataclass
class Trigger:
    value : int
    symbol : str

class ArbitOrderBookTriggering():
    def __init__(self,queue : asyncio.Queue,symbol : str):
        self.queue = queue
        self.symbol = symbol

    async def run(self):




        while True:
            value_a = randint(1, 100)
            value_b = randint(1, 100)
            # print(value_a,'>?',value_b)
            if value_a > value_b:
                await self.queue.put(
                    Trigger(value_a,self.symbol)
                )

            await asyncio.sleep(2)



class ArbitOrderBookTrader:

    def __init__(self, *symbols : str):
        self.queue = asyncio.Queue()

        self.trigger_checkers = [ArbitOrderBookTriggering(
            queue = self.queue,
            symbol = symbol
        ) for symbol in symbols]



    async def start(self):

        for i in self.trigger_checkers:
            asyncio.create_task(i.run())


        while True:
            print(await self.queue.get())
            await asyncio.sleep(0.1)







trader = ArbitOrderBookTrader("ETHUSDT", "BTCUSDT")

asyncio.run(trader.start())