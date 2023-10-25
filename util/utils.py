import re
import spacy

nlp = spacy.load("en_core_web_trf")

def remover_espacos(text):
    frases_sem_espaco_frente = " ".join(text.split())
    return frases_sem_espaco_frente

def remover_caractere_especial(text):
    texto_sem_cs = re.sub(r"ï¿½", r"", text)
    texto_sem_cs = re.sub(r"&lt;([^>]+)&gt;", r"", texto_sem_cs)
    texto_sem_cs = re.sub(r"�", r" ", texto_sem_cs)
    texto_sem_cs = re.sub(r"ü", r"u", texto_sem_cs)
    texto_sem_cs = re.sub(r"Ü", r"U", texto_sem_cs)
    texto_sem_cs = re.sub(r"\(", r" ", texto_sem_cs)
    texto_sem_cs = re.sub(r"&amp;", r"", texto_sem_cs)
    return texto_sem_cs

def remover_emoji(text):
    text_sem_emoji = re.sub(r"((:|;)(-){0,1}(\)|\())", f"", text)
    return text_sem_emoji

def remover_pontos(text):
    doc = nlp(text)
    frases_sem_ponto = " ".join([token.text for token in doc if not token.is_punct]).lower()
    return frases_sem_ponto

def lemmatizar(text):
    doc = nlp(text)
    frases_lematizadas = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return frases_lematizadas

def substituir_numero_telefone(text):
    texto_com_numero_padronizado = re.sub(r"((\d{4}\s\d{3}\s\d{4})|\d{10,12})(\s|$|\/)", f"PH_NUMBER ", text)
    return texto_com_numero_padronizado

def substituir_email(text):
    texto_com_email_padronizado = re.sub(r"\S+@\S+($){0,1}", f"EMAIL", text)
    return texto_com_email_padronizado

def pre_processamento(text):
    texto_processado = text
    texto_processado = remover_emoji(texto_processado)
    texto_processado = remover_caractere_especial(texto_processado)
    texto_processado = remover_espacos(texto_processado)  
    texto_processado = remover_pontos(texto_processado)
    texto_processado = substituir_numero_telefone(texto_processado)
    texto_processado = substituir_email(texto_processado)
    texto_processado = lemmatizar(texto_processado)
    return texto_processado