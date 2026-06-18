import streamlit as st
from datetime import datetime

def exibir_contador():
    st.title("⏳ Nossa Linha Temporal")
    st.write("Contando cada segundo exato do nosso marco inicial neste planeta.")
    st.markdown("---")
    
    # 🌟 CONFIGURAÇÃO: Altere aqui para a data e hora exata em que começaram a namorar!
    # Formato: datetime(ANO, MÊS, DIA, HORA, MINUTO)
    data_inicio = datetime(2025, 6, 12, 20, 0) 
    agora = datetime.now()
    
    diferenca = agora - data_inicio
    
    dias = diferenca.days
    horas = diferenca.seconds // 3600
    minutos = (diferenca.seconds % 3600) // 60
    
    st.subheader("🔒 Tempo de União Ininterrupto")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="📆 Dias", value=f"{dias} dias")
    with col2:
        st.metric(label="⏰ Horas", value=f"{horas}h")
    with col3:
        st.metric(label="⏱️ Minutos", value=f"{minutos}min")
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🎯 Próximos Marcos Universais")
    
    # Calcula dias para o próximo dia 12 (mêsversário/aniversário)
    if agora.day <= 12:
        dias_restantes = 12 - agora.day
    else:
        # Aproximação simples para o próximo mês
        dias_restantes = (30 - agora.day) + 12
        
    st.info(f"🎁 Faltam aproximadamente **{dias_restantes} dias** para a nossa próxima data comemorativa oficial! Prepare o coração.")
