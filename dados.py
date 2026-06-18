import streamlit as st
import csv
import urllib.request

ID_PLANILHA = "11_R_3hNyr18YPPdHzM58iEKxG7_uorm0TBaHIeg36F8"

@st.cache_data(ttl=15)
def ler_aba_csv(url):
    try:
        resposta = urllib.request.urlopen(url)
        linhas = [linha.decode('utf-8') for list_linha in [resposta.read().splitlines()] for linha in list_linha]
        leitor = csv.DictReader(linhas)
        return list(leitor)
    except Exception:
        return []

def carregar_dados():
    capa = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=0")
    # Tenta ler a aba de elogios da planilha
    elogios_planilha = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=123456")
    missoes = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=789101")
    
    # Lista de 25 Elogios Personalizados (Caso a planilha esteja vazia ou falhe)
    elogios_customizados = [
        # O Pequeno Príncipe
        {"Frase": "Você é a minha rosa única no mundo, aquela pela qual sou eternamente responsável por cativar e proteger. 🌹"},
        {"Frase": "No meio de bilhões de estrelas no céu, o meu olhar sempre escolhe você para admirar. 🌌"},
        {"Frase": "Seu sorriso faz o meu deserto florescer por completo. ✨"},
        {"Frase": "O essencial é invisível aos olhos, mas o meu coração enxerga perfeitamente a perfeição que você é. ❤️"},
        {"Frase": "Se você vier, por exemplo, às quatro da tarde, desde as três eu começarei a ser feliz! 🦊"},
        {"Frase": "Você não é apenas uma pessoa comum em um planeta qualquer, você é o meu universo inteiro."},
        
        # Shigatsu wa Kimi no Uso (Your Lie in April)
        {"Frase": "Assim como a Kaori trouxe cor ao mundo do Kousei, você trouxe toda a música e cor para a minha vida. 🎹🎻"},
        {"Frase": "Sua presença em meu dia é como um solo de violino inesquecível: vibrante, linda e cheia de alma."},
        {"Frase": "Seja na primavera ou em qualquer outra estação, você é a melodia mais bonita que meu coração já tocou. 🌸"},
        {"Frase": "Basta um olhar seu para que todas as cores do meu mundo fiquem mais vivas e brilhantes."},
        {"Frase": "Você é a minha sinfonia perfeita, o motivo pelo qual eu continuo querendo ouvir o som do amanhã. 🎵"},
        {"Frase": "Mesmo nos dias mais cinzentos, lembrar de você me faz querer tocar a nossa música eterna."},
        
        # Kimetsu no Yaiba (Demon Slayer)
        {"Frase": "Meu desejo de te proteger e ficar ao seu lado é mais forte do que qualquer Respiração de Concentração Total! ⚔️"},
        {"Frase": "Sua doçura e força me lembram que, não importa a escuridão lá fora, você sempre será a minha luz."},
        {"Frase": "Seu sorriso tem o poder de curar qualquer cansaço, como se eu estivesse na Mansão Borboleta. 🦋"},
        {"Frase": "Se eu tivesse que enfrentar mil luas superiores apenas para te ver sorrir, eu faria sem hesitar! 🔥"},
        {"Frase": "Você tem a pureza do Tanjiro e o poder de iluminar tudo ao seu redor como as chamas do Rengoku."},
        {"Frase": "O laço que nos une é inquebrável, nem mesmo a espada mais forte seria capaz de cortar o que sinto por você."},
        
        # Arcane
        {"Frase": "Em um mundo cheio de caos como Zaun e Piltover, você é a minha única certeza e o meu porto seguro. ⚙️⚡"},
        {"Frase": "Você tem uma força brilhante e uma essência tão única que nem mesmo o Hextec conseguiria replicar. 💎"},
        {"Frase": "Eu atravessaria pontes, enfrentaria exércitos e mudaria o mundo inteiro só para garantir o seu sorriso."},
        {"Frase": "Você é perfeita exatamente do jeito que você é, com cada detalhe único que te faz ser a minha pessoa favorita. ⚡"},
        {"Frase": "Nossa conexão faísca mais forte do que qualquer energia pura. Você me inspira todos os dias."},
        
        # Misturas Especiais
        {"Frase": "Você é a rosa do meu asteroide, a melodia da minha primavera e a força que me faz querer lutar todos os dias. 🌹🎻⚔️"},
        {"Frase": "Nem toda a tecnologia de Piltover ou as magias do mundo conseguiriam explicar o milagre que é ter você na minha vida. ✨"}
    ]
    
    # Se a planilha não trouxer dados válidos, usamos os nossos 25 elogios incríveis
    if not elogios_planilha:
        elogios = elogios_customizados
    else:
        elogios = elogios_planilha

    if not capa: 
        capa = [{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}]
    if not missoes: 
        missoes = [
            {"ID": "1", "Titulo": "Cozinhar algo juntos", "Tipo_Missao": "Média", "Status": "Pendente", "Gif": "comida.gif"},
            {"ID": "2", "Titulo": "Assistir um filme cobertos", "Tipo_Missao": "Fácil", "Status": "Concluída", "Gif": "coberta.gif"}
        ]
        
    return capa[0], elogios, missoes
