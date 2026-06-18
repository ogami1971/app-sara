import streamlit as st

def exibir_rpg():
    st.title("⚔️ Nossa Jornada RPG")
    st.write("Cumpra as missões na vida real, marque-as como concluídas e suba de nível!")
    st.markdown("---")
    
    # Inicializa o XP se não existir
    if "xp_total" not in st.session_state:
        st.session_state["xp_total"] = 0
        st.session_state["missoes_concluidas_count"] = 0

    xp = st.session_state["xp_total"]
    
    # Cálculo progressivo de Nível (Ex: 1500 XP = Nível 1 com 500/1000 XP)
    nivel_atual = (xp // 1000) + 1
    xp_neste_nivel = xp % 1000
    progresso_barra = xp_neste_nivel / 1000.0

    st.subheader("📊 Seu Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="⭐ Nível Atual", value=f"Nível {nivel_atual}")
    with col2:
        st.metric(label="✨ XP Atual", value=f"{xp_neste_nivel} / 1000")
    with col3:
        st.metric(label="✅ Missões Feitas", value=f"{st.session_state['missoes_concluidas_count']}")
        
    st.progress(progresso_barra, text=f"{int(progresso_barra * 100)}% para o Nível {nivel_atual + 1}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🏆 Títulos e Conquistas")
    
    # Sistema dinâmico de travar/destravar conquistas por nível
    conquistas = [
        {"icon": "🌹", "nome": "O Domador de Raposas", "desc": "Cativou a rosa mais única do universo.", "req": 1},
        {"icon": "🎻", "nome": "Monólogo da Primavera", "desc": "Trouxe cor e música para a vida do outro.", "req": 2},
        {"icon": "⚔️", "nome": "Respiração do Amor", "desc": "Mostrou dedicação diária exemplar.", "req": 3},
        {"icon": "⚙️", "nome": "Parceiro de Crime de Zaun", "desc": "Alcançou o nível 4 de pura sintonia.", "req": 4},
        {"icon": "👑", "nome": "Explorador de Brasília", "desc": "Nível 5: O mestre absoluto dos rolês.", "req": 5}
    ]
    
    for c in conquistas:
        desbloqueado = nivel_atual >= c["req"]
        borda = "#FFD700" if desbloqueado else "#888888"
        status_texto = "✨ Desbloqueado" if desbloqueado else f"🔒 Bloqueado (Nível {c['req']})"
        
        st.markdown(f"""
            <div class='card' style='border-left: 5px solid {borda}; background-color: rgba(28, 37, 65, 0.85); padding: 15px; margin-bottom: 10px;'>
                <span style='float: right; font-size: 12px; font-weight: bold; color: {borda};'>{status_texto}</span>
                <h4 style='margin: 0px; color: #FFFFFF;'>{c['icon']} {c['nome']}</h4>
                <p style='margin: 5px 0 0 0; font-size: 13px; color: #aaa; font-style: italic;'>{c['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
