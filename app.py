import streamlit as st
# Configuração da página (DEVE ser o primeiro comando Streamlit do script)
st.set_page_config(page_title="Universo de Amor", page_icon="🌹", layout="wide")

import dados
import telas

# 1. CARREGAMENTO DOS DADOS (Recebendo as 4 abas do Sheets)
capa_data, df_elogios, df_missoes, df_cupons = dados.carregar_dados()

# Inicializa as variáveis de progresso (XP e Nível) vindas do banco local
dados.carregar_progresso_banco()

# 2. MENU LATERAL INTERATIVO
st.sidebar.title("🌌 Menu Interativo")
st.sidebar.write("Navegue pelo nosso mundo:")

# CORREÇÃO AQUI: Nome unificado para opcoes_menu
opcoes_menu = {
    "💕 Início & Carinho": "inicio",
    "🎯 Missões Secretas": "missoes",
    "⚔️ Nossa Jornada RPG": "rpg",
    "🎟️ Máquina de Cupons": "cupons",
    "🔮 Central de Conquistas": "conquistas",
    "🎰 Roleta de Rolês": "roleta",
    "⏳ Tempo Juntos": "tempo",
    "💬 Enviar Carinho": "enviar_carinho"
}

# Cria os botões de rádio no menu lateral
selecao = st.sidebar.radio(
    "Menu", 
    list(opcoes_menu.keys()), 
    label_visibility="collapsed"
)

# CORREÇÃO AQUI: Buscando na variável certa 'opcoes_menu'
item_selecionado = opcoes_menu[selecao]

st.sidebar.markdown("---")
st.sidebar.subheader("🎵 Trilha Sonora")
st.sidebar.video("https://www.youtube.com/watch?v=FkWw9_L0g3o")

# 3. DIRECIONAMENTO DAS TELAS
if item_selecionado == "inicio":
    telas.exibir_inicio(capa_data, df_elogios)

elif item_selecionado == "missoes":
    telas.exibir_missoes(df_missoes)

elif item_selecionado == "cupons":
    telas.exibir_maquina_cupons(df_cupons)

elif item_selecionado == "conquistas":
    telas.exibir_central_conquistas()

elif item_selecionado == "enviar_carinho":
    telas.exibir_enviar_carinho()

else:
    st.title("🚀 Em Construção")
    st.info("Essa parte do universo está sendo moldada por estrelas. Volte logo!")
