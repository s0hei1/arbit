from dataclasses import dataclass,field
from typing import Literal
from third_party.nobipy.models.abstracts import DataclassMappings
from datetime import datetime

APIKeyPermissionType = Literal['READ', 'RADE', 'WITHDRAW']

@dataclass
class CreateAPIKeyRequestModel(DataclassMappings):
    name: str
    permissions: list[APIKeyPermissionType]

    description: str = ""
    ipAddressesWhitelist: list[str] = field(default_factory=list)
    expirationDate: datetime | None = None

    @property
    def formed_permissions(self) -> str:
        if len(self.permissions) == 0 or self.permissions is None:
            raise ValueError("APIKey Must Have 1 Permission at least")


        return ",".join(self.permissions)
