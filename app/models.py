from __future__ import annotations

from dataclasses import dataclass
from numpy.typing import NDArray
import numpy as np
from typing import Literal

Exchanges = Literal['nobitex', 'bitpin']

@dataclass
class OrderBookEntry:
    price: np.float16
    volume: np.float16

    @staticmethod
    def from_nd_array(nd_array: NDArray[np.float16]) -> OrderBookEntry:
        return OrderBookEntry(
            price=np.float16(nd_array[0]),
            volume=np.float16(nd_array[1]),
        )

@dataclass(frozen=True)
class OrderBook:
    exchange_name : Exchanges
    asks: NDArray[np.float16, np.float16]
    bids: NDArray[np.float16, np.float16]


    def get_last_suggests(self):
        return self.last_bid, self.last_ask

    @property
    def last_bid(self):
        return self.bids[0]

    @property
    def last_ask(self):
        return self.asks[0]

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


