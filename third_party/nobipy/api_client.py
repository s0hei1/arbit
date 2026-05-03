from typing import Any, Callable
from httpx import Client, HTTPTransport, Response, Request
from third_party.nobipy.models.exceptions import NotTestedError
from third_party.nobipy.models import GetMarketHistoryRequest, GetStatsRequest, AddBankCardRequest, \
    GenerateWalletAddressRequest, AddBankAccountRequest, GetUserWalletsByFilteringResponse, GetBalanceRequest, \
    GetTransactionsHistoryRequest, GetOrderStatusRequest, GetSpotOrdersRequest, UpdateOrderStatusRequest, \
    AddFavoriteMarketsRequest, AddOrderRequest, GetDepositsRequest, GetTradesRequest, GetWalletTransactionsRequest, \
    CancelOrdersRequest, GetOrderBookResponse, GetOrderBookAllResponse, GetDepthResponse, \
    TradesResponse, StatsResponse, MarketHistoryResponse, GetProfileResponse, GenerateWalletAddressResponse, OkResponse, \
    LimitationsResponse, GetWalletsListResponse, GetWalletsV2Response, BalanceResponse, WalletTransactionsResponse, \
    AddOrderResponse, GetOrdersResponse, SpotTradesResponse, UpdateOrderStatusResponse, TransactionsHistoryResponse, \
    WalletDepositsResponse, FavoriteMarketsResponse, GetOrderStatusResponse,WithdrawRequest, WithdrawResponse, WithdrawConfirmRequest, WithdrawsResponse

from third_party.nobipy.models.static_models import Routes



class ResponseHandler(HTTPTransport):

    def handle_request(self, request: Request):
        response = super().handle_request(request)

        return response


def url_printer_event_hook(request: Request):
    print()
    print(f"REQUEST.{request.method} {request.url}")


def response_status_code_printer_event_hook(response: Response):
    print()
    print(f"RESPONSE {response.url} STATUS CODE {response.status_code}")
    print(f"Response: {response.read()}")


def nobitex_client_factory(
        base_url: str = 'https://apiv2.nobitex.ir',
        token: str | None = None,
        user_agent: str | None = None,
        request_event_hooks: list[Callable[..., Any]] | None = None,
        response_event_hooks: list[Callable[..., Any]] | None = None,
) -> Client:
    _client = Client(
        base_url=base_url,
        timeout=10,
        transport=ResponseHandler(),
        event_hooks={
            "request": request_event_hooks if request_event_hooks is not None else [],
            "response": response_event_hooks if response_event_hooks is not None else [],
        },
    )

    # _client.headers["content-type"] = 'application/json'

    if token is not None:
        _client.headers["Authorization"] = f"Token {token}"

    if user_agent is not None:
        _client.headers["User-Agent"] = f'TraderBot/{user_agent}'

    return _client


class APIClient:

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_order_book(self, symbol_name: str) -> GetOrderBookResponse:
        url = Routes.get_order_book.url_with_path_parameter(symbol_name)
        response = self.client.get(
            url=url
        )
        return GetOrderBookResponse.from_dict(response.json())

    def get_order_book_all(self) -> GetOrderBookAllResponse:
        url = Routes.get_order_book_all.url
        response = self.client.get(
            url=url
        )
        return GetOrderBookAllResponse.from_dict(response.json())

    def get_depth(self, symbol_name: str) -> GetDepthResponse:
        url = Routes.get_depth.url_with_path_parameter(symbol_name)
        response = self.client.get(
            url=url
        )
        return GetDepthResponse.from_dict(response.json())

    def get_trades(self, symbol_name: str) -> TradesResponse:
        url = Routes.get_trades.url_with_path_parameter(symbol_name)
        response = self.client.get(
            url=url
        )
        return TradesResponse.from_dict(response.json())

    def get_stats(self, request: GetStatsRequest) -> StatsResponse:
        response = self.client.get(
            url=Routes.get_stats.url,
            params=request.to_dict()
        )
        return StatsResponse.from_dict(response.json())

    def get_market_history(self, payload: GetMarketHistoryRequest) -> MarketHistoryResponse:
        response = self.client.get(Routes.get_market_history.url, params=payload.to_dict())
        return MarketHistoryResponse.from_dict(response.json())

    def get_user_profile(self) -> GetProfileResponse:
        response = self.client.get(Routes.get_user_profile.url)
        return GetProfileResponse.from_dict(response.json())

    def post_generate_wallet_address(self, payload: GenerateWalletAddressRequest) -> GenerateWalletAddressResponse:
        response = self.client.post(Routes.generate_wallet_address.url, data=payload.to_dict())
        return GenerateWalletAddressResponse.from_dict(response.json())

    def post_add_bank_card(self, payload: AddBankCardRequest) -> OkResponse:
        response = self.client.post(Routes.add_user_bank_card.url, data=payload.to_dict())
        return OkResponse.from_dict(response.json())

    def post_add_bank_account(self, payload: AddBankAccountRequest) -> OkResponse:
        response = self.client.post(Routes.add_user_bank_account.url, data=payload.to_dict())
        return OkResponse.from_dict(response.json())

    def get_user_limitations(self) -> LimitationsResponse:
        response = self.client.get(Routes.get_user_limitations.url)
        return LimitationsResponse.from_dict(response.json())

    def get_user_wallets(self) -> GetWalletsListResponse:
        response = self.client.get(Routes.get_user_wallets_list.url)
        return GetWalletsListResponse.from_dict(response.json())

    def get_user_wallets_by_filtering(self, payload: GetUserWalletsByFilteringResponse) -> GetWalletsV2Response:
        response = self.client.get(Routes.get_user_wallets_by_filtering.url, params=payload.to_dict())
        return GetWalletsV2Response.from_dict(response.json())

    def get_balance(self, payload: GetBalanceRequest) -> BalanceResponse:
        response = self.client.post(Routes.get_balance.url, data=payload.to_dict())
        return BalanceResponse.from_dict(response.json())

    def get_wallet_transactions(self, payload: GetWalletTransactionsRequest) -> WalletTransactionsResponse:
        response = self.client.get(Routes.get_user_wallet_transactions.url, params=payload.to_dict())
        return WalletTransactionsResponse.from_dict(response.json())

    def get_transaction_history(self, payload: GetTransactionsHistoryRequest) -> TransactionsHistoryResponse:
        response = self.client.get(Routes.get_user_transactions_history.url, params=payload.to_dict())
        return TransactionsHistoryResponse.from_dict(response.json())

    def get_deposits(self, payload: GetDepositsRequest) -> WalletDepositsResponse:
        response = self.client.get(Routes.get_user_wallet_deposits.url, params=payload.to_dict())
        return WalletDepositsResponse.from_dict(response.json())

    def get_favorite_markets(self) -> FavoriteMarketsResponse:
        response = self.client.get(Routes.get_user_favorite_markets.url)
        return FavoriteMarketsResponse.from_dict(response.json())

    def add_favorite_markets(self, payload: AddFavoriteMarketsRequest) -> FavoriteMarketsResponse:
        response = self.client.post(Routes.post_user_favorite_markets.url, data=payload.to_dict())
        return FavoriteMarketsResponse.from_dict(response.json())

    def add_order(self, payload: AddOrderRequest) -> AddOrderResponse:
        print(payload.to_dict())
        response = self.client.post(Routes.add_order.url, data=payload.to_dict())

        return AddOrderResponse.from_dict(response.json())

    def get_order_status(self, payload: GetOrderStatusRequest) -> GetOrderStatusResponse:
        response = self.client.post(
            Routes.get_order_status.url,
            data=payload.to_dict()
        )
        return GetOrderStatusResponse.from_dict(response.json())

    def get_spot_orders(self, payload: GetSpotOrdersRequest) -> GetOrdersResponse:
        response = self.client.get(
            Routes.get_spot_orders.url,
            params=payload.to_dict()
        )
        return GetOrdersResponse.from_dict(response.json())

    def update_order(self, payload: UpdateOrderStatusRequest) -> UpdateOrderStatusResponse:
        response = self.client.post(
            Routes.update_order_status.url,
            data=payload.to_dict()
        )
        return UpdateOrderStatusResponse.from_dict(response.json())

    def cancel_orders(self, payload: CancelOrdersRequest) -> OkResponse:
        response = self.client.post(
            Routes.cancel_orders.url,
            data=payload.to_dict()
        )
        return OkResponse.from_dict(response.json())

    def get_spot_traded(self, payload: GetTradesRequest) -> SpotTradesResponse:
        response = self.client.get(
            Routes.get_spot_trades.url,
            params=payload.to_dict()
        )
        return SpotTradesResponse.from_dict(response.json())

    def withdraw_request(self, payload: WithdrawRequest) -> WithdrawResponse:
        raise NotTestedError("This Method is not Tested")
        response = self.client.post(
            Routes.withdraw_request.url,
            data=payload.to_dict()
        )
        return WithdrawResponse.from_dict(response.json())

    def withdraw_request_confirm(self, payload: WithdrawConfirmRequest) -> WithdrawResponse:
        raise NotTestedError("This Method is not Tested")
        response = self.client.post(
            Routes.withdraw_request_confirm.url,
            data=payload.to_dict()
        )
        return WithdrawResponse.from_dict(response.json())

    def get_withdraw(self, withdraw: int) -> WithdrawResponse:
        raise NotTestedError("This Method is not Tested")
        response = self.client.get(
            Routes.get_withdraw_details.url_with_path_parameter(str(withdraw))
        )
        return WithdrawResponse.from_dict(response.json())

    def get_withdraws(self) -> WithdrawsResponse:
        response = self.client.get(
            Routes.get_withdraws.url
        )
        return WithdrawsResponse.from_dict(response.json())

    def get_web_socket_token(self):
        pass
