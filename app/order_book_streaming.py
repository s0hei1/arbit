from __future__ import annotations
import asyncio

from app.models import OrderBook
from third_party.bitpinpy.web_socket_client._ws_client import BitpinWebSocketClient
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient



async def main():
    bitpin = BitpinWebSocketClient()
    nobitex = NobipyWebSocketClient()

    await bitpin.connect()
    await nobitex.connect()

    gen_nobitex = nobitex.channel_order_book("ETHUSDT",yield_as_dict=True)
    gen_bitpin = bitpin.channel_order_book("ETH_USDT",yield_as_dict=True)

    while True:
        # read both feeds concurrently (non‑blocking)
        order_nobitex = await anext(gen_nobitex)
        order_bitpin = await anext(gen_bitpin)

        print(OrderBook.from_nobitex(order_nobitex).get_last_suggests())
        print(OrderBook.from_bitpin(order_bitpin).get_last_suggests())

        await asyncio.sleep(1)

asyncio.run(main())