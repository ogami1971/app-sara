import streamlit as st
import csv
import urllib.request
from datetime import datetime

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
    
    # 25 Elogios Automatizados fixos
    elogios_customizados = [
        {"Frase": "Você é a minha rosa única no mundo, aquela pela qual sou eternamente responsável por cativar e proteger. 🌹"},
        {"Frase": "No meio de bilhões de estrelas no céu, o meu olhar sempre escolhe você para admirar. 🌌"},
        {"Frase": "Seu sorriso faz o meu deserto florescer por completo. ✨"},
        {"Frase": "O essencial é invisível aos olhos, mas o meu coração enxerga perfeitamente a perfeição que você é. ❤️"},
        {"Frase": "Se você vier, por exemplo, às quatro da tarde, desde as três eu começarei a ser feliz! 🦊"},
        {"Frase": "Você não é apenas uma pessoa comum em um planeta qualquer, você é o meu universo inteiro."},
        {"Frase": "Assim como a Kaori trouxe cor ao mundo do Kousei, você trouxe toda a música e cor para a minha vida. 🎹🎻"},
        {"Frase": "Sua presença em meu dia é como um solo de violino inesquecível: vibrante, linda e cheia de alma."},
        {"Frase": "Seja na primavera ou em qualquer outra estação, você é a melodia mais bonita que meu coração já tocou. 🌸"},
        {"Frase": "Basta um olhar seu para que todas as cores do meu mundo fiquem mais vivas e brilhantes."},
        {"Frase": "Você é a minha sinfonia perfeita, o motivo pelo qual eu continuo querendo ouvir o som do amanhã. 🎵"},
        {"Frase": "Mesmo nos dias mais cinzentos, lembrar de você me faz querer tocar a nossa música eterna."},
        {"Frase": "Meu desejo de te proteger e ficar ao seu lado é mais forte do que qualquer Respiração de Concentração Total! ⚔️"},
        {"Frase": "Sua doçura e força me lembram que, não importa a escuridão lá fora, você sempre será a minha luz."},
        {"Frase": "Seu sorriso tem o poder de curar qualquer cansaço, como se eu estivesse na Mansão Borboleta. 🦋"},
        {"Frase": "Se eu tivesse que enfrentar mil luas superiores apenas para te ver sorrir, eu faria sem hesitar! 🔥"},
        {"Frase": "Você tem a pureza do Tanjiro e o poder de iluminar tudo ao seu redor como as chamas do Rengoku."},
        {"Frase": "O laço que nos une é inquebrável, nem mesmo a espada mais forte seria capaz de cortar o que sinto por você."},
        {"Frase": "Em um mundo cheio de caos como Zaun e Piltover, você é a minha única certeza e o meu porto seguro. ⚙️⚡"},
        {"Frase": "Você tem uma força brilhante e uma essência tão única que nem mesmo o Hextec conseguiria replicar. 💎"},
        {"Frase": "Eu atravessaria pontes, enfrentaria exércitos e mudaria o mundo inteiro só para garantir o seu sorriso."},
        {"Frase": "Você é perfeita exatamente do jeito que você é, com cada detalhe único que te faz ser a minha pessoa favorita. ⚡"},
        {"Frase": "Nossa conexão faísca mais forte do que qualquer energia pura. Você me inspira todos os dias."},
        {"Frase": "Você é a rosa do meu asteroide, a melodia da minha primavera e a força que me faz querer lutar todos os dias. 🌹🎻⚔️"},
        {"Frase": "Nem toda a tecnologia de Piltover ou as magias do mundo conseguiriam explicar o milagre que é ter você na minha vida. ✨"}
    ]
    
    # 🌟 POOL DE 31 MISSÕES DIÁRIAS (FÁCEIS / COTIDIANAS)
    banco_diarias = [
        {"Titulo": "Dar um abraço inesperado por trás e segurar por 15 segundos. 🫂", "Gif": "coberta.gif"},
        {"Titulo": "Roubar um beijo estalado enquanto ela estiver distraída falando ou mexendo no celular. 💋", "Gif": "Gato fazendo mirra.gif"},
        {"Titulo": "Assumir uma tarefa de casa dela hoje (lavar a louça, arrumar a cama, etc.) para poupar o tempo dela. 🧹", "Gif": "comida.gif"},
        {"Titulo": "Mandar um áudio curtinho no WhatsApp dizendo um motivo bobo pelo qual você se apaixonou por ela. 🎙️", "Gif": "raposa.gif"},
        {"Titulo": "Preparar um copo d'água, suco ou um lanchinho e levar até ela sem ela pedir. 🥤", "Gif": "comida.gif"},
        {"Titulo": "Elogiar o cabelo, o cheiro ou a roupa dela logo no primeiro instante em que se virem hoje. ✨", "Gif": "raposa.gif"},
        {"Titulo": "Fazer uma massagem rápida de 5 minutos nos ombros dela para aliviar a tensão. 💆‍♀️", "Gif": "coberta.gif"},
        {"Titulo": "Andar de mãos dadas o caminho inteiro se saírem, fazendo carinho com o polegar. 🤝", "Gif": "raposa.gif"},
        {"Titulo": "Mandar um meme interno de vocês dois no meio do dia com um 'lembrei de você'. ⚡", "Gif": "deboche.gif"},
        {"Titulo": "Fazer um cafuné demorado na cabeça dela enquanto assistem a alguma coisa. 🐼", "Gif": "coberta.gif"},
        {"Titulo": "Dizer 'Eu te amo' bem baixinho no ouvido dela do nada. 🤫", "Gif": "Gato fazendo mirra.gif"},
        {"Titulo": "Deixar um bilhetinho físico escondido no estojo, bolsa ou caderno dela. ✍️", "Gif": "raposa.gif"},
        {"Titulo": "Ceder totalmente o controle remoto ou a escolha do que assistir/comer hoje. 🎬", "Gif": "coberta.gif"},
        {"Titulo": "Abrir a porta do carro ou dar o lado de dentro da calçada para ela caminhar protegida. 🛡️", "Gif": "raposa.gif"},
        {"Titulo": "Fazer um lanchinho especial juntos tarde da noite (vale assaltar a geladeira!). 🌙🍟", "Gif": "comida.gif"},
        {"Titulo": "Fazer cócegas ou uma brincadeira boba até arrancar uma risada sincera dela. 😜", "Gif": "Monstrando a lingua.gif"},
        {"Titulo": "Dar um beijo demorado na testa dela antes de se despedirem ou irem dormir. 🌹", "Gif": "rosa.gif"},
        {"Titulo": "Passarem 10 minutos conversando sobre como foi o dia, prestando atenção total sem olhar o celular. 📱❌", "Gif": "raposa.gif"},
        {"Titulo": "Limpar ou organizar o espaço onde vocês costumam ficar juntos. 🧺", "Gif": "coberta.gif"},
        {"Titulo": "Fazer um carinho gostoso no rosto dela usando as costas das mãos. 🐱", "Gif": "Gato fazendo mirra.gif"},
        {"Titulo": "Deixar ela brava com uma piada boba de propósito e resolver cobrindo de beijos. 😤❤️", "Gif": "brava.gif"},
        {"Titulo": "Fazer o som de algum bicho ou uma careta aleatória só para quebrar a rotina. 👅", "Gif": "Monstrando a lingua.gif"},
        {"Titulo": "Segurar a mão dela firmemente enquanto estiverem assistindo TV ou descansando. 🔒", "Gif": "coberta.gif"},
        {"Titulo": "Trazer uma guloseima barata, mas que ela ame (uma bala, chiclete, chocolate de mercado) ao se encontrarem. 🍬", "Gif": "comida.gif"},
        {"Titulo": "Pentear, prender ou fazer um carinho nos cabelos dela com toda a calma do mundo. 💇‍♀️", "Gif": "coberta.gif"},
        {"Titulo": "Olhar nos olhos dela por 10 segundos seguidos em silêncio e terminar com um sorriso. 👀", "Gif": "raposa.gif"},
        {"Titulo": "Ajudar a carregar as sacolas, mochila ou qualquer peso que ela esteja levando. 🏋️‍♂️", "Gif": "raposa.gif"},
        {"Titulo": "Mandar uma foto sua zoada ou engraçada só para alegrar o período em que estiverem longe. 📸", "Gif": "deboche.gif"},
        {"Titulo": "Dar um cheirinho longo no pescoço dela. 🦊", "Gif": "Gato fazendo mirra.gif"},
        {"Titulo": "Dividirem exatamente metade de um lanche ou doce de um jeito fofo. 🍕", "Gif": "comida.gif"},
        {"Titulo": "Colocar uma música lenta no celular e dar uma voltinha dançando no meio da sala hoje. 💃", "Gif": "rosa.gif"}
    ]
    
    # 🌟 POOL DE 4 MISSÕES SEMANAIS (MÉDIAS / JOGOS E CRATIVIDADE)
    banco_semanais = [
        {"Titulo": "Noite de Jogos/Desafios: Passar pelo menos 45 minutos jogando algo juntos (videogame, tabuleiro ou cartas) valendo uma aposta divertida! 🎮🎲", "Gif": "deboche.gif"},
        {"Titulo": "Expressão Artística: Escrever um poema, uma cartinha caprichada ou fazer um desenho/colagem simples representando o amor de vocês e entregar essa semana. 📝🎨", "Gif": "rosa.gif"},
        {"Titulo": "Fortaleza do Casal: Montar uma cabana/fortaleza usando lençóis, cadeiras e travesseiros na sala ou quarto para assistirem a um filme lá dentro. ⛺🎬", "Gif": "coberta.gif"},
        {"Titulo": "Chef de Cozinha em Dupla: Escolher uma receita totalmente nova na internet e cozinharem juntos do zero, dividindo as tarefas e testando o prato. 🍝🍕", "Gif": "comida.gif"}
    ]
    
    # 🌟 POOL DE 12 MISSÕES MENSAIS (DIFÍCEIS / ENCONTROS EM BRASÍLIA E COMPRAS)
    banco_mensais = [
        {"Titulo": "Encontro ao Pôr do Sol no CCBB Brasília: Fazer um piquenique caprichado nos jardins do CCBB, aproveitar o espaço aberto e ver as exposições juntos. 🧺🎨", "Gif": "Wallpaper.jpg"},
        {"Titulo": "Tarde de Compras e Cinema: Ir ao ParkShopping ou Iguatemi com a missão de escolherem um presente ou mimo um para o outro (pode ser algo baratinho/divertido) e fechar o dia pegando um cineminha com combo de pipoca. 🛍️🍿", "Gif": "comida.gif"},
        {"Titulo": "Turismo Romântico na Ermida Dom Bosco: Ir assistir ao pôr do sol clássico de Brasília sentados na beira do Lago Paranoá, conversando e ouvindo música. 🌅🌌", "Gif": "Wallpaper.jpg"},
        {"Titulo": "Encontro Gastronômico na Ponta da Pontão do Lago Sul: Escolher um restaurante gostoso à beira do lago para jantarem ou tomarem um super sorvete, aproveitando a vista iluminada à noite. 🍽️✨", "Gif": "comida.gif"},
        {"Titulo": "Dia de Compras no Conjunto Nacional + Visita à Torre de TV: Passear pelo centro de Brasília, fazer umas comprinhas leves e subir na Torre de TV para ver a cidade do alto juntos. 🏢🏙️", "Gif": "raposa.gif"},
        {"Titulo": "Manhã no Parque da Cidade + Água de Coco: Alugar uma bike ou caminhar no Parque da Cidade, esticar uma canga na grama embaixo dos eucaliptos e terminar tomando uma água de coco gelada. 🚴‍♂️🥥", "Gif": "coberta.gif"},
        {"Titulo": "Noite Italiana/Pizza Especial: Sair para jantar em uma pizzaria artesanal ou cantina aconchegante de Brasília (como as da Asa Norte/Sul) focado em um encontro bem reservado e romântico. 🍕🍷", "Gif": "comida.gif"},
        {"Titulo": "Passeio Cultural e Fotos na Catedral e Esplanada: Tirar a tarde para fazer fotos conceituais um do outro na arquitetura da Catedral de Brasília e arredores, guardando lindas memórias para o diário. 📸🏛️", "Gif": "deboche.gif"},
        {"Titulo": "Tarde Doce nas Cafeterias da Asa Norte: Fazer uma 'expedição' para conhecer um café ou confeitaria super estilosa na Asa Norte, comendo doces finos e conversando bastante. 🍰☕", "Gif": "comida.gif"},
        {"Titulo": "Encontro Surpresa no Jardim Botânico: Caminhar pelas trilhas ecológicas, visitar o orquidário e tomar o famoso piquenique ou café da manhã colonial que tem nas lanchonetes de lá. 🌲🌺", "Gif": "rosa.gif"},
        {"Titulo": "Passeio de Lancha/Pedalinho ou SUP no Lago: Curtir uma atividade aquática divertida no Lago Paranoá em uma tarde de calor, terminando o dia comendo algo gostoso por perto. 🛶☀️", "Gif": "Monstrando a lingua.gif"},
        {"Titulo": "Missão Compras de Decoração: Ir a uma feirinha de artesanato (como a da Torre) ou loja legal de decoração com o objetivo de comprarem um item simbólico que vai ficar guardado como recordação do quarto de vocês. 🛍️🧸", "Gif": "raposa.gif"}
    ]
    
    # --- CÁLCULO DE DATAS TEMPORAIS ---
    agora = datetime.now()
    dia_atual = agora.day
    mes_atual = agora.month
    
    # Calcula a semana do mês atual (1 a 4)
    semana_atual = min(4, ((dia_atual - 1) // 7) + 1)
    
    # Sorteio automatizado baseado no tempo
    missao_diaria = banco_diarias[(dia_atual - 1) % len(banco_diarias)]
    missao_semanal = banco_semanais[(semana_atual - 1) % len(banco_semanais)]
    missao_mensal = banco_mensais[(mes_atual - 1) % len(banco_mensais)]
    
    # Monta a lista com as três categorias ativas
    missoes_finais = [
        {
            "ID": "diaria",
            "Titulo": f"☀️ [DIÁRIA] {missao_diaria['Titulo']}",
            "Tipo_Missao": "Fácil (Cotidiana)",
            "Status": "Disponível para Hoje",
            "Gif": missao_diaria['Gif']
        },
        {
            "ID": "semanal",
            "Titulo": f"🗓️ [SEMANAL - SEMANA {semana_atual}] {missao_semanal['Titulo']}",
            "Tipo_Missao": "Média (Criativa/Games)",
            "Status": "Disponível esta Semana",
            "Gif": missao_semanal['Gif']
        },
        {
            "ID": "mensal",
            "Titulo": f"👑 [MENSAL] {missao_mensal['Titulo']}",
            "Tipo_Missao": "Hardcore (Brasília/Compras)",
            "Status": "Disponível este Mês",
            "Gif": missao_mensal['Gif']
        }
    ]
    
    if not capa: 
        capa = [{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}]
        
    return capa[0], elogios_customizados, missoes_finais
