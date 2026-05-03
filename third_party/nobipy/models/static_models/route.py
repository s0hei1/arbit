from dataclasses import dataclass
from http import HTTPMethod
from typing import Literal, ClassVar

PrivacyType = Literal['private', 'public']


@dataclass(frozen=True)
class Route:
    url : str
    privacy_type : PrivacyType
    http_method : HTTPMethod | None
    doc : str | None = None

    def url_with_path_parameter(self,path_parameter : str) -> str:
        _url = f'{self.url}/{path_parameter}'
        _url = _url.replace('//', '/')
        return _url

class Routes:
    get_order_book : ClassVar[Route] = Route(url = "/v3/orderbook/", privacy_type = "public",http_method = HTTPMethod.GET)
    get_order_book_all : ClassVar[Route] = Route(url = "/v3/orderbook/all", privacy_type = "public",http_method = HTTPMethod.GET)
    get_depth : ClassVar[Route] = Route(url = "/v2/depth/", privacy_type = "public",http_method = HTTPMethod.GET)
    get_trades : ClassVar[Route] = Route(url = "/v2/trades/", privacy_type = "public",http_method = HTTPMethod.GET)
    get_stats : ClassVar[Route] = Route(url = "/market/stats", privacy_type = "public",http_method = HTTPMethod.GET)
    get_market_history : ClassVar[Route] = Route(url = "/market/udf/history", privacy_type = "public",http_method = HTTPMethod.GET)

    get_user_profile : ClassVar[Route] = Route(url = "/users/profile", privacy_type = "private",http_method = HTTPMethod.GET)
    generate_wallet_address : ClassVar[Route] = Route(url = "/users/wallets/generate-address", privacy_type = "private",http_method = HTTPMethod.POST)
    add_user_bank_card : ClassVar[Route] = Route(url = "/users/cards-add/", privacy_type = "private",http_method = HTTPMethod.POST)
    add_user_bank_account : ClassVar[Route] = Route(url = "/users/accounts-add/", privacy_type = "private",http_method = HTTPMethod.POST)
    get_user_limitations : ClassVar[Route] = Route(url = "/users/limitations", privacy_type = "private",http_method = HTTPMethod.POST)
    get_user_wallets_list : ClassVar[Route] = Route(url = "/users/wallets/list", privacy_type = "private",http_method = HTTPMethod.GET)
    get_user_wallets_by_filtering : ClassVar[Route] = Route(url = "/v2/wallets", privacy_type = "private",http_method = HTTPMethod.GET)
    get_balance : ClassVar[Route] = Route(url = "/users/wallets/balance", privacy_type = "private",http_method = HTTPMethod.POST)
    get_user_wallet_transactions : ClassVar[Route] = Route(url = "/users/wallets/transactions/list", privacy_type = "private",http_method = HTTPMethod.GET)
    get_user_transactions_history : ClassVar[Route] = Route(url = "/users/transactions-history", privacy_type = "private",http_method = HTTPMethod.GET)
    get_user_wallet_deposits : ClassVar[Route] = Route(url = "/users/wallets/deposits/list", privacy_type = "private",http_method = HTTPMethod.GET)
    get_user_favorite_markets : ClassVar[Route] = Route(url = "/users/markets/favorite", privacy_type = "private",http_method = HTTPMethod.GET)
    post_user_favorite_markets : ClassVar[Route] = Route(url = "/users/markets/favorite", privacy_type = "private",http_method = HTTPMethod.POST)

    add_order : ClassVar[Route] = Route(url = "/market/orders/add", privacy_type = "private",http_method = HTTPMethod.POST)
    get_order_status : ClassVar[Route] = Route(
        url="/market/orders/status",
        privacy_type="private",
        http_method=HTTPMethod.POST
    )
    get_spot_orders : ClassVar[Route] = Route(
        url="/market/orders/list",
        privacy_type="private",
        http_method=HTTPMethod.GET
    )
    update_order_status : ClassVar[Route] = Route(
        url="/market/orders/update-status",
        privacy_type="private",
        http_method=HTTPMethod.POST
    )
    cancel_orders : ClassVar[Route] = Route(
        url="/market/orders/cancel-old",
        privacy_type="private",
        http_method=HTTPMethod.POST
    )
    get_spot_trades : ClassVar[Route] = Route(
        url="/market/trades/list",
        privacy_type="private",
        http_method=HTTPMethod.GET
    )


    withdraw_request : ClassVar[Route] = Route(url = "/users/wallets/withdraw", privacy_type = "private",http_method = HTTPMethod.POST)
    withdraw_request_confirm : ClassVar[Route] = Route(url = "/users/wallets/withdraw-confirm", privacy_type = "private",http_method = HTTPMethod.POST)
    get_withdraw_details : ClassVar[Route] = Route(url ="/withdraws/", privacy_type ="private", http_method = HTTPMethod.GET)
    get_withdraws : ClassVar[Route] = Route(url ="/users/wallets/withdraws/list", privacy_type ="private", http_method = HTTPMethod.GET)


    # create_api_key : ClassVar[Route] = Route(url = "/apikeys/create/", privacy_type = "private",http_method = HTTPMethod.POST)
