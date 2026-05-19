import asyncio
from centrifuge import SubscriptionEventHandler, PublicationContext, SubscribingContext, SubscribedContext, \
    UnsubscribedContext,JoinContext,LeaveContext,SubscriptionErrorContext
import logging

class EventHandler(SubscriptionEventHandler):

    def __init__(self, queue: asyncio.Queue[dict]):
        self.queue = queue

    async def on_publication(self, ctx: PublicationContext) -> None:
        await self.queue.put(ctx.pub.data)


    async def on_subscribing(self, ctx: SubscribingContext) -> None:
        logging.debug("On Subscribing")

    async def on_subscribed(self, ctx: SubscribedContext) -> None:
        logging.debug("On Subscribed")

    async def on_unsubscribed(self, ctx: UnsubscribedContext) -> None:
        logging.debug("On Unsubscribed")

    async def on_join(self, ctx: JoinContext) -> None:
        logging.debug("On Leave")

    async def on_leave(self, ctx: LeaveContext) -> None:
        logging.debug("On Leave")

    async def on_error(self, ctx: SubscriptionErrorContext) -> None:
        logging.debug("On Error")
