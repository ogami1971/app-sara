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
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/jpg;base64,{imagem_base64}");
                background-size: cover !important;
                background-position: center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }}
            /* Torna o fundo do conteúdo ligeiramente transparente para mostrar o wallpaper nas laterais */
            .main {{
                background-color: rgba(11, 19, 43, 0.8) !important;
                color: #FFFFFF !important;
                padding: 30px !important;
                border-radius: 20px !important;
            }}
            /* Deixa a barra lateral combinando */
            [data-testid="stSidebar"] {{
                background-color: rgba(11, 19, 43, 0.9) !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        # Caso a imagem falhe por algum motivo, não trava o app
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

# 3. Injetar o Wallpaper de Fundo usando o arquivo correto do seu GitHub
injetar_wallpaper_local("Wallpaper.jpg")

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
