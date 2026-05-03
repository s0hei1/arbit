import asyncio

from centrifuge import Client, SubscriptionEventHandler, SubscribingContext, SubscribedContext, UnsubscribedContext, \
    JoinContext, PublicationContext, LeaveContext, SubscriptionErrorContext, ClientEventHandler, \
    ServerPublicationContext, ConnectingContext, ConnectedContext, DisconnectedContext, ErrorContext, \
    ServerSubscribedContext, ServerSubscribingContext, ServerUnsubscribedContext
from src.models import GetOrderBookResponse
from typing import AsyncGenerator
from typing import Callable
from dataclasses import dataclass
url = "wss://ws.nobitex.ir/connection/websocket"



class EventHandler(SubscriptionEventHandler):

    def __init__(self, queue : asyncio.Queue[dict]):
        self.queue = queue

    async def on_publication(self, ctx: PublicationContext) -> None:
        await self.queue.put(ctx.pub.data)


class WebSocketClient:

    def __init__(self):
        self.client = Client('wss://ws.nobitex.ir/connection/websocket')
        self._queue = asyncio.Queue()

    async def connect(self):
        await self.client.connect()

    async def disconnect(self):
        await self.client.disconnect()

    async def cancel_subscribe(self, channel : str):
        await self.client.get_subscription(channel).unsubscribe()

    async def channel_order_book(self, symbol_name : str):
        channel = f"public:orderbook-{symbol_name}"
        sub = self.client.new_subscription(
            channel =channel,
            events=EventHandler(
                queue=self._queue
            )
        )
        await sub.subscribe()
        while True:
            data = await self._queue.get()
            yield data

async def main():
    client = WebSocketClient()
    await client.connect()

    result = client.channel_order_book('BTCIRT')

    async for i in result:
        print(i)


asyncio.run(main())
