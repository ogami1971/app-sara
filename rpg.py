import streamlit as st

def exibir_rpg():
    st.title("⚔️ Nossa Jornada RPG")
    st.write("Cumpra as missões do aplicativo na vida real para acumular XP e desbloquear títulos lendários juntos!")
    st.markdown("---")
    
    # Simulação de XP baseada na interação do app
    st.subheader("📊 Seu Nível Atual")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="⭐ Nível do Casal", value="Nível 14")
    with col2:
        st.metric(label="✨ XP Total", value="1.450 / 2.000")
        
    st.progress(0.72, text="72% para o próximo nível")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🏆 Conquistas Desbloqueadas")
    
    conquistas = [
        {"icon": "🌹", "nome": "O Domador de Raposas", "desc": "Cativou a rosa mais única do asteroide B-612.", "status": "Desbloqueado", "cor": "#FFD700"},
        {"icon": "🎻", "nome": "Monólogo da Primavera", "desc": "Subiu o som do coração e trouxe cor ao mundo do outro.", "status": "Desbloqueado", "cor": "#FFD700"},
        {"icon": "⚔️", "nome": "Respiração do Amor: Primeira Forma", "desc": "Enfrentou a rotina diária com 5 beijos estalados seguidos.", "status": "Desbloqueado", "cor": "#FFD700"},
        {"icon": "⚙️", "nome": "Parceiro de Crime de Zaun", "desc": "Atravessou pontes e encarou o caos de Brasília de mãos dadas.", "status": "Bloqueado", "cor": "#888888"},
        {"icon": "👑", "nome": "Explorador de Brasília", "desc": "Completou uma missão hardcore mensal em um ponto turístico oficial.", "status": "Bloqueado", "cor": "#888888"}
    ]
    
    for c in conquistas:
        borda = c["cor"]
        st.markdown(f"""
            <div class='card' style='border-left: 5px solid {borda}; background-color: rgba(28, 37, 65, 0.85); padding: 15px; margin-bottom: 10px;'>
                <span style='float: right; font-size: 12px; font-weight: bold; color: {borda};'>{c['status']}</span>
                <h4 style='margin: 0px; color: #FFFFFF;'>{c['icon']} {c['nome']}</h4>
                <p style='margin: 5px 0 0 0; font-size: 13px; color: #aaa; font-style: italic;'>{c['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
