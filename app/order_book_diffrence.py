from __future__ import annotations
import asyncio
import numpy as np
from app.models import OrderBook
from app.static_models.common_symbols import SharedSymbol, SharedSymbols
from app.tools.app_logs import setup_logging
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient
import logging

setup_logging(default_level=logging.INFO)

logger = logging.getLogger(__name__)

class ArbitOrderBookTrader():
    def __init__(self, *symbols: SharedSymbol):
        self.symbols = symbols
        self.queue = asyncio.Queue()

    async def _stream(self, symbol: SharedSymbol):

        nobitex = NobipyWebSocketClient()

        await nobitex.connect()

        gen_nobitex = nobitex.channel_order_book(symbol.nobitex_name, yield_as_dict=True)
        np.set_printoptions(suppress=True)

        while True:
            ob_nobitex = OrderBook.from_nobitex(await anext(gen_nobitex))

            logger.info(ob_nobitex.size())

            await self.queue.put({
                'symbol': symbol.name,
                'diff': ob_nobitex.last_ask_price - ob_nobitex.last_bid_price,
                'commission': (ob_nobitex.last_ask_price + ob_nobitex.last_bid_price) * 0.0014,
            }
            )

    async def run(self):

        for symbol in self.symbols:
            asyncio.create_task(self._stream(symbol))

        while True:
            price_diff = await self.queue.get()

            # logger.info(price_diff)


o = ArbitOrderBookTrader(
    SharedSymbols.TONUSDT,
)
asyncio.run(o.run())

