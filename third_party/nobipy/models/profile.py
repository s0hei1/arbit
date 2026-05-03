from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Literal
from datetime import datetime
from third_party.nobipy.models.abstracts import DataclassMappings

TransactionType = Literal[
    'deposit',
    'withdraw',
    'buy',
    'sell',
    'manual',
    'referral',
    'transfer',
    'pnl',
    'delegate',
    'staking',
    'yield_farming',
    'discount',
]
WalletType = Literal['margin', 'spot']

@dataclass
class AddBankAccountRequest(DataclassMappings):
    number : str
    shaba: str
    bank: str

@dataclass
class AddBankCardRequest(DataclassMappings):
    number : str
    bank: str

    def __post_init__(self):
        if not (16 <= len(self.number) <= 20):
            raise ValueError(f'{self.number} is not a valid bank number')

@dataclass
class AddFavoriteMarketsRequest(DataclassMappings):
    market : list[str]

    def to_dict(self) -> dict:
        return {
            "market": ','.join(self.market),
        }

@dataclass
class GenerateWalletAddressRequest(DataclassMappings):
    currency : str | None
    wallet_id : str | None
    network : str | None = None

    def __post_init__(self):
        if self.currency is None and self.wallet_id is None:
            raise ValueError("Currency and Wallet ID cannot be None at same time")

@dataclass
class GetBalanceRequest(DataclassMappings):
    currency : str

@dataclass
class GetDepositsRequest(DataclassMappings):
    wallet : str = 'all'

@dataclass(frozen=True)
class GetStatsRequest(DataclassMappings):
    srcCurrency : list[str]
    dstCurrency : list[str]

    def to_dict(self):
        srcCurrency_str = ','.join(self.srcCurrency)
        dstCurrency_str = ','.join(self.dstCurrency)

        return {
            'srcCurrency' : srcCurrency_str,
            'dstCurrency' : dstCurrency_str,
        }

@dataclass
class GetTransactionsHistoryRequest(DataclassMappings):
    currency: str | None = None
    tp: TransactionType | None = None
    from_: datetime | None = None
    to: datetime | None = None
    from_id: datetime | None = None


    def to_dict(self) -> dict:
        d = asdict(self)
        d['from'] = d.pop('from_')
        keys = list(d.keys())
        for k in keys:
            if d[k] is None:
                d.pop(k)

        return d

@dataclass
class GetUserWalletsByFilteringResponse(DataclassMappings):
    currencies : list[str] | None = None
    type_ : WalletType = 'spot'

    def to_dict(self):
        return {
            'currencies': ', '.join(self.currencies),
            'type': self.type_,
        }

@dataclass
class GetWalletTransactionsRequest(DataclassMappings):
    wallet_id : int

@dataclass
class BalanceResponse:
    balance: str
    status: str

    @staticmethod
    def from_dict(data: dict) -> BalanceResponse:
        return BalanceResponse(
            balance=data["balance"],
            status=data["status"],
        )

@dataclass
class FavoriteMarketsResponse:
    status: str
    favoriteMarkets: list[str]

    @staticmethod
    def from_dict(data: dict) -> FavoriteMarketsResponse:
        return FavoriteMarketsResponse(
            status=data["status"],
            favoriteMarkets=data["favoriteMarkets"],
        )

@dataclass
class GenerateWalletAddressResponse:
    status: str
    address: str

    @staticmethod
    def from_dict(data: dict) -> GenerateWalletAddressResponse:
        return GenerateWalletAddressResponse(
            status=data["status"],
            address=data["address"],
        )

@dataclass
class DepositInfoEntry:
    address: str | None
    tag: str | None

    @staticmethod
    def from_dict(data: dict) -> DepositInfoEntry:
        return DepositInfoEntry(
            address=data.get("address"),
            tag=data.get("tag"),
        )


@dataclass
class Wallet:
    depositAddress: str | None
    depositTag: str | None
    depositInfo: dict[str, DepositInfoEntry]
    id: int
    currency: str
    balance: str
    blockedBalance: str
    activeBalance: str
    rialBalance: int
    rialBalanceSell: int

    @staticmethod
    def from_dict(data: dict) -> Wallet:
        return Wallet(
            depositAddress=data.get("depositAddress"),
            depositTag=data.get("depositTag"),
            depositInfo={
                key: DepositInfoEntry.from_dict(value)
                for key, value in data.get("depositInfo", {}).items()
            },
            id=data["id"],
            currency=data["currency"],
            balance=data["balance"],
            blockedBalance=data["blockedBalance"],
            activeBalance=data["activeBalance"],
            rialBalance=data["rialBalance"],
            rialBalanceSell=data["rialBalanceSell"],
        )


@dataclass
class GetWalletsListResponse:
    status: str
    wallets: list[Wallet]

    @staticmethod
    def from_dict(data: dict) -> GetWalletsListResponse:
        return GetWalletsListResponse(
            status=data["status"],
            wallets=[Wallet.from_dict(w) for w in data["wallets"]],
        )

@dataclass
class WalletEntry:
    id: int
    balance: str
    blocked: str

    @staticmethod
    def from_dict(data: dict) -> WalletEntry:
        return WalletEntry(
            id=data["id"],
            balance=data["balance"],
            blocked=data["blocked"],
        )


@dataclass
class GetWalletsV2Response:
    status: str
    wallets: dict[str, WalletEntry]

    @staticmethod
    def from_dict(data: dict) -> GetWalletsV2Response:
        return GetWalletsV2Response(
            status=data["status"],
            wallets={
                currency: WalletEntry.from_dict(info)
                for currency, info in data["wallets"].items()
            },
        )

@dataclass
class LimitEntry:
    used: str
    limit: str

    @staticmethod
    def from_dict(data: dict) -> LimitEntry:
        return LimitEntry(
            used=data["used"],
            limit=data["limit"],
        )


@dataclass
class Features:
    crypto_trade: bool
    rial_trade: bool
    coin_deposit: bool
    rial_deposit: bool
    coin_withdrawal: bool
    rial_withdrawal: bool

    @staticmethod
    def from_dict(data: dict) -> Features:
        return Features(
            crypto_trade=data["crypto_trade"],
            rial_trade=data["rial_trade"],
            coin_deposit=data["coin_deposit"],
            rial_deposit=data["rial_deposit"],
            coin_withdrawal=data["coin_withdrawal"],
            rial_withdrawal=data["rial_withdrawal"],
        )


@dataclass
class Limits:
    withdrawRialDaily: LimitEntry
    withdrawCoinDaily: LimitEntry
    withdrawTotalDaily: LimitEntry
    withdrawTotalMonthly: LimitEntry

    @staticmethod
    def from_dict(data: dict) -> Limits:
        return Limits(
            withdrawRialDaily=LimitEntry.from_dict(data["withdrawRialDaily"]),
            withdrawCoinDaily=LimitEntry.from_dict(data["withdrawCoinDaily"]),
            withdrawTotalDaily=LimitEntry.from_dict(data["withdrawTotalDaily"]),
            withdrawTotalMonthly=LimitEntry.from_dict(data["withdrawTotalMonthly"]),
        )


@dataclass
class Limitations:
    userLevel: str
    features: Features
    limits: Limits

    @staticmethod
    def from_dict(data: dict) -> Limitations:
        return Limitations(
            userLevel=data["userLevel"],
            features=Features.from_dict(data["features"]),
            limits=Limits.from_dict(data["limits"]),
        )


@dataclass
class LimitationsResponse:
    status: str
    limitations: Limitations

    @staticmethod
    def from_dict(data: dict) -> LimitationsResponse:
        return LimitationsResponse(
            status=data["status"],
            limitations=Limitations.from_dict(data["limitations"]),
        )

@dataclass
class BankCard:
    number: str
    bank: str
    owner: str
    confirmed: bool
    status: str

    @staticmethod
    def from_dict(data: dict) -> BankCard:
        return BankCard(
            number=data["number"],
            bank=data["bank"],
            owner=data["owner"],
            confirmed=data["confirmed"],
            status=data["status"],
        )


@dataclass
class BankAccount:
    id: int
    number: str
    shaba: str
    bank: str
    owner: str
    confirmed: bool
    status: str

    @staticmethod
    def from_dict(data: dict) -> BankAccount:
        return BankAccount(
            id=data["id"],
            number=data["number"],
            shaba=data["shaba"],
            bank=data["bank"],
            owner=data["owner"],
            confirmed=data["confirmed"],
            status=data["status"],
        )


@dataclass
class Verifications:
    email: bool
    phone: bool
    mobile: bool
    identity: bool
    selfie: bool
    bankAccount: bool
    bankCard: bool
    address: bool
    city: bool
    nationalSerialNumber: bool

    @staticmethod
    def from_dict(data: dict) -> "Verifications":
        return Verifications(
            email=data["email"],
            phone=data["phone"],
            mobile=data["mobile"],
            identity=data["identity"],
            selfie=data["selfie"],
            bankAccount=data["bankAccount"],
            bankCard=data["bankCard"],
            address=data["address"],
            city=data["city"],
            nationalSerialNumber=data["nationalSerialNumber"],
        )


@dataclass
class PendingVerifications:
    email: bool
    phone: bool
    mobile: bool
    identity: bool
    selfie: bool
    bankAccount: bool
    bankCard: bool

    @staticmethod
    def from_dict(data: dict) -> PendingVerifications:
        return PendingVerifications(
            email=data["email"],
            phone=data["phone"],
            mobile=data["mobile"],
            identity=data["identity"],
            selfie=data["selfie"],
            bankAccount=data["bankAccount"],
            bankCard=data["bankCard"],
        )


@dataclass
class Options:
    fee: str
    feeUsdt: str
    isManualFee: bool
    tfa: bool
    socialLoginEnabled: bool

    @staticmethod
    def from_dict(data: dict) -> Options:
        return Options(
            fee=data["fee"],
            feeUsdt=data["feeUsdt"],
            isManualFee=data["isManualFee"],
            tfa=data["tfa"],
            socialLoginEnabled=data["socialLoginEnabled"],
        )


@dataclass
class Profile:
    firstName: str
    lastName: str
    nationalCode: str
    email: str
    username: str
    phone: str
    mobile: str
    city: str
    bankCards: list[BankCard]
    bankAccounts: list[BankAccount]
    verifications: Verifications
    pendingVerifications: PendingVerifications
    options: Options
    withdrawEligible: bool

    @staticmethod
    def from_dict(data: dict) -> Profile:
        return Profile(
            firstName=data["firstName"],
            lastName=data["lastName"],
            nationalCode=data["nationalCode"],
            email=data["email"],
            username=data["username"],
            phone=data["phone"],
            mobile=data["mobile"],
            city=data["city"],
            bankCards=[BankCard.from_dict(x) for x in data["bankCards"]],
            bankAccounts=[BankAccount.from_dict(x) for x in data["bankAccounts"]],
            verifications=Verifications.from_dict(data["verifications"]),
            pendingVerifications=PendingVerifications.from_dict(data["pendingVerifications"]),
            options=Options.from_dict(data["options"]),
            withdrawEligible=data["withdrawEligible"],
        )

@dataclass
class TradeStats:
    monthTradesTotal: str
    monthTradesCount: int

    @staticmethod
    def from_dict(data: dict) -> TradeStats:
        return TradeStats(
            monthTradesTotal=data["monthTradesTotal"],
            monthTradesCount=data["monthTradesCount"],
        )

@dataclass
class GetProfileResponse:
    status: str
    profile: Profile
    tradeStats: TradeStats
    websocketAuthParam: str

    @staticmethod
    def from_dict(data: dict) -> GetProfileResponse:
        return GetProfileResponse(
            status=data["status"],
            profile=Profile.from_dict(data["profile"]),
            tradeStats=TradeStats.from_dict(data["tradeStats"]),
            websocketAuthParam=data["we_id"],
        )

@dataclass
class MarketStat:
    isClosed: bool
    bestSell: str
    bestBuy: str
    volumeSrc: str
    volumeDst: str
    latest: str
    mark: str
    dayLow: str
    dayHigh: str
    dayOpen: str
    dayClose: str
    dayChange: str


@dataclass
class StatsResponse:
    status: str
    stats: dict[str, MarketStat]

    @staticmethod
    def from_dict(data: dict) -> StatsResponse:
        stats = {
            symbol: MarketStat(**values)
            for symbol, values in data["stats"].items()
        }

        return StatsResponse(
            status=data["status"],
            stats=stats
        )

@dataclass
class Trade:
    time: int
    price: str
    volume: str
    type: str


@dataclass
class TradesResponse:
    status: str
    trades: list[Trade]

    @staticmethod
    def from_dict(data: dict) -> TradesResponse:
        return TradesResponse(
            status=data["status"],
            trades=[
                Trade(
                    time=item["time"],
                    price=item["price"],
                    volume=item["volume"],
                    type=item["type"],
                )
                for item in data["trades"]
            ],
        )

@dataclass
class HistoryTransaction:
    id: int
    amount: str
    description: str
    created_at: str
    balance: str
    tp: str
    calculatedFee: str | None
    type: str
    currency: str

    @staticmethod
    def from_dict(data: dict) -> "HistoryTransaction":
        return HistoryTransaction(
            id=data["id"],
            amount=data["amount"],
            description=data["description"],
            created_at=data["created_at"],
            balance=data["balance"],
            tp=data["tp"],
            calculatedFee=data.get("calculatedFee"),
            type=data["type"],
            currency=data["currency"],
        )


@dataclass
class TransactionsHistoryResponse:
    status: str
    transactions: list[HistoryTransaction]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict) -> "TransactionsHistoryResponse":
        return TransactionsHistoryResponse(
            status=data["status"],
            transactions=[HistoryTransaction.from_dict(t) for t in data["transactions"]],
            hasNext=data["hasNext"],
        )

@dataclass
class DepositTransaction:
    id: int
    amount: str
    currency: str
    description: str
    created_at: str
    calculatedFee: str

    @staticmethod
    def from_dict(data: dict) -> DepositTransaction:
        return DepositTransaction(
            id=data["id"],
            amount=data["amount"],
            currency=data["currency"],
            description=data["description"],
            created_at=data["created_at"],
            calculatedFee=data["calculatedFee"],
        )


@dataclass
class Deposit:
    txHash: str
    address: str
    confirmed: bool
    transaction: DepositTransaction
    currency: str
    blockchainUrl: str
    confirmations: int
    requiredConfirmations: int
    amount: str

    @staticmethod
    def from_dict(data: dict) -> Deposit:
        return Deposit(
            txHash=data["txHash"],
            address=data["address"],
            confirmed=data["confirmed"],
            transaction=DepositTransaction.from_dict(data["transaction"]),
            currency=data["currency"],
            blockchainUrl=data["blockchainUrl"],
            confirmations=data["confirmations"],
            requiredConfirmations=data["requiredConfirmations"],
            amount=data["amount"],
        )


@dataclass
class WalletDepositsResponse:
    status: str
    deposits: list[Deposit]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict) -> WalletDepositsResponse:
        return WalletDepositsResponse(
            status=data["status"],
            deposits=[Deposit.from_dict(d) for d in data["deposits"]],
            hasNext=data["hasNext"],
        )

@dataclass
class Transaction:
    currency: str
    created_at: str
    calculatedFee: str
    id: int
    amount: str
    description: str

    @staticmethod
    def from_dict(data: dict) -> "Transaction":
        return Transaction(
            currency=data["currency"],
            created_at=data["created_at"],
            calculatedFee=data["calculatedFee"],
            id=data["id"],
            amount=data["amount"],
            description=data["description"],
        )


@dataclass
class WalletTransactionsResponse:
    status: str
    transactions: list[Transaction]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict) -> "WalletTransactionsResponse":
        return WalletTransactionsResponse(
            status=data["status"],
            transactions=[Transaction.from_dict(t) for t in data["transactions"]],
            hasNext=data["hasNext"],
        )
