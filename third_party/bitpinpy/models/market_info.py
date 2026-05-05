from __future__ import annotations
from dataclasses import dataclass

from third_party.bitpinpy.models.abstracts import DataclassMappings


@dataclass
class GetNetworksRequest(DataclassMappings):
    code : str | None = None
    can_deposit : bool | None = True
    can_withdraw : bool | None = True

@dataclass
class GetCurrencyNetworksRequest(DataclassMappings):
    currency_code : str



@dataclass
class CurrencyResponse:
    currency : str
    name : str
    tradable : bool
    precision  : str

    @staticmethod
    def from_dict(data: dict) -> CurrencyResponse:
        return CurrencyResponse(
            currency=data["currency"],
            name=data["name"],
            tradable=data["tradable"],
            precision=data["precision"],
        )


@dataclass
class MarketResponse:
    symbol: str
    name: str
    base: str
    quote: str
    tradable: bool
    price_precision: int
    base_amount_precision: int
    quote_amount_precision: int

    @staticmethod
    def from_dict(data: dict) -> MarketResponse:
        return MarketResponse(
            symbol=data["symbol"],
            name=data["name"],
            base=data["base"],
            quote=data["quote"],
            tradable=data["tradable"],
            price_precision=data["price_precision"],
            base_amount_precision=data["base_amount_precision"],
            quote_amount_precision=data["quote_amount_precision"],
        )

@dataclass
class NetworkResponse:
    id: str
    code: str
    title: str
    title_fa: str
    can_deposit: bool
    can_withdraw: bool
    address_pattern: str

    @staticmethod
    def from_dict(data: dict) -> NetworkResponse:
        return NetworkResponse(
            id=data["id"],
            code=data["code"],
            title=data["title"],
            title_fa=data["title_fa"],
            can_deposit=data["can_deposit"],
            can_withdraw=data["can_withdraw"],
            address_pattern=data["address_pattern"],
        )

@dataclass
class CurrencyNetworkResponse:
    network : NetworkResponse
    deposit_under_maintenance : bool
    withdraw_under_maintenance : bool

    @staticmethod
    def from_dict(data: dict) -> CurrencyNetworkResponse:
        return CurrencyNetworkResponse(
            network=NetworkResponse.from_dict(data["network"]),
            deposit_under_maintenance=data["deposit_under_maintenance"],
            withdraw_under_maintenance=data["withdraw_under_maintenance"],
        )

@dataclass
class TickersResponse:
    symbol : str
    price : str
    daily_change_price : float
    low : str
    high : str
    timestamp : float

    @staticmethod
    def from_dict(data: dict) -> TickersResponse:
        return TickersResponse(
            symbol = data['symbol'],
            price = data['price'],
            daily_change_price = data['daily_change_price'],
            low = data['low'],
            high = data['high'],
            timestamp = data['timestamp'],
        )

@dataclass
class OrderBookEntry:
    price : str
    volume : str

    @staticmethod
    def from_dict(data: dict) -> OrderBookEntry:
        return OrderBookEntry(
            price = data['price'],
            volume = data['volume'],
        )


@dataclass
class OrderBookResponse:
    asks: list[OrderBookEntry]
    bids: list[OrderBookEntry]

    @staticmethod
    def from_dict(data: dict) -> OrderBookResponse:
        return OrderBookResponse(
            asks=[OrderBookEntry(price=i[0], volume=i[1]) for i in data['asks']],
            bids=[OrderBookEntry(price=i[0], volume=i[1]) for i in data['bids']],
        )

@dataclass
class MatchResponse:
    id : str
    price : str
    base_amount : str
    quote_amount : str
    side : str

    @staticmethod
    def from_dict(data: dict) -> MatchResponse:
        return MatchResponse(
            id = data['id'],
            price = data['price'],
            base_amount = data['base_amount'],
            quote_amount = data['quote_amount'],
            side = data['side'],
        )

@dataclass
class CommissionsResponse:
    market : int
    symbol : str
    maker : float
    taker : float

    @staticmethod
    def from_dict(data: dict) -> CommissionsResponse:
        return CommissionsResponse(
            market = data['market'],
            symbol = data['symbol'],
            maker = data['maker'],
            taker = data['taker'],
        )
