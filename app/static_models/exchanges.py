from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Exchange:
    name: str
    wss : str



class Exchanges:

    nobitex : ClassVar[Exchange] = Exchange(
        name='nobitex',
        wss ='wss://ws.nobitex.ir/connection/websocket'
    )

    bitpin : ClassVar[Exchange] = Exchange(
        name='bitpin',
        wss='wss://centrifugo.bitpin.ir/connection/websocket'
    )