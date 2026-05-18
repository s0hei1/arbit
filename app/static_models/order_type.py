from dataclasses import dataclass
from typing import Literal, ClassVar


@dataclass
class OrderType:
    order_side: Literal['BUY', 'SELL']
    order_type: Literal['LIMIT', 'MARKET','STOP_LIMIT', 'STOP_MARKET']
    name: str


    def is_buy(self):
        return self.order_side == "BUY"
    def is_sell(self):
        return self.order_side == "SELL"


class OrderTypes:
    buy_limit: ClassVar[OrderType] = OrderType(order_side="BUY", name="Buy Limit", order_type='LIMIT')
    buy_market: ClassVar[OrderType] = OrderType(order_side="BUY", name="Buy Market", order_type='MARKET')

    sell_limit: ClassVar[OrderType] = OrderType(order_side="SELL", name="Sell Limit", order_type='LIMIT')
    sell_market: ClassVar[OrderType] = OrderType(order_side="SELL", name="Sell Market", order_type='MARKET')

    @classmethod
    def get_order_types(cls) -> list[OrderType]:
        return [
            getattr(cls, i)
            for i in OrderType.__annotations__
            if isinstance(getattr(cls, i), OrderType)
        ]


    @classmethod
    def get_type_names(self) -> list[str]:
        return [i.name for i in self.get_order_types()]

    @classmethod
    def get_type_by_name(self, input_name: str) -> OrderType:
        return first([i for i in self.get_order_types() if i.name == input_name])

