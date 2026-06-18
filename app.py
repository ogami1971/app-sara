import streamlit as st
import base64
from estilos import aplicar_estilos
from dados import carregar_dados, carregar_progresso_banco
import telas
import notificacoes

# 🌟 IMPORT DOS NOSSOS MÓDULOS SEPARADOS
import rpg
import roleta
import contador

# 🌟 CONFIGURAÇÃO ÚNICA DA PÁGINA (A primeira linha executável do app!)
st.set_page_config(
    page_title="Universo de Amor", 
    page_icon="🌹", 
    layout="wide",
    initial_sidebar_state="expanded"
)

def injetar_wallpaper_dinamico():
    temas_arquivos = {
        "pequeno_principe": "Wallpaper.jpg",       
        "shigatsu": "shigatsu.jpg",               
        "demon_slayer": "demon_slayer.jpg",           
        "arcane": "arcane.jpg",                 
        "padrao": "Wallpaper.jpg"                  
    }
    tema_atual = st.session_state.get("tema_fundo", "padrao")
    arquivo_imagem = temas_arquivos.get(tema_atual, "Wallpaper.jpg")
    try:
        with open(arquivo_imagem, "rb") as arquivo:
            dados_imagem = arquivo.read()
        imagem_base64 = base64.b64encode(dados_imagem).decode()
        st.markdown(
            f"""
            <style>
            .stAppViewMain, [data-testid="stAppViewContainer"], .stApp {{
                background-image: url("data:image/jpg;base64,{imagem_base64}") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
                transition: background-image 0.6s ease-in-out !important;
            }}
            [data-testid="stApp"] {{ background: transparent !important; }}
            [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {{
                background-color: rgba(20, 27, 48, 0.9) !important;
            }}
            
            /* Esconde o bloco de texto bugado do topo */
            [data-testid="stHeader"] {{
                background-color: transparent !important;
            }}
            [data-testid="stHeader"]::before {{
                content: "" !important;
                display: none !important;
            }}
            h1 a, h2 a, h3 a {{
                display: none !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        pass

if "tema_fundo" not in st.session_state:
    st.session_state["tema_fundo"] = "padrao"
if "historico_carinhos" not in st.session_state:
    st.session_state["historico_carinhos"] = []

try:
    aplicar_estilos()
except Exception:
    pass
injetar_wallpaper_dinamico()

# 🌟 CARREGA DADOS ESTÁTICOS E DA O START NO BANCO DE PROGRESSO DA SARA
capa_data, df_elogios, df_missoes = carregar_dados()
carregar_progresso_banco()

# Verifica automaticamente as notificações por e-mail com o Zapier ao abrir o app
try:
    notificacoes.verificar_datas_comemorativas()
except Exception:
    pass

# 🪐 MENU LATERAL EXPANDIDO COM AS NOVAS OPÇÕES MODULARES
st.sidebar.title("🌌 Menu Interativo")
tela_selecionada = st.sidebar.radio(
    "Navegue pelo nosso mundo:",
    [
        "🌌 Início & Carinho", 
        "🎯 Missões Secretas", 
        "⚔️ Nossa Jornada RPG",
        "🎰 Máquina de Cupons",
        "🎯 Central de Conquistas",  # 🌟 Adicionado!
        "🎲 Roleta de Rolês",    
        "⏳ Tempo Juntos",       
        "💬 Enviar Carinho"
    ]
)
st.sidebar.markdown("### 🎵 Trilha Sonora")

# 🌟 Link do YouTube configurado (Your Name Acústico)
id_video_youtube = "7j60jaMapJ0" 

# Cria o player do YouTube em miniatura dentro do menu lateral
st.sidebar.markdown(
    f"""
    <iframe width="100%" height="180" 
        src="https://www.youtube.com/embed/{id_video_youtube}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen style="border-radius: 10px; margin-bottom: 10px;">
    </iframe>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown("---")

# 🛣️ ROTEADOR DIRECIONANDO PARA AS TELAS CORRETAS
if tela_selecionada == "🌌 Início & Carinho":
    telas.exibir_inicio(capa_data, df_elogios)
elif tela_selecionada == "🎯 Missões Secretas":
    telas.exibir_missoes(df_missoes)
elif tela_selecionada == "⚔️ Nossa Jornada RPG":
    rpg.exibir_rpg()
elif tela_selecionada == "🎰 Máquina de Cupons":
    telas.exibir_maquina_cupons()
elif tela_selecionada == "🎯 Central de Conquistas":
    telas.exibir_central_conquistas()
elif tela_selecionada == "🎰 Roleta de Rolês":
    roleta.exibir_roleta()
elif tela_selecionada == "⏳ Tempo Juntos":
    contador.exibir_contador()
elif tela_selecionada == "💬 Enviar Carinho":
    telas.exibir_enviar_carinho()
