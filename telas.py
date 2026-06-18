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
    st.title("🎯 Mural de Missões Ativas")
    st.write("Aqui estão os seus desafios temporais. Cumpra-os na vida real para ganhar XP!")
    st.markdown("---")
    
    # Inicializa variáveis de controle de XP se não existirem
    if "xp_total" not in st.session_state:
        st.session_state["xp_total"] = 0
    if "missoes_concluidas_count" not in st.session_state:
        st.session_state["missoes_concluidas_count"] = 0
    if "feitas_hoje" not in st.session_state:
        st.session_state["feitas_hoje"] = []

    if not df_missoes:
        st.info("🎯 Nenhuma missão ativa encontrada na planilha neste momento.")
        return

    # Percorre a lista gerando um índice numérico (idx) automático para cada botão
    for idx, missao in enumerate(df_missoes):
        # Captura os dados tratando possíveis variações de letras maiúsculas/minúsculas
        titulo = missao.get("Titulo", missao.get("titulo", "Missão Secreta"))
        tipo = missao.get("Tipo_Missao", missao.get("tipo", "Fácil (Cotidiana)"))
        gif = missao.get("Gif", missao.get("gif", ""))
        
        # Define a recompensa de XP baseada no texto do tipo de missão
        if "Diária" in str(tipo) or "DIÁRIA" in str(titulo) or "Fácil" in str(tipo):
            xp_ganho = 50
        elif "Semanal" in str(tipo) or "SEMANAL" in str(titulo) or "Média" in str(tipo):
            xp_ganho = 150
        else:
            xp_ganho = 500
            
        # Usa o índice numérico da linha como o ID único do botão
        id_unico_missao = f"missao_num_{idx}"
        ja_feita = id_unico_missao in st.session_state["feitas_hoje"]
        
        st.markdown(f"""
            <div class='card' style='border-left: 5px solid #FFD700; margin-bottom: 20px;'>
                <span style='float: right; background: #1C2541; padding: 3px 8px; border-radius: 10px; font-size: 12px; color: #FFD700; font-weight: bold;'>✨ +{xp_ganho} XP</span>
                <h3 style='margin-top: 0px; color: #FFFFFF;'>{titulo}</h3>
                <p style='margin-bottom: 0px; color: #E0E1DD;'><b>Dificuldade:</b> {tipo}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Mostra o Gif correspondente se ele estiver configurado
        if gif:
            try:
                st.image(gif, width=250)
            except Exception:
                pass
            
        # Sistema de Botão Corrigido usando chaves únicas numéricas
        if ja_feita:
            st.success("✅ Você já concluiu essa missão e coletou o XP!")
        else:
            if st.button(f"🎯 Concluir Desafio ({xp_ganho} XP)", key=f"btn_ctrl_{id_unico_missao}"):
                st.session_state["xp_total"] += xp_ganho
                st.session_state["missoes_concluidas_count"] += 1
                st.session_state["feitas_hoje"].append(id_unico_missao)
                st.balloons()
                st.success(f"Incrível! Você ganhou {xp_ganho} XP para a sua jornada! ⭐")
                st.rerun()
                
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")
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
    st.title("💬 Enviar um Carinho Especial")
    st.write("Escreva algo lindo para a Sara. A mensagem vai para o mural do app e direto para o e-mail dela!")
    st.markdown("---")
    
    with st.form("form_carinho", clear_on_submit=True):
        texto_carinho = st.text_area("O que você quer dizer para a sua rosa hoje?")
        tipo_carinho = st.selectbox("Escolha o tom do carinho:", ["Romântico 🌹", "Engraçado 🍿", "Apoio/Motivação ✨"])
        
        botao_enviar = st.form_submit_button("🚀 Enviar Carinho ao Universo")
        
        if botao_enviar and texto_carinho:
            # 1. (Aqui fica o seu código atual que salva no arquivo dados.py ou planilha principal)
            # ... [Seu código atual de salvar carinho] ...
            
            # 2. GATILHO PARA O EMAIL (Via Zapier):
            # Vamos estruturar a linha exatamente como o Zapier vai ler na aba 'Notificacoes'
            try:
                import pandas as pd
                from datetime import datetime
                
                # Criamos a mensagem formatada que ela vai ler no e-mail
                mensagem_email = f"Oi Sara! O Denner te enviou um carinho {tipo_carinho} pelo app:\n\n\"{texto_carinho}\"\n\nCom amor, seu Pequeno Príncipe. 🪐"
                
                # Puxamos o arquivo que gerencia a planilha para injetar na aba 'Notificacoes'
                # Se você usa o st.session_state ou gspread, basta adicionar uma nova linha na aba 'Notificacoes'
                # Exemplo simulado por webhook ou append simples:
                import notificacoes
                notificacoes.disparar_notificacao_planilha(mensagem_email)
                
                st.balloons()
                st.success("✨ Carinho enviado para o mural e a caminho do e-mail dela!")
            except Exception as e:
                st.error("O carinho foi para o mural, mas houve um problema ao agendar o e-mail.")
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
