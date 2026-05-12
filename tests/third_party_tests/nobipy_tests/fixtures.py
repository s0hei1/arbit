import pytest
from random import choice, random
from third_party.nobipy.api_client import nobitex_client_factory, APIClient
from third_party.httpx_overhead import request_logger, response_logger
from third_party.nobipy.models.static_models import Resolutions
from third_party.nobipy.models.static_models.resolution import Resolution



@pytest.fixture
def client() -> APIClient:
    return APIClient(
        client=nobitex_client_factory(
            token='TOKEN',
            request_event_hooks=[request_logger()],
            response_event_hooks=[response_logger()]
        ),

    )

@pytest.fixture
def get_symbols() -> list[str]:
    return [
        "BTCIRT",
        "BTCUSDT",
        "ETHUSDT",
        "USDTIRT",
    ]


@pytest.fixture
def any_symbol(get_symbols : list[str]) -> str:
    return choice(get_symbols)

@pytest.fixture
def any_resolution() -> Resolution:
    return choice(Resolutions.get_all())




