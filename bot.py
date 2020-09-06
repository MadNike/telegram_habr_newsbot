from config import API_KEY
from habr_parser import HabrParser
import telebot
from concurrent.futures import ThreadPoolExecutor



class Bot:

    def __init__(self):
        self.api = telebot.TeleBot(API_KEY)
        self.parser = HabrParser()

        # Пока что айди подиписанных пользователей хранятся в текстовом файле

        @self.api.message_handler(content_types='text')
        def add_subscriber(message):
            if message.text == "/subscribe":
                with open('subscribers.txt', 'r') as read_file:
                    if str(message.from_user.id) not in read_file.readlines():
                        with open('subscribers.txt', 'a') as write_file:
                            write_file.write('\n'+str(message.from_user.id))
                    else:
                        self.api.send_message(message.from_user.id, "You are already subscribed!")

        self.api.polling()


    def send_last_post(self, user_id):
        self.api.send_message(user_id, self.parser.last_post.to_str())



# bot = Bot()