import typing

from .artifacts import Artifacts
from .jenkins_requests import get_node


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

        desc = {"url": self.url}
        self._artifacts = Artifacts(desc)
        return self._artifacts

    @property
    def description(self):
        if self._description:
            return self._description

        self._description = get_node(self.url, 'description')
        return self._description

    def __str__(self):
        return self.number + " " + self.result
