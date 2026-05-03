from __future__ import annotations
from dataclasses import dataclass,asdict
from third_party.nobipy.models.abstracts import DataclassMappings

@dataclass
class GetMarketHistoryRequest(DataclassMappings):
    symbol : str
    resolution : str
    to : int
    page  : int
    from_ : int | None = None
    countback : int | None = None

    def to_dict(self):
        d = asdict(self)
        d['from'] = d.pop('from_')
        return d



@dataclass
class MarketHistoryResponse:
    s: str
    t: list[int]
    o: list[int]
    h: list[int]
    l: list[int]
    c: list[int]
    v: list[float]

    @staticmethod
    def from_dict(data: dict) -> MarketHistoryResponse:
        return MarketHistoryResponse(
                s=data["s"],
                t=data["t"],
                o=data["o"],
                h=data["h"],
                l=data["l"],
                c=data["c"],
                v=data["v"],
            )


@dataclass
class OrderBookEntry:
    price: str
    amount: str

@dataclass
class GetOrderBookResponse:
    status: str
    lastUpdate: int
    lastTradePrice: str
    asks: list[OrderBookEntry]
    bids: list[OrderBookEntry]

    @staticmethod
    def from_dict(data: dict, using_web_sockets : bool = False) -> GetOrderBookResponse:
        return GetOrderBookResponse(
            status='ok' if using_web_sockets else data["status"],
            lastUpdate=data["lastUpdate"],
            lastTradePrice=data["lastTradePrice"],
            asks=[OrderBookEntry(price=a[0], amount=a[1]) for a in data["asks"]],
            bids=[OrderBookEntry(price=b[0], amount=b[1]) for b in data["bids"]],
        )

@dataclass
class GetOrderBookAllEntry:
    lastUpdate: int
    asks: list[OrderBookEntry]
    bids: list[OrderBookEntry]


@dataclass
class GetOrderBookAllResponse:
    status: str
    all: dict[str, GetOrderBookAllEntry]

    @staticmethod
    def from_dict(data: dict) -> GetOrderBookAllResponse:
        return GetOrderBookAllResponse(
            status=data.pop("status"),
            all={
                d: GetOrderBookAllEntry(
                    lastUpdate=data[d]["lastUpdate"],
                    asks=[OrderBookEntry(price=a[0], amount=a[1]) for a in data.get(d)["asks"]],
                    bids=[OrderBookEntry(price=b[0], amount=b[1]) for b in data.get(d)["bids"]],
                ) for d in data},
        )

@dataclass
class GetDepthResponse:
    status: str
    lastUpdate: int
    lastTradePrice: str
    asks: list[OrderBookEntry]
    bids: list[OrderBookEntry]

    @staticmethod
    def from_dict(data: dict) -> GetDepthResponse:
        return GetDepthResponse(
            status=data["status"],
            lastUpdate=data["lastUpdate"],
            lastTradePrice=data["lastTradePrice"],
            asks=[OrderBookEntry(price=a[0], amount=a[1]) for a in data["asks"]],
            bids=[OrderBookEntry(price=b[0], amount=b[1]) for b in data["bids"]],
        )
