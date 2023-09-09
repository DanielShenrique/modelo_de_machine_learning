import telebot
from decouple import config

CHAVE_API = config('API_KEY')

bot = telebot.TeleBot(CHAVE_API)

bot.polling()