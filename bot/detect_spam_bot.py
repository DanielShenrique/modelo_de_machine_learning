import telebot
from decouple import config

CHAVE_API = config('API_KEY')

bot = telebot.TeleBot(CHAVE_API)

textoPadrao = """
Ola Seja bem-vindo
O bot de processamento de (nlp) linguagem natural.
você poderar verificar e ter uma maior certeza do que e fraude ou não da sua mensagem."""

def verificar(mensagem):
    return True

@bot.message_handler(commands=["start"])
def boasVindas(mensagem):
    bot.reply_to(mensagem,textoPadrao)

bot.polling()