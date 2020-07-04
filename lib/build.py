import typing

from .artifacts import Artifacts
from .json_requests import get


class Build:
    def __init__(self, desc: typing.Union[typing.Dict]):
        self.url = desc['url']
        self.number = str(desc['number'])
        self.result = desc['result']

        self.artifacts = None
        self.description = None

    def __getattribute__(self, name):
        item = super().__getattribute__(name)

        if item:
            return item

        if name == 'artifacts':
            params = {'tree': name + '[relativePath]'}

            resp = get(self.url, params=params)[name]
            relative_paths = list(
                map(lambda r_path: r_path['relativePath'], resp))

            desc = {
                'url': super().__getattribute__('url'),
                'relative_paths': relative_paths
            }

            item = Artifacts(desc)
        else:
            params = {'tree': name}
            resp = get(self.url, params=params)[name]
            item = resp
        super().__setattr__(name, resp)
        return item

    def __str__(self):
        return self.number + ' ' + self.result
