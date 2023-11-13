# 👨🏽‍🎓 Tratamento de mensagens de smishing para proteção no telegram - TCC

## 🗂️ Sumário

- <a href="#integrantes">Integrantes</a>
- <a href="#objetivo">Objetivo</a>
- <a href="#baixar-projeto-configurasoes">Baixar projeto</a>
- <a href="#tecnologias-utilizadas">Tecnologias utilizadas</a>

<div id="integrantes" >

## 🧑🏽‍💼 Integrantes
    
- <a href="https://github.com/DanielShenrique" target="_black">Daniel Henrique<a>
- <a href="https://github.com/natan-xav2019" target="_black">Natan Xavier<a>
    
</div>

<div id="objetivo">

## 📌 Objetivo
  
- [x] Encontrar base de dados
- [x] Importar base de dados
- [x] Tratar dados
- [x] Treinar modelo
- [x] Conexão com API do telegram BOT
- [x] Aplicar modelo dentro do telegram

</div>


<div id="baixar-projeto-configurasoes">

## 🖥️ Baixar projeto e configurar ambiente de desenvolvimento venv

1. clonar o repositorio

```bash
git clone https://github.com/DanielShenrique/modelo_de_machine_learning.git
```

2. Entre no diretório do projeto

```bash
cd modelo_de_machine_learning
```

3. Crie o ambiente virtual

```powershell
python -m venv venv
```

4. Ative o ambiente virtual

```powershell
venv\Scripts\activate
```

5. Instale todas as bibliotecas

```powershell
python -m pip install -r requirements.txt
```

6. Baixe a linguagem para o modelo

```powershell
python -m spacy download en_core_web_trf
```

7. Crie um arquivo .env para o projeto

```powershell
API_BOT="CHAVE_DO_BOT"
```

8. Chame o bot para um grupo em adicionar com a tag
```powershell
@adm_mensagem_Bot
```

9. Rode o projeto
```powershell
python -m detect_spam_bot
```

</div>

<div id="tecnologias-utilizadas">

## 📑 Tecnologias utilizadas

- Python:
  - Setuptools
  - Wheel
  - Autopep8
  - Pandas
  - Scikit-learn
  - Spacy
  - Seaborn
  - Python-decouple
  - Pytelegrambotapi
- Git:
  - git-flow
</div>


