from post import Post
import requests
from bs4 import BeautifulSoup as bs

class HabrParser:

    def __init__(self):
        self.url = 'https://habr.com/ru/'
        self.__data = requests.get(self.url)
        self.__soup = bs(self.__data.text, 'html.parser')
        self.last_post = self.get_last_post()

    def get_last_post(self):
        last_post = self.__soup.find('li', class_='content-list__item')
        return Post.from_bs_tag(last_post)

    def new_post(self):
        if self.last_post != self.get_last_post():
            self.last_post = self.get_last_post()
            return True
        else:
            return False


