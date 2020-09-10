from post import Post
from bs4 import BeautifulSoup as bs

def last_post_from_response(response):
    return Post.from_bs_tag(bs(response.text, 'html.parser').find('li', class_='content-list__item'))






