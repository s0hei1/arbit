from __future__ import annotations

from dataclasses import dataclass
from numpy.typing import NDArray
import numpy as np
from typing import Literal

Exchanges = Literal['nobitex', 'bitpin']

@dataclass(frozen=True)
class OrderBook:
    exchange_name : Exchanges
    asks: NDArray[np.float16]
    bids: NDArray[np.float16]


    def get_last_suggests(self):
        return self.asks[-1], self.bids[-1]

    @staticmethod
    def from_bitpin(data: dict[str, ...]) -> OrderBook:
        return OrderBook(
            exchange_name='bitpin',
            asks=np.array(
                [
                    (
                        np.float64(i[0]), np.float64(i[1])
                    )
                    for i in data['asks']
                ]
            ),
            bids=np.array(
                [
                    (
                        np.float64(i[0]), np.float64(i[1])
                    )
                    for i in data['bids']
                ]
            ),
        )

    @staticmethod
    def from_nobitex(data: dict[str, ...]) -> OrderBook:
        return OrderBook(
            exchange_name='nobitex',
            asks=np.array(
                [
                    (
                        np.float64(i[0]), np.float64(i[1])
                    )
                    for i in data['asks']
                ]
            ),
            bids=np.array(
                [
                    (
                        np.float64(i[0]), np.float64(i[1])
                    )
                    for i in data['bids']
                ]
            ),
        )


