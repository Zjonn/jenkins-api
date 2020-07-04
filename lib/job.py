import typing

from .build import Build
from .json_requests import get


class Job():
    def __init__(self, desc: typing.Union[typing.Dict]):
        self.url = desc['url']
        self.name = desc['name']

    def __getattribute__(self, name):
        item = super().__getattribute__(name)
        if not item:
            params = {'tree': name}
            item = get(self.url, params=params)
            super().__setattr__(name, item)
        return item

    def __str__(self):
        return self.name

    def get_build(self, number: typing.Union[str, int]) -> Build:
        params = {'tree': 'url,number,result'}
        resp = get([self.url, str(number)], params=params)
        return Build(resp)

    def get_builds(self) -> typing.List[Build]:
        params = {'tree': 'builds[url,number,result]'}
        resp = get(self.url, params=params)
        raw_builds = resp['builds']
        return list(map(lambda build_desc: Build(build_desc), raw_builds))
