import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. Configuração da Página do Aplicativo
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilização Visual Premium e Romântica (Fundo escuro e detalhes em ouro)
st.markdown("""
    <style>
    .main { background-color: #0B132B; color: #FFFFFF; }
    h1 { color: #FFD700; text-align: center; font-family: 'Georgia', serif; }
    h2 { color: #FFD700; font-family: 'Georgia', serif; }
    h3 { color: #E0E1DD; text-align: center; }
    .stButton>button {
        background-color: #FF4B4B; color: white; 
        border-radius: 20px; width: 100%; font-size: 16px;
        box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
        border: none;
        padding: 10px;
    }
    .stButton>button:hover { background-color: #FF7575; color: white; }
    .card {
        background-color: #1C2541; padding: 20px; 
        border-radius: 15px; border-left: 5px solid #FFD700;
        margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .missao-concluida { text-decoration: line-through; color: #888888; }
    </style>
""", unsafe_allow_html=True)

# 2. Conexão Direta com os Dados da Planilha
# IMPORTANTE: Substitua "SEU_ID_DA_PLANILHA" pelo ID real da sua planilha!
ID_PLANILHA = "11_R_3hNyr18YPPdHzM58iEKxG7_uorm0TBaHIeg36F8"

@st.cache_data(ttl=15)
def carregar_dados():
    try:
        # Puxa cada aba de forma direta e sem quebras de linha que causam erro
        df_capa = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=0")
        df_elogios = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=123456")
        df_missoes = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=789101")
        return df_capa, df_elogios, df_missoes
    except Exception:
        # Backup caso o ID da planilha ainda não esteja configurado
        df_capa = pd.DataFrame([{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}])
        df_elogios = pd.DataFrame([{"Frase": "Você é o meu momento favorito do dia!"}, {"Frase": "Seu sorriso ilumina meu mundo."}])
        df_missoes = pd.DataFrame([
            {"ID": 1, "Titulo": "Cozinhar algo juntos", "Tipo_Missao": "Média", "Status": "Pendente", "Gif": "comida.gif"},
            {"ID": 2, "Titulo": "Assistir um filme cobertos", "Tipo_Missao": "Fácil", "Status": "Concluída", "Gif": "coberta.gif"}
        ])
        return df_capa, df_elogios, df_missoes

df_capa, df_elogios, df_missoes = carregar_dados()


# 3. MENU LATERAL DE NAVEGAÇÃO
st.sidebar.title("🌌 Menu Interativo")
tela_selecionada = st.sidebar.radio(
    "Navegue pelo nosso mundo:",
    ["🌌 Início & Carinho", "🎯 Missões Secretas", "📸 Nosso Diário", "💬 Enviar Carinho"]
)
st.sidebar.markdown("---")
st.sidebar.info("Feito com ❤️ por Denner")


# ==========================================
# TELA 1: INÍCIO & CARINHO
# ==========================================
if tela_selecionada == "🌌 Início & Carinho":
    try:
        st.image("capa.jpg", use_container_width=True)
    except:
        st.warning("🌌 Carregando imagem de capa...")
    
    st.title(f"✨ {df_capa['Titulo_App'].iloc[0]} ✨")
    st.markdown(f"<h3>{df_capa['Subtitulo_App'].iloc[0]}</h3>", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("❤️ Um carinho para o seu dia")
    if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
        frase_sorteada = random.choice(df_elogios['Frase'].tolist())
        st.balloons() 
        st.markdown(f"<div class='card' style='text-align: center; font-size: 20px; font-style: italic;'>\"{frase_sorteada}\"</div>", unsafe_allow_html=True)
    else:
        st.info("Clique no botão acima para receber sua dose diária de amor!")


# ==========================================
# TELA 2: MISSÕES SECRETAS
# ==========================================
elif tela_selecionada == "🎯 Missões Secretas":
    st.title("🎯 Nossas Missões Românticas")
    st.write("Aqui estão os nossos desafios! Clique no botão de cada uma para ver uma surpresa animada:")
    st.markdown("---")

    for index, row in df_missoes.iterrows():
        status_icon = "✅" if row['Status'] == "Concluída" else "⏳"
        classe_texto = "missao-concluida" if row['Status'] == "Concluída" else ""
        
        st.markdown(f"""
            <div class='card'>
                <span style='float: right; background: #FF4B4B; padding: 2px 8px; border-radius: 10px; font-size: 12px;'>{row['Tipo_Missao']}</span>
                <h4 class='{classe_texto}'>{status_icon} {row['Titulo']}</h4>
                <p style='font-size: 13px; color: #aaa; margin-bottom: 0px;'>Status: {row['Status']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🔍 Ver Surpresa: {row['Titulo']}", key=f"btn_{row['ID']}"):
            st.write(f"**Nível:** Essa missão é considerada *{row['Tipo_Missao']}*. Vamos cumprir juntos?")
            nome_gif = str(row['Gif']).strip()
            try:
                st.image(nome_gif, caption="Nosso Momento!", use_container_width=True)
            except Exception:
                try:
                    st.image(nome_gif.lower(), caption="Nosso Momento!", use_container_width=True)
                except Exception:
                    st.error(f"🎬 O arquivo '{nome_gif}' não foi localizado no repositório.")
        st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# TELA 3: NOSSO DIÁRIO / MEMÓRIAS
# ==========================================
elif tela_selecionada == "📸 Nosso Diário":
    st.title("📸 Nosso Diário de Memórias")
    st.markdown("---")
    
    st.subheader("🌹 O Princípio de Tudo")
    st.write("“Tu te tornas eternamente responsável por aquilo que cativas.”")
    
    try:
        st.image("tela de carregamento.jpg", caption="
