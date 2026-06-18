import streamlit as st
import requests

# Link oficial do seu Zapier
URL_ZAPIER = "https://hooks.zapier.com/hooks/catch/27988630/43nzv0q/"

def disparar_notificacao_planilha(mensagem):
    """
    Envia a mensagem em tempo real direto para o Webhook do Zapier.
    """
    payload = {"mensagem": mensagem}
    try:
        resposta = requests.post(URL_ZAPIER, json=payload, timeout=5)
        # O Zapier costuma retornar status 200 quando recebe com sucesso
        if resposta.status_code == 200:
            return True
        return False
    except Exception:
        return False

def verificar_datas_comemorativas():
    """
    Checa datas especiais (opcional para o app.py).
    """
    pass
