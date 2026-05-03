import pytest
from random import choice, random
from third_party.nobipy.api_client import nobitex_client_factory, APIClient, url_printer_event_hook, \
    response_status_code_printer_event_hook
from third_party.nobipy.models.static_models import Resolutions
from third_party.nobipy.models.static_models.resolution import Resolution
from third_party.nobipy.my_token import TOKEN


@pytest.fixture
def client() -> APIClient:
    return APIClient(
        client=nobitex_client_factory(
            token=TOKEN,
            request_event_hooks=[url_printer_event_hook],
            response_event_hooks=[response_status_code_printer_event_hook]
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




