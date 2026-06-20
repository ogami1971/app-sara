import streamlit as st
import requests

def disparar_notificacao_planilha(mensagem, quem_enviou="Sara"):
    """
    Envia mensagens para o WhatsApp do Denner. O texto muda indicando quem realizou
    a ação dentro do aplicativo, centralizando os alertas até a API da Sara estar pronta.
    """
    
    # 🚨 USANDO SEU NÚMERO E SUA CHAVE PARA AMBOS OS CASOS:
    WHATSAPP_DENNER = "556198482916"
    API_KEY_DENNER = "1302963"

    url_callmebot = "https://api.callmebot.com/whatsapp.php"
    
    # 🎭 PERSONALIZAÇÃO DO TEXTO DO ALERTA
    if quem_enviou.lower() == "sara":
        # Mensagem avisando você sobre o que ela fez
        mensagem_formatada = f"🪐 *Alerta do Pequeno Príncipe!* \n\nDenner, a sua rosa (Sara) acabou de interagir no app! \n\n📋 *Ação dela:* {mensagem}"
    else:
        # Confirmação enviada para você informando que seu carinho foi processado
        mensagem_formatada = f"🌹 *Confirmação de Envio (Para Denner):* \n\nSeu carinho foi processado com sucesso! Você enviou para a Sara:\n\n✨ {mensagem}"

    # Parâmetros apontando sempre para o seu celular
    payload = {
        "phone": WHATSAPP_DENNER,
        "text": mensagem_formatada,
        "apikey": API_KEY_DENNER
    }
    
    try:
        resposta = requests.get(url_callmebot, params=payload, timeout=10)
        if resposta.status_code == 200:
            return True
        return False
    except Exception:
        return False
