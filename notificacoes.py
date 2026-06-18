import streamlit as st
import requests
import json

URL_ZAPIER = "https://hooks.zapier.com/hooks/catch/27988630/43nzv0q/"

def disparar_notificacao_planilha(mensagem):
    """
    Envia a mensagem formatada em JSON com cabeçalhos explícitos para o Zapier.
    """
    payload = {"mensagem": str(mensagem)}
    headers = {"Content-Type": "application/json"}
    
    try:
        resposta = requests.post(
            URL_ZAPIER, 
            data=json.dumps(payload), 
            headers=headers, 
            timeout=5
        )
        if resposta.status_code in [200, 201]:
            return True
        return False
    except Exception:
        return False
