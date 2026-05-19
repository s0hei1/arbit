from typing import Callable, Any
from httpx import Client, AsyncClient

from third_party.httpx_overhead._http_transports import ResponseHandler


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

    if token is not None:
        _client.headers["Authorization"] = f"Token {token}"

    if user_agent is not None:
        _client.headers["User-Agent"] = f'TraderBot/{user_agent}'

    return _client

def nobitex_async_client_factory(
        base_url: str = 'https://apiv2.nobitex.ir',
        token: str | None = None,
        user_agent: str | None = None,
        request_event_hooks: list[Callable[..., Any]] | None = None,
        response_event_hooks: list[Callable[..., Any]] | None = None,
) -> AsyncClient:
    _client = AsyncClient(
        base_url=base_url,
        timeout=10,
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

