import asyncio
from typing import AsyncGenerator, Any

from centrifuge import Client, SubscriptionState
from third_party.bitpinpy.models.market_info import OrderBookResponse
from third_party.bitpinpy.web_socket_client._event_handler import EventHandler

class BitpinWebSocketClient:

    def __init__(self):
        self.client = Client('wss://centrifugo.bitpin.ir/connection/websocket')
        self._queue = asyncio.Queue()

    async def connect(self):
        await self.client.connect()

    async def disconnect(self):
        await self.client.disconnect()

    async def cancel_subscribe(self, channel : str):
        await self.client.get_subscription(channel).unsubscribe()

    async def channel_order_book(self, symbol_name : str, yield_as_dict : bool = False)  -> AsyncGenerator[dict | OrderBookResponse,Any] :
        _channel = f"orderbook:{symbol_name}"
        _sub = self.client.get_subscription(_channel)
        if _sub is None:
            _sub = self.client.new_subscription(
                channel =_channel,
                events=EventHandler(
                    queue=self._queue
                )
            )

        if _sub.state == SubscriptionState.UNSUBSCRIBED:
            await _sub.subscribe()

        if yield_as_dict:
            while True:
                print(await self._queue.get())
                yield await self._queue.get()
        else:
            while True:
                yield OrderBookResponse.from_dict(await self._queue.get())


