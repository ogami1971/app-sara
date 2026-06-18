import streamlit as st
import random

def exibir_roleta():
    st.title("🍿 O Decisor Cósmico")
    st.write("Bateu aquela dúvida clássica sobre o que fazer ou assistir? Deixe o destino do nosso universo decidir!")
    st.markdown("---")
    
    animes = ["Demon Slayer ⚔️", "Your Lie in April 🎻", "Arcane ⚙️", "Um filme de romance aleatório 🎬", "Maratona de séries comendo pipoca 🍿"]
    comidas = ["Pizza na Asa Norte 🍕", "Hambúrguer artesanal 🍔", "Japa caprichado 🍣", "Açaí gelado no final da tarde 🍧", "Cozinharem algo juntos do zero 🍳"]
    roles = ["Piquenique no CCBB 🧺", "Pôr do sol na Ermida Dom Bosco 🌅", "Cineminha com combo duplo 🎟️", "Caminhada relaxante no Parque da Cidade 🌳", "Ficar de bobeira em uma cabana de lençóis ⛺"]
    
    tab1, tab2, tab3 = st.tabs(["📺 O que assistir?", "🍕 O que comer?", "🚗 Onde ir?"])
    
    with tab1:
        st.subheader("Qual a maratona de hoje?")
        if st.button("🎰 Sortear Tela", key="btn_anime"):
            escolha = random.choice(animes)
            st.markdown(f"<div class='card' style='text-align: center; font-size: 22px; font-weight: bold; color: #FFD700;'>🎬 {escolha}</div>", unsafe_allow_html=True)
            
    with tab2:
        st.subheader("Qual o cardápio da vez?")
        if st.button("🎰 Sortear Fome", key="btn_comida"):
            escolha = random.choice(comidas)
            st.markdown(f"<div class='card' style='text-align: center; font-size: 22px; font-weight: bold; color: #FFD700;'>😋 {escolha}</div>", unsafe_allow_html=True)
            
    with tab3:
        st.subheader("Para onde vamos sair?")
        if st.button("🎰 Sortear Rolê", key="btn_role"):
            escolha = random.choice(roles)
            st.markdown(f"<div class='card' style='text-align: center; font-size: 22px; font-weight: bold; color: #FFD700;'>📍 {escolha}</div>", unsafe_allow_html=True)
