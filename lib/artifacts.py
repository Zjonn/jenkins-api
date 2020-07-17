import typing

from .jenkins_requests import get_node


class Artifacts:
    def __init__(self, desc: typing.Union[typing.Dict]):
        self.url = desc["url"]

        self._relative_paths = None
        self._paths = None

    @property
    def relative_paths(self):
        if self._relative_paths:
            return self._relative_paths

        resp = get_node(self.url, "artifacts", subnodes="relativePath")
        self._relative_paths = list(map(lambda r_path: r_path["relativePath"], resp))

        return self._relative_paths

    def __str__(self):
        return f"Artifacts from {self.url}"
