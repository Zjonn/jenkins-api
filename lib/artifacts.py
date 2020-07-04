import typing

from .json_requests import get


class Artifacts:
    def __init__(self, desc: typing.Union[typing.Dict]):
        self.url = desc['url']
        self.relative_paths = desc['relative_paths']

    def __str__(self):
        return f'Artifacts from {self.url}'
