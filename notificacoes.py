import streamlit as st
import requests

def disparar_notificacao_planilha(mensagem):
    """
    Envia a mensagem de texto direto para o seu WhatsApp usando a API do CallMeBot.
    Substitui o Zapier completamente.
    """
    # Seus dados configurados da API do CallMeBot
    PHONE = "556198482916"
    API_KEY = "1302963"
    
    # Monta a URL exatamente no formato que o CallMeBot exige
    url_callmebot = "https://api.callmebot.com/whatsapp.php"
    
    # Parâmetros que vão anexados na URL (?phone=...&text=...&apikey=...)
    payload = {
        "phone": PHONE,
        "text": str(mensagem),
        "apikey": API_KEY
    }
    
    try:
        # O CallMeBot recebe dados via requisição GET
        resposta = requests.get(url_callmebot, params=payload, timeout=10)
        
        # Se retornar status 200, significa que o bot aceitou o envio
        if resposta.status_code == 200:
            return True
        return False
    except Exception:
        return False
