import typing

from .json_requests import get


def get_node(
    url: typing.Union[str, typing.List[str]],
    node: str,
    subnodes: typing.Union[str, typing.List[str]] = None,
):
    if type(subnodes) is list:
        subnodes = ",".join(subnodes)

    if subnodes:
        subnodes = f"[{subnodes}]"

    params = {"tree": f"{node}{subnodes}"}
    return get(url, params=params)[node]
