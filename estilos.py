import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        /* Importa uma fonte de altíssima legibilidade e traços limpos estilo minimalista asiático */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');

        /* Aplica a tipografia limpa sem quebrar as classes nativas do Streamlit */
        html, body, .main, p, .stMarkdown {
            font-family: 'Inter', sans-serif !important;
        }

        /* Caixa de conteúdo centralizada com fundo semi-transparente ideal */
        .main .block-container {
            background-color: rgba(11, 19, 43, 0.75) !important;
            padding: 40px !important;
            border-radius: 20px !important;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5) !important;
            margin-top: 20px !important;
            margin-bottom: 20px !important;
        }

        /* Título Principal - Dourado com sombra marcante para destacar no céu claro */
        h1 { 
            color: #FFD700 !important; 
            text-align: center; 
            font-weight: 700 !important;
            font-size: 2.8rem !important;
            margin-bottom: 15px !important;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.85) !important;
        }

        /* Subtítulos (como o 'Bem-vinda') - Agora em amarelo suave com contorno escuro para leitura perfeita */
        h3 { 
            color: #FFF3B0 !important; 
            text-align: center; 
            font-weight: 400 !important;
            font-size: 1.6rem !important;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.9) !important;
            margin-bottom: 25px !important;
        }

        /* Títulos de Seções (como 'Um carinho para o seu dia') */
        h2 {
            color: #FFD700 !important;
            font-weight: 700 !important;
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.8) !important;
        }
        
        h4 {
            color: #FFD700 !important;
            font-weight: 700 !important;
        }

        /* Textos de ajuda/info que ficam na tela */
        .stMarkdown p {
            color: #FFFFFF !important;
            text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8) !important;
            font-size: 15px !important;
        }

        /* Botão estilizado */
        .stButton>button {
            background-color: #FF4B4B !important; 
            color: white !important; 
            border-radius: 20px !important; 
            width: 100%; 
            font-size: 16px !important;
            font-weight: 700 !important;
            box-shadow: 0px 4px 12px rgba(255, 75, 75, 0.4) !important;
            border: none !important;
            padding: 12px !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton>button:hover {
            background-color: #FF6B6B !important;
            transform: translateY(-2px) !important;
            box-shadow: 0px 6px 15px rgba(255, 75, 75, 0.6) !important;
        }

        /* Cards internos do menu */
        .card {
            background-color: rgba(28, 37, 65, 0.85) !important; 
            padding: 25px !important; 
            border-radius: 15px !important; 
            border-left: 5px solid #FFD700 !important;
            margin-bottom: 20px !important; 
            box-shadow: 0 6px 12px rgba(0,0,0,0.4) !important;
        }

        .missao-concluida { 
            text-decoration: line-through !important; 
            color: #888888 !important; 
        }

        /* Customização fina da caixinha de seleção */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #1C2541 !important;
            color: white !important;
        }

        /* 🎯 APAGA O TEXTO BUGADO DO MENU DE FORMA DEFINITIVA */
        [data-testid="collapsedControl"], 
        [data-testid="collapsedControl"] button,
        [data-testid="collapsedControl"] button * {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            width: 0px !important;
            height: 0px !important;
        }
        </style>
    """, unsafe_allow_html=True)
