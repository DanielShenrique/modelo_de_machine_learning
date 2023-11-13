import telebot
from telebot import types
from decouple import config
from util.utils import pre_processamento
import util.formato_porcento as fp
from decimal import Decimal
import pickle

CHAVE_API = config('API_BOT')

bot = telebot.TeleBot(CHAVE_API)

listaComandos = ["start","status","comandos"]
quantidade_fraude = 0
quantidade_nao_fraude = 0
quantidade_mensagens = 0
mensagem_apresentacao = """
Olá, me chamo Fraud Seeker!
Sou um bot que irá verificar as suas mensagens no grupo ou no meu privado quando desejar me enviar.
Ficarei sempre a escutar as mensagens para manter a sua segurança.
Afinal essa é a minha prioridade, tornar o mundo da internet um lugar mais seguro.
"""

with open('modelo/modelo.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

with open('modelo/vectorize.pkl', 'rb') as arquivo:
    vectorize = pickle.load(arquivo)


def transformar_mensagem(texto):
    texto_transformado = pre_processamento(texto)
    return texto_transformado

@bot.message_handler(commands=["comandos","commands","c"])
def status(mensagem: types.Message):
    textoComandos = f"Temos {len(listaComandos)} comandos\n"
    for comando in listaComandos:
        textoComandos = f"{textoComandos}Comando /{comando}\n"
    bot.send_message(mensagem.chat.id , textoComandos)

@bot.message_handler(commands=["start",'help'])
def boasVindas(mensagem: types.Message):
    bot.reply_to(mensagem,mensagem_apresentacao)

@bot.message_handler(commands=["status"])
def Status(mensagem: types.Message):
    if(quantidade_mensagens):
        porcentagem_faude = fp.formato_porcentagem(quantidade_fraude/quantidade_mensagens)
        porcentagem_nao_faude = fp.formato_porcentagem(quantidade_nao_fraude/quantidade_mensagens)    
        resposta = f"Quantidade de fraude {quantidade_fraude}.\n"
        resposta += f"Quantidade de mensagem não fraude {quantidade_nao_fraude}.\n"
        resposta += f"Quantidade de mensagem lidas {quantidade_mensagens}.\n"
        resposta += f"Quantidade de propoção de fraudes encontradas {porcentagem_faude}.\n"
        resposta += f"Quantidade de propoção de mensagens normais {porcentagem_nao_faude}.\n"
        bot.send_message(mensagem.chat.id, resposta)
    else:
        bot.send_message(mensagem.chat.id, "Nenhuma mensagem lida até o momento.")


@bot.message_handler(func= lambda mensagem: True)
def escutando(mensagem: types.Message):
    global quantidade_fraude, quantidade_nao_fraude, quantidade_mensagens

    frase = transformar_mensagem(mensagem.text)
    frase_vectorizada = vectorize.transform([frase])
    predicao = modelo.predict(frase_vectorizada)

    if(predicao > -1):
        bot.reply_to(mensagem, "Essa mensagem é uma possivel ameaça!!!")
        quantidade_fraude += 1
    else:
        quantidade_nao_fraude += 1

    quantidade_mensagens += 1


bot.polling()