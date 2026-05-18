from httpx import Client, AsyncClient
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

class AsyncAPIClient:

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_order_book(self, symbol_name: str) -> GetOrderBookResponse:
        url = Routes.get_order_book.url_with_path_parameter(symbol_name)
        response = await self.client.get(
            url=url
        )
        return GetOrderBookResponse.from_dict(response.json())

    async def get_order_book_all(self) -> GetOrderBookAllResponse:
        url = Routes.get_order_book_all.url
        response = await self.client.get(
            url=url
        )
        return GetOrderBookAllResponse.from_dict(response.json())

    async def get_depth(self, symbol_name: str) -> GetDepthResponse:
        url = Routes.get_depth.url_with_path_parameter(symbol_name)
        response = await self.client.get(
            url=url
        )
        return GetDepthResponse.from_dict(response.json())

    async def get_trades(self, symbol_name: str) -> TradesResponse:
        url = Routes.get_trades.url_with_path_parameter(symbol_name)
        response = await self.client.get(
            url=url
        )
        return TradesResponse.from_dict(response.json())

    async def get_stats(self, request: GetStatsRequest) -> StatsResponse:
        response = await self.client.get(
            url=Routes.get_stats.url,
            params=request.to_dict()
        )
        return StatsResponse.from_dict(response.json())

    async def get_market_history(self, payload: GetMarketHistoryRequest) -> MarketHistoryResponse:
        response = await self.client.get(Routes.get_market_history.url, params=payload.to_dict())
        return MarketHistoryResponse.from_dict(response.json())

    async def get_user_profile(self) -> GetProfileResponse:
        response = await self.client.get(Routes.get_user_profile.url)
        return GetProfileResponse.from_dict(response.json())

    async def post_generate_wallet_address(self, payload: GenerateWalletAddressRequest) -> GenerateWalletAddressResponse:
        response = await self.client.post(Routes.generate_wallet_address.url, data=payload.to_dict())
        return GenerateWalletAddressResponse.from_dict(response.json())

    async def post_add_bank_card(self, payload: AddBankCardRequest) -> OkResponse:
        response = await self.client.post(Routes.add_user_bank_card.url, data=payload.to_dict())
        return OkResponse.from_dict(response.json())

    async def post_add_bank_account(self, payload: AddBankAccountRequest) -> OkResponse:
        response = await self.client.post(Routes.add_user_bank_account.url, data=payload.to_dict())
        return OkResponse.from_dict(response.json())

    async def get_user_limitations(self) -> LimitationsResponse:
        response = await self.client.get(Routes.get_user_limitations.url)
        return LimitationsResponse.from_dict(response.json())

    async def get_user_wallets(self) -> GetWalletsListResponse:
        response = await self.client.get(Routes.get_user_wallets_list.url)
        return GetWalletsListResponse.from_dict(response.json())

    async def get_user_wallets_by_filtering(self, payload: GetUserWalletsByFilteringResponse) -> GetWalletsV2Response:
        response = await self.client.get(Routes.get_user_wallets_by_filtering.url, params=payload.to_dict())
        return GetWalletsV2Response.from_dict(response.json())

    async def get_balance(self, payload: GetBalanceRequest) -> BalanceResponse:
        response = await self.client.post(Routes.get_balance.url, data=payload.to_dict())
        return BalanceResponse.from_dict(response.json())

    async def get_wallet_transactions(self, payload: GetWalletTransactionsRequest) -> WalletTransactionsResponse:
        response = await self.client.get(Routes.get_user_wallet_transactions.url, params=payload.to_dict())
        return WalletTransactionsResponse.from_dict(response.json())

    async def get_transaction_history(self, payload: GetTransactionsHistoryRequest) -> TransactionsHistoryResponse:
        response = await self.client.get(Routes.get_user_transactions_history.url, params=payload.to_dict())
        return TransactionsHistoryResponse.from_dict(response.json())

    async def get_deposits(self, payload: GetDepositsRequest) -> WalletDepositsResponse:
        response = await self.client.get(Routes.get_user_wallet_deposits.url, params=payload.to_dict())
        return WalletDepositsResponse.from_dict(response.json())

    async def get_favorite_markets(self) -> FavoriteMarketsResponse:
        response = await self.client.get(Routes.get_user_favorite_markets.url)
        return FavoriteMarketsResponse.from_dict(response.json())

    async def add_favorite_markets(self, payload: AddFavoriteMarketsRequest) -> FavoriteMarketsResponse:
        response = await self.client.post(Routes.post_user_favorite_markets.url, data=payload.to_dict())
        return FavoriteMarketsResponse.from_dict(response.json())

    async def add_order(self, payload: AddOrderRequest) -> AddOrderResponse:
        print(payload.to_dict())
        response = await self.client.post(Routes.add_order.url, data=payload.to_dict())

        return AddOrderResponse.from_dict(response.json())

    async def get_order_status(self, payload: GetOrderStatusRequest) -> GetOrderStatusResponse:
        response = await self.client.post(
            Routes.get_order_status.url,
            data=payload.to_dict()
        )
        return GetOrderStatusResponse.from_dict(response.json())

    async def get_spot_orders(self, payload: GetSpotOrdersRequest) -> GetOrdersResponse:
        response = await self.client.get(
            Routes.get_spot_orders.url,
            params=payload.to_dict()
        )
        return GetOrdersResponse.from_dict(response.json())

    async def update_order(self, payload: UpdateOrderStatusRequest) -> UpdateOrderStatusResponse:
        response = await self.client.post(
            Routes.update_order_status.url,
            data=payload.to_dict()
        )
        return UpdateOrderStatusResponse.from_dict(response.json())

    async def cancel_orders(self, payload: CancelOrdersRequest) -> OkResponse:
        response = await self.client.post(
            Routes.cancel_orders.url,
            data=payload.to_dict()
        )
        return OkResponse.from_dict(response.json())

    async def get_spot_traded(self, payload: GetTradesRequest) -> SpotTradesResponse:
        response = await self.client.get(
            Routes.get_spot_trades.url,
            params=payload.to_dict()
        )
        return SpotTradesResponse.from_dict(response.json())

    async def withdraw_request(self, payload: WithdrawRequest) -> WithdrawResponse:
        raise NotTestedError("This Method is not Tested")
        response = await self.client.post(
            Routes.withdraw_request.url,
            data=payload.to_dict()
        )
        return WithdrawResponse.from_dict(response.json())

    async def withdraw_request_confirm(self, payload: WithdrawConfirmRequest) -> WithdrawResponse:
        raise NotTestedError("This Method is not Tested")
        response = await self.client.post(
            Routes.withdraw_request_confirm.url,
            data=payload.to_dict()
        )
        return WithdrawResponse.from_dict(response.json())

    async def get_withdraw(self, withdraw: int) -> WithdrawResponse:
        raise NotTestedError("This Method is not Tested")
        response = await self.client.get(
            Routes.get_withdraw_details.url_with_path_parameter(str(withdraw))
        )
        return WithdrawResponse.from_dict(response.json())

    async def get_withdraws(self) -> WithdrawsResponse:
        response = await self.client.get(
            Routes.get_withdraws.url
        )
        return WithdrawsResponse.from_dict(response.json())

    async def get_web_socket_token(self):
        pass
