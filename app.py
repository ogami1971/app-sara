import streamlit as st
import random
import csv
import urllib.request
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

# 2. Conexão Nativa com os Dados da Planilha (Evita erros de compilação)
# IMPORTANTE: Substitua "SEU_ID_DA_PLANILHA" pelo ID real da sua planilha!
ID_PLANILHA = "SEU_ID_DA_PLANILHA"

@st.cache_data(ttl=15)
def ler_aba_csv(url):
    try:
        resposta = urllib.request.urlopen(url)
        linhas = [linha.decode('utf-8') for list_linha in [resposta.read().splitlines()] for linha in list_linha]
        leitor = csv.DictReader(linhas)
        return list(leitor)
    except:
        return []

def carregar_dados():
    capa = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=0")
    elogios = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=123456")
    missoes = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=789101")
    
    # Backups de segurança caso a planilha ainda não esteja mapeada com o ID correto
    if not capa: capa = [{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}]
    if not elogios: elogios = [{"Frase": "Você é o meu momento favorito do dia!"}, {"Frase": "Seu sorriso ilumina meu mundo."}]
    if not missoes: missoes = [
        {"ID": "1", "Titulo": "Cozinhar algo juntos", "Tipo_Missao": "Média", "Status": "Pendente", "Gif": "comida.gif"},
        {"ID": "2", "Titulo": "Assistir um filme cobertos", "Tipo_Missao": "Fácil", "Status": "Concluída", "Gif": "coberta.gif"}
    ]
    return capa[0], elogios, missoes

capa_data, df_elogios, df_missoes = carregar_dados()


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
    
    st.title(f"✨ {capa_data.get('Titulo_App', 'Nosso Universo')} ✨")
    st.markdown(f"<h3>{capa_data.get('Subtitulo_App', 'Bem-vinda')}</h3>", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("❤️ Um carinho para o seu dia")
    if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
        frases = [item['Frase'] for item in df_elogios if 'Frase' in item]
        frase_sorteada = random.choice(frases) if frases else "Você é especial!"
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

    for row in df_missoes:
        status_icon = "✅" if row.get('Status') == "Concluída" else "⏳"
        classe_texto = "missao-concluida" if row.get('Status') == "Concluída" else ""
        
        st.markdown(f"""
            <div class='card'>
                <span style='float: right; background: #FF4B4B; padding: 2px 8px; border-radius: 10px; font-size: 12px;'>{row.get('Tipo_Missao', 'Normal')}</span>
                <h4 class='{classe_texto}'>{status_icon} {row.get('Titulo', 'Missão')}</h4>
                <p style='font-size: 13px; color: #aaa; margin-bottom: 0px;'>Status: {row.get('Status', 'Pendente')}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🔍 Ver Surpresa: {row.get('Titulo')}", key=f"btn_{row.get('ID')}"):
            st.write(f"**Nível:** Essa missão é considerada *{row.get('Tipo_Missao')}*. Vamos cumprir juntos?")
            nome_gif = str(row.get('Gif', '')).strip()
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
        st.image("tela de carregamento.jpg", caption="Onde o nosso universo começou...", use_container_width=True)
    except:
        st.info("📸 Preparando nosso mural de fotos...")
        
    st.markdown("---")
    st.subheader("✨ Nossa Sintonia")
    try:
        st.image("rosa.gif", caption="Você é única no mundo para mim.", use_container_width=True)
    except:
        pass


# ==========================================
# TELA 4: ENVIAR CARINHO 
# ==========================================
elif tela_selecionada == "💬 Enviar Carinho":
    st.title("💬 Deixe um Recadinho para o Denner")
    st.write("Escolha uma reação e escreva algo fofo!")
    st.markdown("---")
    
    st.subheader("1. Como você está se sentindo agora?")
    reacao_escolhida = st.selectbox(
        "Selecione uma reação:",
        ["Selecione...", "Carinhosa (Rosa)", "Com saudades (Raposa)", "Manhosa (Mirra)", "Brava (Bravinha)", "Divertida (Língua)"]
    )
    
    mapeamento_gifs = {
        "Carinhosa (Rosa)": "rosa.gif",
        "Com saudades (Raposa)": "raposa.gif",
        "Manhosa (Mirra)": "Gato fazendo mirra.gif",
        "Brava (Bravinha)": "brava.gif",
