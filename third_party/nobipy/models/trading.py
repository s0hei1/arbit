from __future__ import annotations
from dataclasses import dataclass, asdict
from third_party.nobipymodels.abstracts import DataclassMappings
from typing import Literal,Any
from datetime import datetime


ExecutionType = Literal['limit', 'market','stop_limit', 'stop_market']
TradeType = Literal['margin', 'spot']
OrderStatus = Literal['all', 'open', 'close', 'done']
OrderSide = Literal['sell', 'buy']
OrderingType = Literal['id', '-id-', 'created_at', 'created_at-', 'price', 'price-']
UpdateOrderStatus = Literal['new','active','inactive','canceled']

@dataclass(frozen=True)
class AddOrderRequest(DataclassMappings):
    type: OrderSide
    srcCurrency: str
    dstCurrency: str
    amount: float
    price: float | None
    execution: ExecutionType = 'limit'
    stopPrice: float | None = None
    clientOrderId: str | None = None

    def __post_init__(self):
        if self.execution in ('stop_limit', 'stop_market') and self.stopPrice is None:
            raise ValueError('stopPrice can not be None at [stop_limit , stop_market] execution types')

@dataclass(frozen=True)
class CancelOrdersRequest(DataclassMappings):
    hours: float | None = None
    execution: ExecutionType | None = None
    tradeType: TradeType | None = None
    srcCurrency: str | None = None
    dstCurrency: str | None = None


@dataclass
class GetOrderStatusRequest(DataclassMappings):
    id: int | None = None
    clientOrderId: str | None = None

    def __post_init__(self):
        if self.id is None and self.clientOrderId is None:
            raise ValueError("Either id or clientOrderId must be provided")

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)

        if self.id is None:
            d.pop('id')
        if self.clientOrderId is None:
            d.pop('clientOrderId')

        return d

@dataclass
class GetSpotOrdersRequest(DataclassMappings):
    status : OrderStatus = 'open'
    type: OrderSide | None = None
    execution: ExecutionType | None = None
    tradeType: TradeType | None = None
    srcCurrency: str | None = None
    dstCurrency: str | None = None
    details: int = 1
    fromId: int = 1
    order: OrderingType | None = None

@dataclass
class GetTradesRequest(DataclassMappings):
    srcCurrency: str | None = None
    dstCurrency: str | None = None
    fromId: int | None = None

@dataclass
class UpdateOrderStatusRequest(DataclassMappings):
    status: UpdateOrderStatus
    order: int | None = None
    clientOrderId: str | None = None

@dataclass
class SpotTrade:
    id: int
    orderId: int
    srcCurrency: str
    dstCurrency: str
    market: str
    timestamp: str
    type: str
    price: str
    amount: str
    total: str
    fee: str

    @staticmethod
    def from_dict(data: dict):
        return SpotTrade(
            id=data["id"],
            orderId=data["orderId"],
            srcCurrency=data["srcCurrency"],
            dstCurrency=data["dstCurrency"],
            market=data["market"],
            timestamp=data["timestamp"],
            type=data["type"],
            price=data["price"],
            amount=data["amount"],
            total=data["total"],
            fee=data["fee"],
        )


@dataclass
class SpotTradesResponse:
    status: str
    trades: list[SpotTrade]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict):
        return SpotTradesResponse(
            status=data["status"],
            trades=[SpotTrade.from_dict(t) for t in data.get("trades", [])],
            hasNext=data.get("hasNext", False),
        )

@dataclass
class OrderEntry:

    type: OrderSide
    execution: str
    tradeType: str
    srcCurrency: str
    dstCurrency: str
    price: str
    amount: str
    totalPrice: str
    totalOrderPrice: str
    matchedAmount: str
    unmatchedAmount: str
    clientOrderId: str | None = None
    id: int | None = None
    status: str | None = None
    fee: str | None = None
    created_at : datetime | None = None
    averagePrice: str | None = None
    market: str | None = None
    partial: bool | None = None

    @staticmethod
    def from_dict(data: dict) -> OrderEntry:
        return OrderEntry(
            type=data["type"],
            execution=data["execution"],
            tradeType=data["tradeType"],
            srcCurrency=data["srcCurrency"],
            dstCurrency=data["dstCurrency"],
            price=data["price"],
            amount=data["amount"],
            totalPrice=data["totalPrice"],
            totalOrderPrice=data["totalOrderPrice"],
            matchedAmount=data["matchedAmount"],
            unmatchedAmount=data["unmatchedAmount"],
            clientOrderId=data.get("clientOrderId"),
            id=data["id"] if "id" in data else None,
            status=data["status"] if "status" in data else None,
            fee=data["fee"] if "fee" in data else None,
            created_at=datetime.fromisoformat(data["created_at"].replace('Z', '+00:00')) if "created_at" in data else None,
            averagePrice=data["averagePrice"] if "averagePrice" in data else None,
            market=data["market"] if "market" in data else None,
            partial=data["partial"] if "partial" in data else None,
        )

@dataclass
class AddOrderResponse:
    status: str
    order: OrderEntry

    @staticmethod
    def from_dict(data: dict) -> AddOrderResponse:
        return AddOrderResponse(
            status=data["status"],
            order=OrderEntry.from_dict(data["order"]),
        )


@dataclass
class GetOrderStatusResponse:
    status: str
    order: OrderEntry

    @staticmethod
    def from_dict(data: dict):
        return GetOrderStatusResponse(
            status=data["status"],
            order=OrderEntry.from_dict(data["order"]),
        )


@dataclass
class GetOrdersResponse:
    status: str
    orders: list[OrderEntry]

    @staticmethod
    def from_dict(data: dict):
        return GetOrdersResponse(
            status=data["status"],
            orders=[OrderEntry.from_dict(o) for o in data.get("orders", [])],
        )

@dataclass
class UpdateOrderStatusResponse:
    status: str
    order: OrderEntry

    @staticmethod
    def from_dict(data: dict) -> UpdateOrderStatusResponse:
        return UpdateOrderStatusResponse(
            status=data["status"],
            order=OrderEntry.from_dict(data["order"]),
        )

