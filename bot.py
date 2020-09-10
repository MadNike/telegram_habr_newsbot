from config import API_KEY
from listener import Listener
import telebot



class Bot:


    def __init__(self):
        self.api = telebot.TeleBot(API_KEY)
        self.listner = Listener()

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


    def distribution(self):
        with open('subscribers.txt', 'r')  as f:
            for user in f.readlines():
                if user.strip():
                    for post in self.listner.listen():
                        self.api.send_message(user, post.to_str())


    def start(self):
        self.distribution()
        self.api.polling()
