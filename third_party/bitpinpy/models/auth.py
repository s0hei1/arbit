from __future__ import annotations
from dataclasses import dataclass
from src_bitpinpy.models.abstracts import DataclassMappings


@dataclass
class AuthenticateRequest(DataclassMappings):
    api_key : str
    secret_key : str



@dataclass
class AuthenticateResponse:
    refresh : str
    access : str

    @staticmethod
    def from_dict(data: dict) -> AuthenticateResponse:
        return AuthenticateResponse(**data)


