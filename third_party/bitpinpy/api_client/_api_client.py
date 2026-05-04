from httpx import Client
from third_party.bitpinpy.models.auth import AuthenticateRequest, AuthenticateResponse
from third_party.bitpinpy.models.market_info import CurrencyResponse, MarketResponse, NetworkResponse, \
    GetNetworksRequest
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

