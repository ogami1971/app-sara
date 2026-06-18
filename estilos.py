import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        /* Define o Wallpaper de Fundo Interativo para todo o App */
        [data-testid="stAppViewContainer"] {
            background-image: url("Wallpaper.jpg"); /* Nome exato do seu arquivo */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        /* Torna o container principal levemente translúcido para o fundo aparecer nos lados */
        .main { 
            background-color: rgba(11, 19, 43, 0.85); /* Mantém o azul escuro, mas com 85% de opacidade */
            color: #FFFFFF; 
            padding: 30px;
            border-radius: 20px;
        }

        /* Garante que o menu lateral combine com o fundo se necessário */
        [data-testid="stSidebar"] {
            background-color: rgba(28, 37, 65, 0.95) !important;
        }

        h1 { 
            color: #FFD700; 
            text-align: center; 
            font-family: 'Georgia', serif; 
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.5);
        }
        h2, h4 { 
            color: #FFD700; 
            font-family: 'Georgia', serif; 
        }
        h3 { 
            color: #E0E1DD; 
            text-align: center; 
            font-family: 'Georgia', serif;
            font-weight: 300;
        }
        .stButton>button {
            background-color: #FF4B4B; 
            color: white; 
            border-radius: 20px; 
            width: 100%; 
            font-size: 16px;
            font-weight: bold;
            box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
            border: none;
            padding: 12px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover { 
            background-color: #FF7575; 
            color: white; 
            transform: translateY(-2px);
            box-shadow: 0px 6px 15px rgba(255, 117, 117, 0.4);
        }
        .card {
            background-color: #1C2541; 
            padding: 25px; 
            border-radius: 15px; 
            border-left: 5px solid #FFD700;
            margin-bottom: 20px; 
            box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        }
        .missao-concluida { 
            text-decoration: line-through; 
            color: #888888; 
        }
        .stSelectbox div[data-baseweb="select"] {
            background-color: #1C2541 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
