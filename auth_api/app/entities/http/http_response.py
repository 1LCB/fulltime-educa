from dataclasses import dataclass


@dataclass
class HttpResponse:
    status_code: int
    content: dict | str
    headers: dict = None
