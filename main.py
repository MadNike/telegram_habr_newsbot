import os
from habr_parser import HabrParser
import telebot

# Get news

# Tg bot
bot = telebot.TeleBot(os.environ.get("HABR_TG_BOT_TOKEN"))
