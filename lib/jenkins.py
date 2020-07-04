import typing

from .job import Job
from .json_requests import get


class Jenkins:
    def __init__(self,
                 url: str,
                 username: typing.Optional[str] = None,
                 api_token: typing.Optional[str] = None):
        self.url = url

        self.jobs = None

        if username and api_token:
            self.auth = (username, api_token)

    def __getattribute__(self, name):
        item = super().__getattribute__(name)
        if not item:
            params = {'tree': f'{name}'}
            item = get(super().__getattribute__('url'), params=params)
        return item

    def __str__(self):
        return self.url

    def get_job(self, job_name: str) -> Job:
        params = {'tree': 'url,name'}
        resp = get([self.url, 'job', job_name], params)
        return Job(resp)

    def get_jobs(self) -> typing.List[Job]:
        params = {'tree': 'jobs[url,name]'}
        resp = get(self.url, params=params)
        jobs = resp['jobs']
        return list(map(lambda job_desc: Job(job_desc), jobs))

    def get_all_jobs(self) -> typing.List[Job]:
        pass
