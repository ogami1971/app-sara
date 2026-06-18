import streamlit as st
import random
from datetime import datetime

def exibir_inicio(capa_data, df_elogios):
    st.title(f"✨ {capa_data.get('Titulo_App', 'Nosso Universo')} ✨")
    st.markdown(f"<h3>{capa_data.get('Subtitulo_App', 'Bem-vinda')}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("❤️ Um carinho para o seu dia")
    
    if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
        frases = [item['Frase'] for item in df_elogios if 'Frase' in item]
        frase_sorteada = random.choice(frases) if frases else "Você é a rosa mais preciosa do meu universo!"
        
        # 🌟 CORREÇÃO: Salva a frase na memória estável antes do st.rerun() para ela não sumir!
        st.session_state["ultima_frase_sorteada"] = frase_sorteada
        
        # Sistema inteligente que lê palavras-chave e chaveia o ID do tema
        frase_minuscula = frase_sorteada.lower()
        if "rosa" in frase_minuscula or "planeta" in frase_minuscula or "essencial" in frase_minuscula or "quatro da tarde" in frase_minuscula or "universo" in frase_minuscula:
            st.session_state["tema_fundo"] = "pequeno_principe"
        elif "kaori" in frase_minuscula or "violino" in frase_minuscula or "melodia" in frase_minuscula or "sinfonia" in frase_minuscula or "primavera" in frase_minuscula or "música" in frase_minuscula:
            st.session_state["tema_fundo"] = "shigatsu"
        elif "respiração" in frase_minuscula or "luas" in frase_minuscula or "tanjiro" in frase_minuscula or "rengoku" in frase_minuscula or "espada" in frase_minuscula or "borboleta" in frase_minuscula:
            st.session_state["tema_fundo"] = "demon_slayer"
        elif "zaun" in frase_minuscula or "piltover" in frase_minuscula or "hextec" in frase_minuscula or "perfeita exatamente" in frase_minuscula or "faísca" in frase_minuscula:
            st.session_state["tema_fundo"] = "arcane"
        
        st.balloons() 
        # Força o Streamlit a redesenhar a tela aplicando o fundo imediatamente na mudança
        st.rerun()

    # Mostra a frase salva na tela (ela vai persistir perfeitamente mesmo após o st.rerun())
    if "ultima_frase_sorteada" in st.session_state:
        st.markdown(f"<div class='card' style='text-align: center; font-size: 20px; font-style: italic; color: #FFFFFF;'>\"{st.session_state['ultima_frase_sorteada']}\"</div>", unsafe_allow_html=True)
    else: 
        st.info("Clique no botão acima para receber sua dose diária de amor!")

def exibir_missoes(df_missoes):
    st.title("🎯 Nossas Missões Românticas")
    st.write("Aqui estão os nossos desafios! Clique no botão de cada uma para ver uma surpresa animada:")
    st.markdown("---")
    
    for row in df_missoes:
        status_real = row.get('Status', 'Pendente').strip()
        status_icon = "✅" if status_real == "Concluída" else "⏳"
        classe_texto = "missao-concluida" if status_real == "Concluída" else ""
        
        st.markdown(f"""
            <div class='card'>
                <span style='float: right; background: #FF4B4B; padding: 2px 8px; border-radius: 10px; font-size: 12px; font-weight: bold;'>{row.get('Tipo_Missao', 'Normal')}</span>
                <h4 class='{classe_texto}'>{status_icon} {row.get('Titulo', 'Missão')}</h4>
                <p style='font-size: 13px; color: #aaa; margin-bottom: 0px;'>Status do Desafio: {status_real}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🔍 Ver Surpresa: {row.get('Titulo')}", key=f"btn_{row.get('ID')}"):
            st.write(f"**Nível:** Essa missão é considerada *{row.get('Tipo_Missao')}*. Vamos cumprir juntos?")
            nome_gif = str(row.get('Gif', '')).strip()
            try: 
                st.image(nome_gif, caption="Nosso Moment!")
            except Exception:
                try: 
                    st.image(nome_gif.lower(), caption="Nosso Moment!")
                except Exception: 
                    st.error(f"🎬 O arquivo animado '{nome_gif}' não foi localizado na raiz.")
        st.markdown("<br>", unsafe_allow_html=True)

def exibir_diario():
    st.title("📸 Nosso Diário de Memórias")
    st.markdown("---")
    
    st.subheader("🌹 O Princípio de Tudo")
    st.markdown("> *“Tu te tornas eternamente responsável por aquilo que cativas.”*")
    try: 
        st.image("Tela de carregamento.jpg", caption="Onde o nosso universo começou...")
    except Exception: 
        st.info("📸 Preparando nosso mural de fotos...")
        
    st.markdown("---")
    st.subheader("✨ Nossa Sintonia")
    try: 
        st.image("rosa.gif", caption="Você é única no mundo para mim.")
    except Exception: 
        st.warning("🌹 Cuidando da nossa rosa animada...")

def exibir_linha_tempo():
    st.title("⏳ Nossa Linha do Tempo")
    st.write("Um espaço para lembrar os momentos em que nossos planetas se cruzaram de forma inesquecível ✨")
    st.markdown("---")
    
    st.markdown("""
        <div class='card'>
            <h4>🚀 O Dia que nos Conhecemos</h4>
            <p style='color: #E0E1DD; font-style: italic;'>O início de uma jornada inteira por esse espaço sideral.</p>
        </div>
        <div class='card'>
            <h4>🔒 O Pedido</h4>
            <p style='color: #E0E1DD; font-style: italic;'>O instante exato em que decidi cativar e proteger a rosa mais linda do jardim.</p>
        </div>
        <div class='card'>
            <h4>🌌 Próximo Capítulo...</h4>
            <p style='color: #888888; font-style: italic;'>Ainda estamos escrevendo a nossa história, estrela por estrela.</p>
        </div>
    """, unsafe_allow_html=True)

def exibir_enviar_carinho():
    st.title("💬 Espaço do Carinho")
    st.write("Como você está se sentindo agora, minha rosa? Escolha uma reação ou escreva uma mensagem!")
    st.markdown("---")
    
    opcoes_reacoes = {
        "Selecione uma reação...": None,
        "Estou com saudades 🦊": "raposa.gif",
        "Quero dengo / manhosa 🐱": "Gato fazendo mirra.gif",
        "Quero cafuné e dengo (Preguiça) 🐼": "coberta.gif",
        "Pensando em você... 🤔": "raposa.gif",
        "Tô brava com você! 😤": "brava.gif",
        "Te acho um bobo (Deboche) 😜": "deboche.gif",
        "Mostrando a língua para você 👅": "Monstrando a lingua.gif",
        "Estou com fome! 🍕": "comida.gif",
        "Quero coberta e cafuné 🛌": "coberta.gif"
    }
    
    reacao_escolhida = st.selectbox("Como está seu humor hoje?", list(opcoes_reacoes.keys()))
    mensagem_personalizada = st.text_input("Quer deixar um recado extra? (Opcional)", placeholder="Escreva algo aqui...")
    
    if st.button("🚀 Enviar para o Nosso Universo"):
        agora = datetime.now().strftime("%H:%M")
        if reacao_escolhida != "Selecione uma reação..." or mensagem_personalizada.strip() != "":
            novo_carinho = {
                "hora": agora,
                "reacao_texto": reacao_escolhida if reacao_escolhida != "Selecione uma reação..." else None,
                "gif": opcoes_reacoes[reacao_escolhida] if reacao_escolhida != "Selecione uma reação..." else None,
                "mensagem": mensagem_personalizada.strip() if mensagem_personalizada.strip() != "" else None
            }
            st.session_state["historico_carinhos"].insert(0, novo_carinho)
            st.toast("Carinho enviado com sucesso! ✨", icon="❤️")
        else:
            st.warning("Por favor, selecione uma reação ou digite uma mensagem!")
            
    if st.session_state["historico_carinhos"]:
        st.markdown("### 🌟 Painel de Reações em Tempo Real")
        ultimo_envio = st.session_state["historico_carinhos"][0]
        st.markdown(f"#### 🏹 O que a Sara está sentindo agora ({ultimo_envio['hora']}):")
        
        if ultimo_envio["mensagem"]:
            st.markdown(f"<div class='card' style='font-size: 18px; text-align: center;'>💭 <b>Recado da Sara:</b> <br><i>\"{ultimo_envio['mensagem']}\"</i></div>", unsafe_allow_html=True)
            
        if ultimo_envio["gif"]:
            try:
                st.image(ultimo_envio["gif"], caption=f"Humor atual: {ultimo_envio['reacao_texto']}")
            except Exception:
                st.error(f"🎬 O arquivo animado '{ultimo_envio['gif']}' não pôde ser renderizado.")
