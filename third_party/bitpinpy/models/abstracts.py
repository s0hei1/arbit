from dataclasses import is_dataclass, asdict
import json

class DataclassMappings:

    def to_dict(self) -> dict:
        if not is_dataclass(self):
            raise TypeError("to_dict can only be used on dataclass instances")
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())