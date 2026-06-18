import streamlit as st
from estilos import aplicar_estilos
from dados import carregar_dados
import telas

# 1. Configuração da Página
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Aplicar Visual CSS
aplicar_estilos()

# 3. Inicializar Session State
if "historico_carinhos" not in st.session_state:
    st.session_state["historico_carinhos"] = []

# 4. Carregar Dados da Planilha
capa_data, df_elogios, df_missoes = carregar_dados()

# 5. Menu Lateral
st.sidebar.title("🌌 Menu Interativo")
tela_selecionada = st.sidebar.radio(
    "Navegue pelo nosso mundo:",
    ["🌌 Início & Carinho", "🎯 Missões Secretas", "📸 Nosso Diário", "⏳ Nossa Linha do Tempo", "💬 Enviar Carinho"]
)
st.sidebar.markdown("---")
st.sidebar.info("Feito com ❤️ por Denner")

# 6. Roteador de Telas
if tela_selecionada == "🌌 Início & Carinho":
    telas.exibir_inicio(capa_data, df_elogios)

elif tela_selecionada == "🎯 Missões Secretas":
    telas.exibir_missoes(df_missoes)

elif tela_selecionada == "📸 Nosso Diário":
    telas.exibir_diario()

elif tela_selecionada == "⏳ Nossa Linha do Tempo":
    telas.exibir_linha_tempo()

elif tela_selecionada == "💬 Enviar Carinho":
    telas.exibir_enviar_carinho()
