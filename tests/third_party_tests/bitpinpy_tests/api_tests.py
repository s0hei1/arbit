import pytest
from third_party.bitpinpy.api_client import APIClient
from fixtures import client
from random import choice

from third_party.bitpinpy.models.market_info import GetNetworksRequest, GetCurrencyNetworksRequest


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
    any_network = choice(response)

    assert any_network.id
    assert isinstance(response, list)

def test_get_currency_networks(client : APIClient):
    response = client.get_currency_networks(
        GetCurrencyNetworksRequest(
            currency_code = 'BTC'
        )
    )
    any_network = choice(response)

    assert any_network.network
    assert isinstance(response, list)


def test_get_tickers(client : APIClient):
    response = client.get_tickers()
    any_ticker = choice(response)

    assert any_ticker.symbol
    assert isinstance(response, list)

def test_get_order_book(client : APIClient):
    response = client.get_order_book(symbol_name = 'BTC_USDT')

    assert isinstance(response.asks, list)

def test_get_matches(client : APIClient):
    response = client.get_matches(symbol_name = 'BTC_USDT')
    any_match = choice(response)
    assert any_match.side
    assert isinstance(response, list)

def test_get_commissions(client : APIClient):
    response = client.get_commissions()
    any_commission = choice(response)
    assert any_commission.maker
    assert isinstance(response, list)



