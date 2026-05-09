from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class CommonChannelURLs:
    order_book : str

@dataclass(frozen=True)
class Exchange:
    name: str
    wss: str
    channels_url: CommonChannelURLs


class Exchanges:

    nobitex : ClassVar[Exchange] = Exchange(
        name='nobitex',
        wss ='wss://ws.nobitex.ir/connection/websocket',
        channels_url= CommonChannelURLs(
            order_book= "public:orderbook-{symbol}"
        )
    )

    bitpin : ClassVar[Exchange] = Exchange(
        name='bitpin',
        wss='wss://centrifugo.bitpin.ir/connection/websocket',
        channels_url=CommonChannelURLs(
            order_book="public:orderbook-{symbol}"
        )

    )