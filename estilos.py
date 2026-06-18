import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        /* Alvo direto no container de fundo do Streamlit Cloud */
        .stApp {
            background-image: url("app/static/Wallpaper.jpg") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }
        
        /* Caso o de cima falhe por conta da pasta static, tenta esse também */
        [data-testid="stAppViewContainer"] {
            background-image: url("app/static/Wallpaper.jpg") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }

        .main { 
            background-color: rgba(11, 19, 43, 0.85) !important;
            color: #FFFFFF !important; 
            padding: 30px !important;
            border-radius: 20px !important;
        }

        [data-testid="stSidebar"] {
            background-color: rgba(28, 37, 65, 0.95) !important;
        }

        h1 { 
            color: #FFD700 !important; 
            text-align: center; 
            font-family: 'Georgia', serif; 
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.5);
        }
        h2, h4 { 
            color: #FFD700 !important; 
        }
        h3 { 
            color: #E0E1DD !important; 
        }
        .stButton>button {
            background-color: #FF4B4B !important; 
            color: white !important; 
            border-radius: 20px !important; 
        }
        .card {
            background-color: #1C2541 !important; 
            padding: 25px; 
            border-radius: 15px; 
            border-left: 5px solid #FFD700;
            margin-bottom: 20px; 
        }
        .stSelectbox div[data-baseweb="select"] {
            background-color: #1C2541 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
