import telebot 
from telebot import types
from telebot.custom_filters import TextFilter
import spacy
import pandas as pd 

from sklearn.feature_extraction.text import TfidfVectorizer

from decouple import config

from util.utils import pre_processamento

import pickle

CHAVE_API = config('API_BOT')

bot = telebot.TeleBot(CHAVE_API)

listaComandos = ["start","status","test","comandos",]
mensagens = []
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

@bot.message_handler(commands=["test"])
def verificar(mensagem: types.Message):
    # # mensagem_vetor = vectorizer.transform(mensagens)
    # # aplicação do modelo de machine learning
    # # resposta = model.predict(mensagem_vetor)

    #TODO: trazer o método o vectorize
    #TODO: trazer o método para transformar as frases
    #TODO: utilizar o modelo para classificar
    #TODO: testar amanhã

    # nlp = spacy.load("en_core_web_md")
    for m in mensagens:
        frase = ""
        # doc = nlp(m.text)
        # for token in doc:
        #     frase += f"Palavra: \"{token.text}\" Classe gramatical: {token.pos_}\n"
        frase = transformar_mensagem(m.text)
        frase_vectorizada = vectorize.transform([frase])

        #TODO: alguma coisa está dando muito errada aqui
        #TODO: ver depois
        predicao = modelo.predict(frase_vectorizada)

        bot.send_message(mensagem.chat.id, frase)
        bot.send_message(mensagem.chat.id, predicao)
 


@bot.message_handler(commands=["status"])
def Status(mensagem: types.Message):
    bot.send_message(mensagem.chat.id , f"Quantidade de mensagem lidas {len(mensagens)}")
    for mensage in mensagens:
        bot.send_message(mensagem.chat.id , f"O texto: {mensage.text}")
    

@bot.message_handler(func= lambda mensagem: True)
def escutando(mensagem: types.Message):
    mensagens.append(mensagem)

bot.polling()