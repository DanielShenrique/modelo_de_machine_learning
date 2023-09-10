import telebot
from decouple import config

CHAVE_API = config('API_KEY')

bot = telebot.TeleBot(CHAVE_API)

listaComandos = ["comandos","start","estatos"]

textoPadrao = """
Ola Seja bem-vindo
O bot de processamento de (nlp) linguagem natural.
você poderar verificar e ter uma maior certeza do que e fraude ou não da sua mensagem."""

@bot.message_handler(commands=["comandos","commands","c"])
def status(mensagem):
    textoComandos = f"temos {len(listaComandos)} commandos\n"

    for comando in listaComandos:
        textoComandos = f"{textoComandos}Comando /{comando}\n"
    bot.send_message(mensagem.chat.id , textoComandos)

@bot.message_handler(commands=["start"])
def boasVindas(mensagem):
    bot.reply_to(mensagem,textoPadrao)

bot.polling()