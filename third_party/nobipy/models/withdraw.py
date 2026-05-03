from __future__ import annotations
from datetime import datetime
from third_party.nobipy.models.abstracts import DataclassMappings
from typing import Literal
from dataclasses import dataclass

Networks = Literal[
'FIAT_MONEY', 'ETH', 'BSC', 'ADA',
'ALGO', 'APT', 'ARB', 'BCH', 'BNB',
'BTC', 'BTCLN', 'DOGE', 'DOT',
'EOS', 'ETC', 'LTC', 'PMN',
'TRX', 'OMNI', 'ZTRX', 'XLM',
'XMR', 'XRP', 'ATOM', 'EGLD',
'FIL', 'FLR', 'FLOW', 'FTM',
'MATIC', 'AVAX', 'HBAR', 'NEAR',
'TON', 'SOL', 'XTZ', 'ONE'
]

@dataclass(frozen=True)
class WithdrawEntry:
    id: int
    createdAt: datetime | None
    status: str
    amount: str | None
    currency: str
    network: str
    invoice: str | None
    address: str | None
    tag: str | None
    wallet_id: int
    blockchain_url: str | None
    is_cancelable: bool

    @staticmethod
    def from_dict(data: dict) -> WithdrawEntry:
        return WithdrawEntry(
            id=data["id"],
            createdAt=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            status=data["status"],
            amount=data["amount"],
            currency=data["currency"],
            network=data["network"],
            invoice=data.get("invoice"),
            address=data.get("address"),
            tag=data.get("tag"),
            wallet_id=data["wallet_id"],
            blockchain_url=data.get("blockchain_url"),
            is_cancelable=data["is_cancelable"],
        )



@dataclass(frozen=True)
class WithdrawRequest(DataclassMappings):
    wallet : int
    network : str | None = None
    invoice : str | None = None
    amount : int | None = None
    address : str | None = None
    explanations : str | None = None
    noTag : bool | None = False
    tag : str | None = None


    def __post_init__(self):
        if self.invoice is None and self.amount is None and self.address is None:
            raise AttributeError('Invoice And [amount, address] cannot be None at the same time')

@dataclass(frozen=True)
class WithdrawConfirmRequest(DataclassMappings):
    withdraw : int
    otp : int | None



@dataclass(frozen=True)
class WithdrawResponse(DataclassMappings):
    status: str
    withdraw: WithdrawEntry

    @staticmethod
    def from_dict(data: dict) -> WithdrawResponse:
        return WithdrawResponse(
            status=data["status"],
            withdraw=WithdrawEntry.from_dict(data["withdraw"]),
        )

@dataclass(frozen=True)
class WithdrawsResponse(DataclassMappings):
    status: str
    withdraws: list[WithdrawEntry]

    @staticmethod
    def from_dict(data: dict) -> WithdrawsResponse:
        return WithdrawsResponse(
            status=data["status"],
            withdraws=[WithdrawEntry.from_dict(w) for w in data['withdraws']],
        )



