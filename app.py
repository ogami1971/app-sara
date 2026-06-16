import streamlit as st
import pandas as pd
import random

# 1. Configuração da Página
st.set_page_config(
    page_title="App Pequeno Príncipe - Sara",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="expanded" # Deixa o menu lateral visível para navegação
)

# Estilização CSS Premium e Romântica
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

# 2. Conexão com os Dados da Planilha
SHEET_URL = "https://docs.google.com/spreadsheets/d/SEU_ID_DA_PLANILHA/export?format=csv"

@st.cache_data(ttl=30) # Atualiza rápido para quando mudar o status na planilha
def carregar_dados():
    try:
        df_capa = pd.read_csv(f"{SHEET_URL}&gid=0")
        df_elogios = pd.read_csv(f"{SHEET_URL}&gid=123456")
        df_missoes = pd.read_csv(f"{SHEET_URL}&gid=789101")
        return df_capa, df_elogios, df_missoes
    except:
        df_capa = pd.DataFrame([{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}])
        df_elogios = pd.DataFrame([{"Frase": "Você é o meu momento favorito do dia!"}, {"Frase": "Seu sorriso ilumina meu mundo."}])
        df_missoes = pd.DataFrame([
            {"ID": 1, "Titulo": "Cozinhar algo juntos", "Tipo_Missao": "Média", "Status": "Pendente", "Gif": "comida.gif"},
            {"ID": 2, "Titulo": "Assistir um filme cobertos", "Tipo_Missao": "Fácil", "Status": "Concluída", "Gif": "coberta.gif"}
        ])
        return df_capa, df_elogios, df_missoes

df_capa, df_elogios, df_missoes = carregar_dados()


# 3. MENU LATERAL DE NAVEGAÇÃO (As Telas do App)
st.sidebar.title("🌌 Navegação")
st.sidebar.markdown("Escolha o canto do nosso universo que deseja visitar:")
tela_selecionada = st.sidebar.radio(
    "Ir para:",
    ["🌌 Início & Carinho", "🎯 Missões Secretas", "📸 Nosso Diário"]
)

st.sidebar.markdown("---")
st.sidebar.info("Feito com ❤️ por Denner")


# ==========================================
# TELA 1: INÍCIO & CARINHO
# ==========================================
if tela_selecionada == "🌌 Início & Carinho":
    # Banner Principal do Pequeno Príncipe (Links diretos funcionam melhor se a imagem sumir)
    st.image("Imagens/Pequeno Príncipe.jpg", use_column_width=True)
    
    st.title(f"✨ {df_capa['Titulo_App'].iloc[0]} ✨")
    st.markdown(f"<h3>{df_capa['Subtitulo_App'].iloc[0]}</h3>", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("❤️ Um carinho para o seu dia")
    if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
        frase_sorteada = random.choice(df_elogios['Frase'].tolist())
        st.balloons()
        st.markdown(f"<div class='card' style='text-align: center; font-size: 20px; font-style: italic;'>\"{frase_sorteada}\"</div>", unsafe_allow_html=True)
    else:
        st.info("Clique no botão acima para ler o elogio do momento!")


# ==========================================
# TELA 2: MISSÕES SECRETAS (COM BOTÕES!)
# ==========================================
elif tela_selecionada == "🎯 Missões Secretas":
    st.title("🎯 Nossas Missões Românticas")
    st.write("Cumpra as missões com o seu namorado e clique nelas para liberar as surpresas!")
    st.markdown("---")

    for index, row in df_missoes.iterrows():
        status_icon = "✅" if row['Status'] == "Concluída" else "⏳"
        classe_texto = "missao-concluida" if row['Status'] == "Concluída" else ""
        
        # Estrutura visual da missão
        st.markdown(f"""
            <div class='card'>
                <span style='float: right; background: #FF4B4B; padding: 2px 8px; border-radius: 10px; font-size: 12px;'>{row['Tipo_Missao']}</span>
                <h4 class='{classe_texto}'>{status_icon} {row['Titulo']}</h4>
                <p style='font-size: 13px; color: #aaa;'>Status Atual: {row['Status']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # O BOTÃO REAL: Ao clicar, ele abre detalhes ou o GIF correspondente da missão!
        # Criamos uma chave única com o ID da missão para o Streamlit não se perder
        if st.button(f"🔍 Abrir Detalhes da Missão: {row['Titulo']}", key=f"btn_{row['ID']}"):
            st.write(f"**Detalhes:** Esta missão é considerada *{row['Tipo_Missao']}*. Vamos fazer acontecer?")
            
            # Tenta carregar o GIF da pasta Imagens correspondente ao nome que está na planilha
            try:
                st.image(f"Imagens/{row['Gif']}", caption="Nosso momento!", use_column_width=True)
            except:
                st.warning("GIF correspondente ainda sendo carregado no servidor!")
        st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# TELA 3: NOSSO DIÁRIO / MEMÓRIAS
# ==========================================
elif tela_selecionada == "📸 Nosso Diário":
    st.title("📸 Nosso Diário de Memórias")
    st.write("Um espaço para guardar as lembranças mais bonitas do que já vivemos.")
    st.markdown("---")
    
    # Aqui você pode colocar fotos fixas de vocês ou mensagens especiais cronológicas
    st.subheader("🌹 O Início de Tudo")
    st.write("“Tu te tornas eternamente responsável por aquilo que cativas.”")
    
    try:
        st.image("Imagens/tela de carregamento.jpg", caption="Onde nosso universo começou...", use_column_width=True)
    except:
        st.info("Aqui ficarão as fotos mais lindas da sua galeria!")
