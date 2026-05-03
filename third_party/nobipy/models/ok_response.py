from __future__ import annotations
from dataclasses import dataclass

@dataclass
class OkResponse:
    status: str

    @staticmethod
    def from_dict(data: dict) -> OkResponse:
        return OkResponse(
            status=data["status"],
        )
