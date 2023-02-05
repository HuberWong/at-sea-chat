from typing import NamedTuple


class Status(NamedTuple):
    is_ok: bool
    massage: str


class StatusWithToken(Status):
    token: str
