import telebot 
from telebot import types

from decouple import config

from util.utils import pre_processamento

import pickle

CHAVE_API = config('API_BOT')

bot = telebot.TeleBot(CHAVE_API)

listaComandos = ["start","status","comandos"]
quantidade_fraude = 0
quantidade_nao_fraude = 0
quantidade_mensagens = 0
textoPadrao = """
Ola Seja bem-vindo
O bot de processamento de (nlp) linguagem natural.
você poderar verificar e ter uma maior certeza do que e fraude ou não da sua mensagem."""

with open('modelo/modelo.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

with open('modelo/vectorize.pkl', 'rb') as arquivo:
    vectorize = pickle.load(arquivo)


def transformar_mensagem(texto):
    texto_transformado = pre_processamento(texto)
    return texto_transformado

@bot.message_handler(commands=["comandos","commands","c"])
def status(mensagem: types.Message):
    textoComandos = f"temos {len(listaComandos)} comandos\n"
    for comando in listaComandos:
        textoComandos = f"{textoComandos}Comando /{comando}\n"
    bot.send_message(mensagem.chat.id , textoComandos)

@bot.message_handler(commands=["start",'help'])
def boasVindas(mensagem: types.Message):
    bot.reply_to(mensagem,textoPadrao)

@bot.message_handler(commands=["status"])
def Status(mensagem: types.Message):
    resposta = f"Quantidade de fraude {quantidade_fraude}.\n"
    resposta += f"Quantidade de mensagem não fraude {quantidade_nao_fraude}.\n"
    resposta += f"Quantidade de mensagem lidas {quantidade_mensagens}.\n"
    resposta += f"Quantidade de propoção de fraudes encontradas {(quantidade_fraude/quantidade_mensagens)*100:.1f}%.\n"
    resposta += f"Quantidade de propoção de mensagens normais {(quantidade_nao_fraude/quantidade_mensagens)*100:.1f}%.\n"

    bot.send_message(mensagem.chat.id, resposta)

@bot.message_handler(func= lambda mensagem: True)
def escutando(mensagem: types.Message):
    global quantidade_fraude, quantidade_nao_fraude, quantidade_mensagens

    frase = transformar_mensagem(mensagem.text)
    frase_vectorizada = vectorize.transform([frase])
    predicao = modelo.predict(frase_vectorizada)

    if(predicao > -1):
        bot.reply_to(mensagem, "Essa mensagem é um possivel ameaça!!!")
        quantidade_fraude += 1
    else:
        quantidade_nao_fraude += 1

    quantidade_mensagens += 1


bot.polling()