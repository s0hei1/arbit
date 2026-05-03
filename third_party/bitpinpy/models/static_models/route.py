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
    authenticate : ClassVar[Route] = Route(url = "api/v1/usr/authenticate/", privacy_type = "public",http_method = HTTPMethod.POST)
    get_currencies : ClassVar[Route] = Route(url = "/api/v1/mkt/currencies/", privacy_type = "public",http_method = HTTPMethod.GET)
    get_markets : ClassVar[Route] = Route(url = "/api/v1/mkt/markets/", privacy_type = "public",http_method = HTTPMethod.GET)


