import streamlit as st
import pandas as pd
import random
import time

# 1. Configuração da Página e Tema
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS para deixar o visual Premium e Romântico
st.markdown("""
    <style>
    .main { background-color: #0B132B; color: #FFFFFF; }
    h1 { color: #FFD700; text-align: center; font-family: 'Georgia', serif; }
    h3 { color: #E0E1DD; text-align: center; }
    .stButton>button {
        background-color: #FF4B4B; color: white; 
        border-radius: 20px; width: 100%; font-size: 18px;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
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

# 2. Conexão com o Google Sheets (Puxando os dados reais)
# Substitua pelo URL da sua planilha que está configurada como "Qualquer pessoa com o link pode ler"
SHEET_URL = "https://docs.google.com/spreadsheets/d/SEU_ID_DA_PLANILHA/export?format=csv"

@st.cache_data(ttl=60)  # Atualiza os dados a cada 1 minuto
def carregar_dados():
    try:
        # Puxa as abas da planilha (ajuste os nomes se necessário)
        df_capa = pd.read_csv(f"{SHEET_URL}&gid=0") # Gid da aba Capa
        df_elogios = pd.read_csv(f"{SHEET_URL}&gid=123456") # Gid da aba Elogios
        df_missoes = pd.read_csv(f"{SHEET_URL}&gid=789101") # Gid da aba Missões
        return df_capa, df_elogios, df_missoes
    except:
        # Dados de backup caso a planilha falhe ao carregar
        df_capa = pd.DataFrame([{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}])
        df_elogios = pd.DataFrame([{"Frase": "Você é o meu momento favorito do dia!"}, {"Frase": "Seu sorriso ilumina meu mundo."}])
        df_missoes = pd.DataFrame([{"Titulo": "Cozinhar algo juntos", "Tipo_Missao": "Média", "Status": "Pendente"}])
        return df_capa, df_elogios, df_missoes

df_capa, df_elogios, df_missoes = carregar_dados()

# 3. CONSTRUÇÃO DA TELA (DESIGN)

# Banner do Pequeno Príncipe (Usando a imagem da sua pasta local ou link)
# Se não subir a imagem no GitHub, você pode trocar a linha abaixo por um link de imagem direto.
try:
    st.image("Imagens/capa.jpg", use_column_width=True)
except:
    pass # Ignora se não achar a imagem por enquanto

# Títulos
st.title(f"✨ {df_capa['Titulo_App'].iloc[0]} ✨")
st.markdown(f"<h3>{df_capa['Subtitulo_App'].iloc[0]}</h3>", unsafe_allow_html=True)
st.markdown("---")

# Seção 1: O Botão Mágico (Sorteador de Elogios)
st.subheader("❤️ Um carinho para o seu dia")

if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
    # Escolhe uma frase aleatória pura via código Python
    frase_sorteada = random.choice(df_elogios['Frase'].tolist())
    st.balloons() # Efeito visual lindo de balões subindo na tela!
    st.markdown(f"<div class='card' style='text-align: center; font-size: 20px; font-style: italic;'>\"{frase_sorteada}\"</div>", unsafe_allow_html=True)
else:
    st.info("Clique no botão acima para ler o elogio do momento!")

st.markdown("---")

# Seção 2: Missões Românticas da Sara
st.subheader("🎯 Missões do Amor")

for index, row in df_missoes.iterrows():
    status_icon = "✅" if row['Status'] == "Concluída" else "⏳"
    classe_texto = "missao-concluida" if row['Status'] == "Concluída" else ""
    
    # Renderiza cada missão dentro de um Card customizado estilizado
    st.markdown(f"""
        <div class='card'>
            <span style='float: right; background: #FF4B4B; padding: 2px 8px; border-radius: 10px; font-size: 12px;'>{row['Tipo_Missao']}</span>
            <h4 class='{classe_texto}'>{status_icon} {row['Titulo']}</h4>
        </div>
    """, unsafe_allow_html=True)
