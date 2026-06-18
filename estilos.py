import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        /* Caixa de conteúdo centralizada e legível */
        .main .block-container {
            background-color: rgba(11, 19, 43, 0.82) !important;
            padding: 40px !important;
            border-radius: 20px !important;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.6) !important;
            margin-top: 20px !important;
            margin-bottom: 20px !important;
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
            font-family: 'Georgia', serif; 
        }
        h3 { 
            color: #E0E1DD !important; 
            text-align: center; 
            font-family: 'Georgia', serif;
            font-weight: 300;
        }
        .stButton>button {
            background-color: #FF4B4B !important; 
            color: white !important; 
            border-radius: 20px !important; 
            width: 100%; 
            font-size: 16px;
            font-weight: bold;
            box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
            border: none;
            padding: 12px;
            transition: all 0.3s ease;
        }
        .card {
            background-color: #1C2541 !important; 
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
