from httpx import Client
from third_party.bitpinpy.models.auth import AuthenticateRequest, AuthenticateResponse
from third_party.bitpinpy.models.market_info import CurrencyResponse, MarketResponse, NetworkResponse, \
    GetNetworksRequest, CurrencyNetworkResponse, GetCurrencyNetworksRequest, TickersResponse, OrderBookResponse, \
    MatchResponse, CommissionsResponse
from third_party.bitpinpy.models.static_models.route import Routes

class APIClient:

    def __init__(self, client: Client) -> None:
        self.client = client


    def authenticate(self, payload : AuthenticateRequest) -> AuthenticateResponse:
        response = self.client.post(
            url = Routes.authenticate.url,
            data=payload.to_dict(),
        )
        return AuthenticateResponse.from_dict(response.json())

    def get_currencies(self) -> list[CurrencyResponse]:
        response = self.client.get(
            url = Routes.get_currencies.url
        )
        return [CurrencyResponse.from_dict(i) for i in response.json()]

    def get_markets(self) -> list[MarketResponse]:
        response = self.client.get(
            url = Routes.get_markets.url
        )
        return [MarketResponse.from_dict(i) for i in response.json()]

    def get_networks(self, payload : GetNetworksRequest) -> list[NetworkResponse]:
        response = self.client.get(
            url = Routes.get_networks.url,
            params=payload.to_dict(),
        )
        return [NetworkResponse.from_dict(i) for i in response.json()]

    def get_currency_networks(self, payload : GetCurrencyNetworksRequest) -> list[CurrencyNetworkResponse]:
        # TODO : Not Tested
        response = self.client.get(
            url = Routes.get_currency_networks.url,
            params=payload.to_dict(),
        )
        return [CurrencyNetworkResponse.from_dict(i) for i in response.json()]

    def get_tickers(self) -> list[TickersResponse]:
        response = self.client.get(
            url = Routes.get_tickers.url,
        )
        return [TickersResponse.from_dict(i) for i in response.json()]

    def get_order_book(self, symbol_name : str) -> OrderBookResponse:
        response = self.client.get(
            url = Routes.get_order_book.url_with_path_parameter(f'{symbol_name}/'),
        )
        return OrderBookResponse.from_dict(response.json())

    def get_matches(self, symbol_name : str) -> list[MatchResponse]:
        response = self.client.get(
            url = Routes.get_matches.url_with_path_parameter(f'{symbol_name}/'),
        )
        return [MatchResponse.from_dict(i) for i in response.json()]

    get_last_trades = get_matches

    def get_commissions(self) -> list[CommissionsResponse]:
        response = self.client.get(
            url = Routes.get_commissions.url,
        )
        return [CommissionsResponse.from_dict(i) for i in response.json()]
