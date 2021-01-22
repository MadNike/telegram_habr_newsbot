from config import API_KEY
import telebot
import time
import requests
from utils import last_post_from_response
from queue import SimpleQueue
from concurrent.futures import ThreadPoolExecutor



class Bot:


    def __init__(self):
        self.api = telebot.TeleBot(API_KEY)
        self.queue = SimpleQueue()
        self.__url = 'https://habr.com/ru/'

        @self.api.message_handler(content_types='text')
        def add_subscriber(message):
            if message.text == "/subscribe":
                with open('subscribers.txt', 'r') as read_file:  # Пока что айди подиписанных пользователей хранятся в текстовом файле
                    if str(message.from_user.id) not in read_file.readlines():
                        with open('subscribers.txt', 'a') as write_file:
                            write_file.write(str(message.from_user.id) + "\n")
                    else:
                        self.api.send_message(message.from_user.id, "You are already subscribed!")

        with ThreadPoolExecutor(max_workers=3) as thread:
            thread.submit(self.update)
            thread.submit(self.send_post)
            thread.submit(self.api.polling)

    def update(self):
        response = requests.get('https://google.com/')
        while True:
            time.sleep(10)
            if response.text != requests.get(self.__url).text:
                response = requests.get(self.__url)
                self.queue.put(last_post_from_response(response))


    def listen(self):
        while True:
            yield self.queue.get()


    def send_post(self):
        for post in self.listen():
            with open('subscribers.txt', 'r')  as f:
                for id in f.readlines():
                    if id != "\n":
                        self.api.send_message(int(id), post.to_str())


    # def distribution(self):
    #     with open('subscribers.txt', 'r')  as f:
    #         for user in f.readlines():
    #             if user.strip():
    #                 self.api.send_message(user, post.to_str())


