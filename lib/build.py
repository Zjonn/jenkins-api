import typing

from .artifacts import Artifacts
from .json_requests import get


class Build:
    def __init__(self, desc: typing.Union[typing.Dict]):
        self._url = desc["url"]
        self._number = str(desc["number"])
        self._result = desc["result"]

        self._artifacts = None
        self._description = None

    @property
    def url(self):
        return self._url

    @property
    def number(self):
        return self._number

    @property
    def result(self):
        return self._result

    @property
    def artifacts(self):
        if self._artifacts:
            return self._artifacts

        params = {"tree": "artifacts[relativePath]"}

        resp = get(self.url, params=params)["artifacts"]
        relative_paths = list(map(lambda r_path: r_path["relativePath"], resp))

        desc = {
            "url": super().__getattribute__("url"),
            "relative_paths": relative_paths,
        }

        self._artifacts = Artifacts(desc)

    @property
    def description(self):
        return self._description

    def __str__(self):
        return self.number + " " + self.result
