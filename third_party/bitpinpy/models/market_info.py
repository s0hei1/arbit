from __future__ import annotations
from dataclasses import dataclass
from typing import List

from src_bitpinpy.models.abstracts import DataclassMappings


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

