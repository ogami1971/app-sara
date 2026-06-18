import streamlit as st
import base64
from estilos import aplicar_estilos
from dados import carregar_dados
import telas

# Função inteligente para injetar a imagem local no plano de fundo (Base64)
def injetar_wallpaper_local(caminho_imagem):
    try:
        with open(caminho_imagem, "rb") as arquivo:
            dados_imagem = arquivo.read()
        imagem_base64 = base64.b64encode(dados_imagem).decode()
        st.markdown(
            f"""
            <style>
            /* Aplica o wallpaper de estrelas no fundo de toda a página */
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/jpg;base64,{imagem_base64}");
                background-size: cover !important;
                background-position: center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }}
            /* Torna o bloco do meio levemente transparente para o fundo aparecer nas laterais */
            .main {{
                background-color: rgba(11, 13, 28, 0.75) !important; /* Azul escuro translúcido */
                color: #FFFFFF !important;
                padding: 30px !important;
                border-radius: 20px !important;
                box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
            }}
            /* Deixa a barra lateral também combinando com transparência */
            [data-testid="stSidebar"] {{
                background-color: rgba(11, 13, 28, 0.85) !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        pass

# 1. Configuração da Página
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Aplicar os Estilos Gerais do arquivo estilos.py
aplicar_estilos()

# 3. Injetar capa.jpg como o plano de fundo do universo inteiro!
injetar_wallpaper_local("capa.jpg")

# 4. Inicializar Session State
if "historico_carinhos" not in st.session_state:
    st.session_state["historico_carinhos"] = []

# 5. Carregar Dados da Planilha
capa_data, df_elogios, df_missoes = carregar_dados()

# 6. Menu Lateral
st.sidebar.title("🌌 Menu Interativo")
tela_selecionada = st.sidebar.radio(
    "Navegue pelo nosso mundo:",
    ["🌌 Início & Carinho", "🎯 Missões Secretas", "📸 Nosso Diário", "⏳ Nossa Linha do Tempo", "💬 Enviar Carinho"]
)
st.sidebar.markdown("---")
st.sidebar.info("Feito com ❤️ por Denner")

# 7. Roteador de Telas
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
