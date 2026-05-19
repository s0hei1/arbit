from __future__ import annotations
import asyncio
import numpy as np
from app.models import OrderBook
from app.static_models.common_symbols import SharedSymbol, SharedSymbols
from app.static_models.exchanges import Exchange, SupportedExchanges
from app.tools.app_logs import setup_logging
from third_party.bitpinpy.web_socket_client._ws_client import BitpinWebSocketClient
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient
from dataclasses import dataclass
import logging

setup_logging(default_level = logging.INFO)

logger = logging.getLogger(__name__)

@dataclass
class TradeTrigger:
    symbol : SharedSymbol
    exchange_buy : SupportedExchanges
    buy_price : float
    exchange_sell : SupportedExchanges
    sell_price : float
    volume : float

    @property
    def buy_volume(self):
        return self.volume * self.buy_price

    @property
    def sell_volume(self):
        return self.volume * self.sell_price


class ArbitOrderBookTrader():
    def __init__(self,*symbols : SharedSymbol):
        self.symbols = symbols
        self.queue = asyncio.Queue()

    async def _stream(self, symbol : SharedSymbol):

        bitpin = BitpinWebSocketClient()
        nobitex = NobipyWebSocketClient()

        await bitpin.connect()
        await nobitex.connect()

        gen_nobitex = nobitex.channel_order_book(symbol.nobitex_name, yield_as_dict=True)
        gen_bitpin = bitpin.channel_order_book(symbol.bitpin_name, yield_as_dict=True)
        np.set_printoptions(suppress=True)

        while True:

            ob_nobitex = OrderBook.from_nobitex(await anext(gen_nobitex))
            ob_bitpin = OrderBook.from_bitpin(await anext(gen_bitpin))

            logger.debug(f'{symbol.name} in Nobitex, bid= {ob_nobitex.last_bid_price}, ask= {ob_nobitex.last_ask_price}')
            logger.debug(f'{symbol.name} in BITPIN, bid= {ob_bitpin.last_bid_price}, ask= {ob_bitpin.last_ask_price}')

            if ob_nobitex.last_bid_price > ob_bitpin.last_ask_price:
                await self.queue.put(TradeTrigger(
                    symbol = symbol,
                    exchange_buy = 'bitpin',
                    buy_price = ob_bitpin.last_ask_price,
                    exchange_sell = 'nobitex',
                    sell_price = ob_nobitex.last_bid_price,
                    volume = min(ob_nobitex.last_ask_volume, ob_bitpin.last_bid_volume),
                ))



            if ob_bitpin.last_bid_price > ob_nobitex.last_ask_price:
                await self.queue.put(TradeTrigger(
                    symbol=symbol,
                    exchange_buy='bitpin',
                    buy_price=ob_nobitex.last_ask_price,
                    exchange_sell='nobitex',
                    sell_price=ob_bitpin.last_bid_price,
                    volume=min(ob_bitpin.last_ask_volume, ob_nobitex.last_bid_volume),
                ))


            logger.debug("App is Running")

    async def run(self):

        for symbol in self.symbols:
            asyncio.create_task(self._stream(symbol))

        t = asyncio.current_task()
        t.

        while True:
            trading_trigger = await self.queue.get()

            profit = abs(trading_trigger.buy_volume - trading_trigger.sell_volume)
            net_profit = profit - (trading_trigger.buy_volume + trading_trigger.sell_volume) * 0.0015

            if net_profit > 0:
                logging.warning(trading_trigger)
                logging.warning(f'buy_volume -> {trading_trigger.buy_volume}')
                logging.warning(f'profit -> {profit}')
                logging.warning(f'net_profit -> {net_profit}')






o = ArbitOrderBookTrader(SharedSymbols.TRXUSDT, SharedSymbols.ETHUSDT,SharedSymbols.BTCUSDT)
asyncio.run(o.run())
