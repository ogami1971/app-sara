import streamlit as st
import base64
from estilos import aplicar_estilos
from dados import carregar_dados
import telas

# Função para converter e injetar o fundo com base no tema ativo
def injetar_wallpaper_dinamico():
    # Mapeamento oficial dos arquivos que você baixou e subiu no GitHub
    temas_arquivos = {
        "pequeno_principe": "Wallpaper.jpg",       
        "shigatsu": "shigatsu.jpg",               
        "demon_slayer": "demon_slayer.jpg",           
        "arcane": "arcane.jpg",                 
        "padrao": "Wallpaper.jpg"                  
    }
    
    # Recupera o tema da sessão atual (se não houver, usa o padrão)
    tema_atual = st.session_state.get("tema_fundo", "padrao")
    arquivo_imagem = temas_arquivos.get(tema_atual, "Wallpaper.jpg")
    
    try:
        with open(arquivo_imagem, "rb") as arquivo:
            dados_imagem = arquivo.read()
        imagem_base64 = base64.b64encode(dados_imagem).decode()
        
        st.markdown(
            f"""
            <style>
            /* Alvo absoluto para envelopar o fundo do app */
            .stAppViewMain, [data-testid="stAppViewContainer"], .stApp {{
                background-image: url("data:image/jpg;base64,{imagem_base64}") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
                transition: background-image 0.6s ease-in-out !important; /* Efeito de transição suave */
            }}
            [data-testid="stApp"] {{ background: transparent !important; }}
            [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {{
                background-color: rgba(20, 27, 48, 0.9) !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        pass

# 1. Configuração de Página
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Inicializar variáveis de estado na memória
if "tema_fundo" not in st.session_state:
    st.session_state["tema_fundo"] = "padrao"

if "historico_carinhos" not in st.session_state:
    st.session_state["historico_carinhos"] = []

# 3. Aplicar Estilização Geral e Wallpaper Ativo
try:
    aplicar_estilos()
except Exception:
    pass
injetar_wallpaper_dinamico()

# 4. Carregar Dados Estruturados
capa_data, df_elogios, df_missoes = carregar_dados()

# 5. Menu de Navegação Lateral
st.sidebar.title("🌌 Menu Interativo")
tela_selecionada = st.sidebar.radio(
    "Navegue pelo nosso mundo:",
    ["🌌 Início & Carinho", "🎯 Missões Secretas", "📸 Nosso Diário", "⏳ Nossa Linha do Tempo", "💬 Enviar Carinho"]
)
st.sidebar.markdown("---")
st.sidebar.info("Feito com ❤️ por Denner")

# 6. Roteamento de Visualização
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
