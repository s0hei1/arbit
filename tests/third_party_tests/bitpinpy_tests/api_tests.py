import pytest
from third_party.bitpinpy.api_client import APIClient
from fixtures import client
from random import choice

from third_party.bitpinpy.models.market_info import GetNetworksRequest


def test_get_markets(client : APIClient):
    response = client.get_markets()
    any_market = choice(response)

    assert any_market.symbol
    assert isinstance(response, list)

def test_get_currencies(client : APIClient):
    response = client.get_currencies()
    any_currency = choice(response)

    assert any_currency.currency
    assert isinstance(response, list)


def test_get_networks(client : APIClient):
    response = client.get_networks(
        GetNetworksRequest()
    )
    any_currency = choice(response)

    assert any_currency.id
    assert isinstance(response, list)



