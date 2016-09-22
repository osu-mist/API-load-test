from locust import HttpLocust, TaskSet, task
from config import *


class UserBehavior(TaskSet):

    @task(1)
    def request_static_urls(self):
        for url in static_urls:
            self.client.get(url,
                verify=False,
                auth=(username, password)
                )

    @task(1)
    def request_dynamic_urls(self):
        for url, params in dynamic_urls:
            for param in params:
                self.client.get(url + param,
                 name=url,
                 verify=False,
                 auth=(username, password)
                 )


class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 9000
