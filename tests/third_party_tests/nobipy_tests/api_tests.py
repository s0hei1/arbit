import pytest
from httpx import Client
from third_party.nobipy.api_client import APIClient
from third_party.nobipy.models import GetStatsRequest, GetMarketHistoryRequest, GetUserWalletsByFilteringResponse, \
    GetBalanceRequest, GetTransactionsHistoryRequest, GetOrderStatusRequest, GetSpotOrdersRequest, \
    UpdateOrderStatusRequest, CancelOrdersRequest
from third_party.nobipy.models import AddFavoriteMarketsRequest
from third_party.nobipy.models import AddOrderRequest
from third_party.nobipy.models import GenerateWalletAddressRequest
from third_party.nobipy.models import GetDepositsRequest
from third_party.nobipy.models import GetTradesRequest
from third_party.nobipy.models import GetWalletTransactionsRequest
from third_party.nobipy.models.static_models import Resolutions
from fixtures import client,get_symbols,any_symbol
import datetime as dt

def test_get_order_book(client : APIClient, any_symbol : str):
    response = client.get_order_book(any_symbol)
    assert response.status == 'ok'

def test_get_order_book_all(client : APIClient,):
    response = client.get_order_book_all()
    assert response.status == 'ok'

def test_get_depth(client : APIClient, any_symbol : str):
    response = client.get_depth(any_symbol)
    assert response.status == 'ok'

def test_get_trades(client : APIClient, any_symbol : str):
    response = client.get_trades(any_symbol)
    assert response.status == 'ok'

def test_get_stats(client : APIClient, any_symbol : str):
    response = client.get_stats(
        GetStatsRequest(
            srcCurrency=['usdt'],
            dstCurrency=['rls'],
        )
    )
    assert response.status == 'ok'

def test_get_market_history(client : APIClient, any_symbol : str):
    response = client.get_market_history(
        GetMarketHistoryRequest(
            symbol = any_symbol,
            resolution = Resolutions.D1.value,
            to = int(dt.datetime.now(dt.UTC).timestamp()),
            page = 1,
            countback=50
        )
    )
    assert response.s == 'ok'

def test_get_profile(client : APIClient):
    response = client.get_user_profile()
    assert response.status == 'ok'

def test_generate_wallet_address(client : APIClient):
    response = client.post_generate_wallet_address(GenerateWalletAddressRequest(
        currency= "btc",
        wallet_id=None,
        network="BSC",
    ))
    assert response.status == 'ok'

def test_get_user_limitations(client : APIClient):
    response = client.get_user_limitations()
    assert response.status == 'ok'

def test_user_wallets_list(client : APIClient):
    response = client.get_user_wallets()
    assert response.status == 'ok'

def test_get_user_wallets_by_filtering(client : APIClient):
    response = client.get_user_wallets_by_filtering(
        GetUserWalletsByFilteringResponse(
            currencies=['btc']
        )
    )
    assert response.status == 'ok'

def test_get_balance(client : APIClient, any_symbol : str):
    response = client.get_balance(
        GetBalanceRequest(
            currency='btc'
        )
    )
    assert response.status == 'ok'

def test_get_wallet_transactions(client : APIClient):
    response = client.get_wallet_transactions(
        GetWalletTransactionsRequest(
            wallet_id=4159
        )
    )
    assert response.status == 'ok'

def test_get_transaction_history(client : APIClient):
    response = client.get_transaction_history(
        GetTransactionsHistoryRequest(
            currency='rls'
        )
    )
    print(response)
    assert response.status == 'ok'

def test_get_favorite_markets(client : APIClient):
    response = client.get_favorite_markets()
    assert response.status == 'ok'

def test_add_favorite_markets(client : APIClient):
    response = client.add_favorite_markets(
        AddFavoriteMarketsRequest(
            market=['BNBUSDT']
        )
    )
    assert response.status == 'ok'

def test_add_order(client : APIClient):
    response = client.add_order(
        AddOrderRequest(
            type = 'sell',
            srcCurrency = 'ton',
            dstCurrency = 'usdt',
            amount = 10.0,
            price = 3,
            execution = 'limit',
            clientOrderId = "TEST2",
        )
    )
    assert response.status == 'ok'

def test_get_order_status(client: APIClient):
    response = client.get_order_status(
        GetOrderStatusRequest(
            id=4735419650
        )
    )
    assert response.status == 'ok'

def test_get_spot_orders(client: APIClient):
    response = client.get_spot_orders(
        GetSpotOrdersRequest(
            status = 'close',
            execution='limit',
            type = 'buy',
            details = 2,
        )
    )
    assert response.status == 'ok'


def test_update_order_status(client: APIClient):
    response_add = client.add_order(
        AddOrderRequest(
            type = 'sell',
            srcCurrency = 'ton',
            dstCurrency = 'usdt',
            amount = 10.0,
            price = 3,
            execution = 'limit',
            clientOrderId = "TEST2",
        )
    )
    assert response_add.status == 'ok'

    response = client.update_order(
        UpdateOrderStatusRequest(
            status = 'canceled',
            order=response_add.order.id,
        )
    )
    assert response.status == 'ok'


def test_cancel_orders(client: APIClient):

    response_add = client.add_order(
        AddOrderRequest(
            type = 'sell',
            srcCurrency = 'ton',
            dstCurrency = 'usdt',
            amount = 10.0,
            price = 3,
            execution = 'limit',
            clientOrderId = "TEST2",
        )
    )
    assert response_add.status == 'ok'

    response= client.cancel_orders(
        CancelOrdersRequest(
            execution = 'limit'
        )
    )
    assert response.status == 'ok'

def test_get_spot_trades(client: APIClient):
    response = client.get_spot_traded(
        GetTradesRequest(
            srcCurrency = 'eth',
            dstCurrency = 'usdt',
        )
    )

    assert response.status == 'ok'

def test_get_withdraws(client: APIClient):
    response = client.get_withdraws()

    assert response.status == 'ok'

