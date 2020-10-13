import typing
import requests
import os.path as path

JSON_API = "api/json"


def build_url(base: typing.Union[str, typing.List[str]], *args) -> str:
    if type(base) is list:
        url = base[0]
        parts = base[1:]
        parts.extend(args)
    else:
        url = base
        parts = args

    for part in parts:
        f_part = part[1:] if part.startswith("/") else part
        url = path.join(url, f_part)

    return url


def get(url: typing.Union[str, typing.List[str]], params=None, **kwargs) -> typing.Dict:
    req_url = build_url(url, JSON_API)
    return requests.get(req_url, params=params, **kwargs).json()
