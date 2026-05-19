from app.static_models.exchanges import SupportedExchanges
from typing import Protocol


class ExchangeAsyncApiClientProtocol(Protocol):

    async def set_order(self,*args,**kwargs) -> ...:
        ...





class SharedExchange:

    def __init__(self):
        pass


    async def set_order(self,) -> ...: