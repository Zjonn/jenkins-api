import typing
import requests

JSON_API = 'api/json'


def build_url(base: typing.Union[str, typing.List[str]], *args) -> str:
    if type(base) is list:
        url = base[0]
        parts = base[1:]
        parts.extend(args)
    else:
        url = base
        parts = args

    for part in parts:
        if url.endswith('/'):
            url = url[:-1]
        if not part.startswith('/'):
            url += '/'
        url += part

    return url


def get(url: typing.Union[str, typing.List[str]],
        params=None,
        **kwargs) -> typing.Dict:
    req_url = build_url(url, JSON_API)
    return requests.get(req_url, params=params, **kwargs).json()
