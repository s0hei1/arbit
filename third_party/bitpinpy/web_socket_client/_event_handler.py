import asyncio
from centrifuge import SubscriptionEventHandler, PublicationContext


class EventHandler(SubscriptionEventHandler):

    def __init__(self, queue : asyncio.Queue[dict]):
        self.queue = queue

    async def on_publication(self, ctx: PublicationContext) -> None:
        await self.queue.put(ctx.pub.data)

