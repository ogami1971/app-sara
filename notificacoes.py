import streamlit as st
import requests
from datetime import datetime

# URL Webhook alternativa se você preferir disparar direto pro Zapier sem passar pela planilha:
# URL_ZAPIER = "SUA_URL_WEBHOOK_DO_ZAPIER_AQUI"

def disparar_notificacao_planilha(mensagem):
    """
    Esta função gera um link que adiciona os dados direto na planilha para o Zapier ler,
    ou injeta no sistema para envio.
    """
    hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Como rodamos o app de forma pública, para escrever na planilha de forma direta 
    # simulamos o envio dos parâmetros ou via Forms/Webhook.
    # Para testes rápidos, podemos usar o Webhook do Zapier que é mais seguro e direto!
    
    # Se você configurou o Catch Hook no Zapier:
    url_webhook = st.secrets.get("ZAPIER_WEBHOOK", "")
    if url_webhook:
        payload = {"data": hoje, "mensagem": mensagem, "status": "Disparado"}
        try:
            requests.post(url_webhook, json=payload)
            return True
        except Exception:
            return False
    return False

def verificar_datas_comemorativas():
    """
    Checa se hoje é uma data especial e agenda a notificação automática no Zapier.
    """
    agora = datetime.now()
    dia = agora.day
    mes = agora.month
    
    # Evita múltiplos disparos no mesmo dia usando cache de sessão
    if "notificacao_hoje_enviada" not in st.session_state:
        st.session_state["notificacao_hoje_enviada"] = False
        
    if not st.session_state["notificacao_hoje_enviada"]:
        # Exemplo 1: Aniversário de Namoro (Todo dia 12)
        if dia == 12:
            msg = f"🌹 Hoje é dia 12/{mes}! Mais um mêsversário de namoro oficial de vocês. Vá ao app ver as novas missões!"
            disparar_notificacao_planilha(msg)
            st.session_state["notificacao_hoje_enviada"] = True
            
        # Exemplo 2: Uma data específica (Ex: Aniversário dela - Ajuste para o dia real)
        elif dia == 25 and mes == 12:
            msg = "🎂 Parabéns para a sua rosa única! O universo inteiro está em festa hoje. Confira o presente secreto no app!"
            disparar_notificacao_planilha(msg)
            st.session_state["notificacao_hoje_enviada"] = True
