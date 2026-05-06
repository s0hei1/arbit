from typing import Callable, Awaitable

from app.models import OrderBook
from app.static_models.exchanges import Exchange
from centrifuge import Client, SubscriptionEventHandler, PublicationContext
import asyncio
from dataclasses import dataclass
import datetime as dt


@dataclass
class ExchangeEventModel:
    exchange_name : str
    key : str
    event_timestamp: float
    data : dict

class ExchangeEventHandler(SubscriptionEventHandler):

    def __init__(self,exchange : Exchange,key : str ,queue : asyncio.Queue[ExchangeEventModel]):
        self.exchange = exchange
        self.queue = queue
        self.key = key

    async def on_publication(self, ctx: PublicationContext) -> None:
        await self.queue.put(ExchangeEventModel(
            exchange_name= self.exchange.name,
            event_timestamp= dt.datetime.now().timestamp(),
            data=ctx.pub.data,
            key = self.key
        ))

class MultipleExchangeStreaming:

    @dataclass
    class _ExchangeStreamModel:
        exchange : Exchange
        client : Client

    def __init__(self, *exchanges : Exchange):
        self._exchange_stream_models = [
            _ExchangeStreamModel(
                exchange = ex,
            )
            for ex in exchanges
        ]

    async def start(self):
        web_socket_clients =[]
        for exchange in self.exchanges:
            web_socket_clients.append(
                Client(
                    address= '',
                )
            )




