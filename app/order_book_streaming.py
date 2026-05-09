from __future__ import annotations
import asyncio
from third_party.bitpinpy.web_socket_client._ws_client import BitpinWebSocketClient
from third_party.nobipy.web_socket_client._ws_client import NobipyWebSocketClient



async def main():
    bitpin = BitpinWebSocketClient()
    nobitex = NobipyWebSocketClient()

    gen_nobitex = nobitex.channel_order_book("BTCIRT",yield_as_dict=True)
    gen_bitpin = bitpin.channel_order_book("BTC_IRT",yield_as_dict=True)

    while True:
        # read both feeds concurrently (non‑blocking)
        order_nobitex = await anext(gen_nobitex)
        order_bitpin = await anext(gen_bitpin)

        iter_nobitex = await aiter(order_nobitex)

        order_book = await anext(iter_nobitex)

        print(order_book)

        await asyncio.sleep(1)

asyncio.run(main())