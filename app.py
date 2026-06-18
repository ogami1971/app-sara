import streamlit as st
import base64
from estilos import aplicar_estilos
from dados import carregar_dados
import telas

# Função com seletor absoluto que transforma a imagem local em wallpaper real
def injetar_wallpaper_completo(caminho_imagem):
    try:
        with open(caminho_imagem, "rb") as arquivo:
            dados_imagem = arquivo.read()
        imagem_base64 = base64.b64encode(dados_imagem).decode()
        
        st.markdown(
            f"""
            <style>
            /* Alvo absoluto no painel principal e contêiner global */
            .stAppViewMain, [data-testid="stAppViewContainer"], .stApp {{
                background-image: url("data:image/jpg;base64,{imagem_base64}") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }}
            
            /* Limpa obstruções visuais secundárias */
            [data-testid="stApp"] {{
                background: transparent !important;
            }}

            /* Customiza a barra lateral para ficar em sintonia */
            [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {{
                background-color: rgba(20, 27, 48, 0.9) !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Erro ao carregar o fundo: {e}")

# 1. Configuração da Página
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Aplicar os Estilos Gerais
try:
    aplicar_estilos()
except Exception:
    pass

# 3. Forçar a injeção do Wallpaper.jpg de ponta a ponta na tela
injetar_wallpaper_completo("Wallpaper.jpg")

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
