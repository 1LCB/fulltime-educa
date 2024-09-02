from dataclasses import dataclass


@dataclass
class HTTPResponse:
    status_code: int
    content: dict | str
    headers: dict = None
