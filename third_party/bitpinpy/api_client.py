from typing import Any, Callable
from httpx import Client, HTTPTransport, Response, Request

from src_bitpinpy.models.auth import AuthenticateRequest, AuthenticateResponse
from src_bitpinpy.models.market_info import CurrencyResponse, MarketResponse
from src_bitpinpy.models.static_models.route import Routes


class ResponseHandler(HTTPTransport):

    def handle_request(self, request: Request):
        response = super().handle_request(request)

        return response


def url_printer_event_hook(request: Request):
    print("")
    print(f"REQUEST.{request.method} {request.url}")


def response_status_code_printer_event_hook(response: Response):
    print()
    print(f"RESPONSE {response.url} STATUS CODE {response.status_code}")
    print(f"Response: {response.read()}")


def bitpin_client_factory(
        base_url: str = 'https://api.bitpin.org',
        token: str | None = None,
        user_agent: str | None = None,
        request_event_hooks: list[Callable[..., Any]] | None = None,
        response_event_hooks: list[Callable[..., Any]] | None = None,
) -> Client:
    _client = Client(
        base_url=base_url,
        timeout=60,
        transport=ResponseHandler(),
        event_hooks={
            "request": request_event_hooks if request_event_hooks is not None else [],
            "response": response_event_hooks if response_event_hooks is not None else [],
        },
    )

    if token is not None:
        _client.headers["Authorization"] = f"Token {token}"

    if user_agent is not None:
        _client.headers["User-Agent"] = f'TraderBot/{user_agent}'

    return _client


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

print("https://api.bitpin.org/api/v1/usr/authenticate/" == "https://api.bitpin.org/api/v1/usr/authenticate/")

print(APIClient(
    client=bitpin_client_factory(
        request_event_hooks=[url_printer_event_hook],
        response_event_hooks=[response_status_code_printer_event_hook],
    )
).authenticate(
AuthenticateRequest(
    api_key="Test",
    secret_key="Test"
)
))

