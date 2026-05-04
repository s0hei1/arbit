import pytest

from third_party.bitpinpy.api_client._api_client import APIClient
from third_party.bitpinpy.api_client._bitpin_client_factory import bitpin_client_factory
from third_party.httpx_overhead import request_logger, response_logger


@pytest.fixture
def client() -> APIClient:
    return APIClient(
        client=bitpin_client_factory(
            request_event_hooks=[request_logger(show_url=True, show_body=True)],
            response_event_hooks=[response_logger()]
        ),
    )



