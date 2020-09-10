from queue import SimpleQueue
import time
import requests
from utils import last_post_from_response
from concurrent.futures import ThreadPoolExecutor

class Listener:

    def __init__(self, url = 'https://habr.com/ru/'):
        self.queue = SimpleQueue()
        self.session = requests.Session()
        self.__url = url

    def __check_updates(self):
        response = self.session.get(self.__url)
        while True:
            time.sleep(60*5)
            if response != self.session.get(self.__url):
                response = self.session.get(self.__url)
                self.queue.put(last_post_from_response(response))

    def listen(self):
        with ThreadPoolExecutor(max_workers=1) as thread:
            thread.submit(self.__check_updates)
        while True:
            yield self.queue.get()



