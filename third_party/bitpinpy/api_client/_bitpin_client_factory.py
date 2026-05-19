from typing import Any, Callable
from httpx import Client, AsyncClient
from third_party.httpx_overhead._http_transports import ResponseHandler


def bitpin_client_factory(
        base_url: str = 'https://api.bitpin.ir',
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

    return _client

def bitpin_async_client_factory(
        base_url: str = 'https://api.bitpin.ir',
        request_event_hooks: list[Callable[..., Any]] | None = None,
        response_event_hooks: list[Callable[..., Any]] | None = None,
) -> AsyncClient:
    _client = AsyncClient(
        base_url=base_url,
        timeout=60,
        event_hooks={
            "request": request_event_hooks if request_event_hooks is not None else [],
            "response": response_event_hooks if response_event_hooks is not None else [],
        },
    )

    return _client
