# título
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
# mostar a mensagem que o usuário enviou no chat


# Frameworks, bibliotecas, pacotes de códigos criados para resolver um problema, mas com condições específicas.

# Streamlit (o que será usado) -> consegue apenas com o Python criar o frontend (o que é visualizado pelo usuário) e o backend (a lógica do que acontece no frontend)
# Flask
# Django
# FastAPI

# a IA que será usada é: OpenAI

# Código da aula ao vivo inacabado:
# import streamlit as st

# st.write("Chatbot com IA")
# st.button()

# st.chat_input
# -----------------------------------------------------------------------------------------S
# Documentação das Bibliotecas:
# • Flask - https://flask.palletsprojects.com/en/2.3.x/
# • Flask no Visual Studio Code - https://code.visualstudio.com/docs/python/tutorial-flask
# • Socketio - https://socket.io/pt-br/docs/v4/
from flask import Flask, render_template  # estruturas para criar o site
from flask_socketio import SocketIO, send  # estruturas para criar o bot

app = Flask(__name__)   # criar o site
# chave de segurança, pode ser qualquer coisa, mas escolha algo difícil
app.config['SECRET'] = "ajuiahfa78fh9f78shfs768fgs7f6"
app.config["DEBUG"] = True  # para testar o código, pode ser retirado ao final
# cria a conexão entre diferentes que estão no mesmo site
socketIO = SocketIO(app, cors_allowed_origins="*")


# define que a função abaixo vai ser acionada quando o evento de "mensagem" acontecer
@socketIO.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    # envia a mensagem para todo mundo conectado ao site
    send(mensagem, broadcast=True)


@app.route("/")  # cria a página do site
def home():
    # essa página vai carregar esse arquivo htm que está aqui
    return render_template("index.html")


if __name__ == "__main__":
    # define que o app vai rodar no servidor local, ou seja, na internet que o computador está conectado
    socketIO.run(app, host='localhost')
