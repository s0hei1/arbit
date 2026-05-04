from logging import Logger
from typing import Callable
from httpx import Request, Response
logger = Logger(__name__)



def request_logger(
        show_url : bool = True,
        show_body : bool = False,
) -> Callable[[Request],None]:

    def wrapper(request: Request):
        if show_url:
            logger.warning(f"\nREQUEST.{request.method} {request.url}")
        if show_body:
            logger.warning(f"R EQUEST.{request.read()}")

    return wrapper


def response_logger(
        show_url: bool = True,
        show_status_code : bool = True,
        show_body: bool = True,
) -> Callable[[Response],None]:
    def wrapper(response: Response):
        if show_url:
            logger.warning(f"RESPONSE FROM -> {response.url}")
        if show_status_code:
            logger.warning(f"RESPONSE.CODE -> {response.status_code}")
        if show_body:
            logger.warning(f"RESPONSE.BODY -> {response.read()}")

    return wrapper
