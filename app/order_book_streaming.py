from __future__ import annotations
import asyncio
import numpy as np
from app.models import OrderBook
from app.static_models.common_symbols import SharedSymbol, SharedSymbols
from app.static_models.exchanges import Exchange, SupportedExchanges
from third_party.bitpinpy.web_socket_client._ws_client import BitpinWebSocketClient
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient
from dataclasses import dataclass

@dataclass
class TradeTrigger:
    symbol : SharedSymbol
    exchange_buy : SupportedExchanges
    buy_price : float
    exchange_sell : SupportedExchanges
    sell_price : float
    volume : float

class ArbitOrderBookTriggering():
    def __init__(self,symbol : SharedSymbol, queue : asyncio.Queue):
        self.symbol = symbol
        self.bitpin = BitpinWebSocketClient()
        self.nobitex = NobipyWebSocketClient()
        self.queue = queue

    async def run(self):

        await self.bitpin.connect()
        await self.nobitex.connect()

        gen_nobitex = self.nobitex.channel_order_book(self.symbol.nobitex_name, yield_as_dict=True)
        gen_bitpin = self.bitpin.channel_order_book(self.symbol.bitpin_name, yield_as_dict=True)
        np.set_printoptions(suppress=True)

        while True:
            ob_nobitex = OrderBook.from_nobitex(await anext(gen_nobitex))
            ob_bitpin = OrderBook.from_bitpin(await anext(gen_bitpin))

            if ob_nobitex.last_bid_price > ob_bitpin.last_ask_price:
                self.queue.put_nowait(TradeTrigger(
                    symbol = self.symbol,
                    exchange_buy = 'bitpin',
                    buy_price = ob_bitpin.last_ask_price,
                    exchange_sell = 'nobitex',
                    sell_price = ob_nobitex.last_bid_price,
                    volume = 10,
                ))

            if ob_bitpin.last_bid_price > ob_nobitex.last_ask_price:
                print(f"Trigger Bitpin : {ob_bitpin.last_bid_price} > {ob_nobitex.last_ask_price}")

            await asyncio.sleep(0.1)
            print(f'Running')

