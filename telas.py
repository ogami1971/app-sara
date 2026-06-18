import streamlit as st
import random
from datetime import datetime
import dados
import notificacoes

def exibir_inicio(capa_data, df_elogios):
    st.title(f"✨ {capa_data.get('Titulo_App', 'Nosso Universo')} ✨")
    st.markdown(f"<h3>{capa_data.get('Subtitulo_App', 'Bem-vinda')}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("❤️ Um carinho para o seu dia")
    
    if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
        frases = [item['Frase'] for item in df_elogios if 'Frase' in item]
        frase_sorteada = random.choice(frases) if frases else "Você é a rosa mais preciosa do meu universo!"
        
        # Salva a frase na memória estável antes do st.rerun() para ela não sumir!
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

    # Mostra a frase salva na tela
    if "ultima_frase_sorteada" in st.session_state:
        st.markdown(f"<div class='card' style='text-align: center; font-size: 20px; font-style: italic; color: #FFFFFF;'>\"{st.session_state['ultima_frase_sorteada']}\"</div>", unsafe_allow_html=True)
    else: 
        st.info("Clique no botão acima para receber sua dose diária de amor!")

def exibir_missoes(df_missoes):
    st.title("🎯 Mural de Missões Ativas")
    st.write("Aqui estão os seus desafios temporais. Cumpra-os na vida real para ganhar XP!")
    st.markdown("---")
    
    # 🌟 INTEGRADO COM O BANCO DE DADOS LOCAL
    if "xp_atual" not in st.session_state:
        dados.carregar_progresso_banco()

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
        
        # Criamos o histórico em session_state baseado na sessão do dia
        if "feitas_hoje" not in st.session_state:
            st.session_state["feitas_hoje"] = []
            
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
            
        # Sistema de Botão Corrigido usando chaves únicas numéricas e salvamento no JSON
        if ja_feita:
            st.success("✅ Você já concluiu essa missão e coletou o XP!")
        else:
            if st.button(f"🎯 Concluir Desafio ({xp_ganho} XP)", key=f"btn_ctrl_{id_unico_missao}"):
                st.session_state["feitas_hoje"].append(id_unico_missao)
                
                # 🌟 Adiciona o XP e calcula o Level Up direto na mecânica persistente!
                dados.adicionar_xp(xp_ganho)
                
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
            # Monta o texto que vai para o e-mail através do Zapier
            mensagem_email = f"Oi Sara! O Denner te enviou um carinho {tipo_carinho} pelo app:\n\n\"{texto_carinho}\"\n\nCom amor, seu Pequeno Príncipe. 🪐"
            
            # Dispara para o Webhook do Zapier
            sucesso = notificacoes.disparar_notificacao_planilha(mensagem_email)
            
            if sucesso:
                st.balloons()
                st.success("✨ Carinho enviado para o mural e a caminho do e-mail dela!")
            else:
                st.warning("O carinho foi enviado, mas o Zapier não respondeu. Verifique o link no arquivo notificacoes.py!")

def exibir_maquina_cupons():
    st.title("🎰 Máquina de Cupons Românticos")
    st.write("Escolha um cupom especial e resgate-o na vida real! O Denner receberá um aviso instantâneo.")
    st.markdown("---")
    
    # Carrega os cupons e mapeia se foram usados cruzando com a memória do JSON
    cupons = dados.carregar_cupons()
    
    for cupom in cupons:
        with st.container():
            if cupom["usado"]:
                # Visual elegante de cupom desativado/queimado
                st.markdown(
                    f"""
                    <div style="background-color: rgba(40, 40, 50, 0.4); border-left: 5px solid #ff4b4b; padding: 15px; border-radius: 8px; margin-bottom: 15px; opacity: 0.6;">
                        <span style="text-decoration: line-through; font-size: 20px; font-weight: bold; color: #888;">{cupom['titulo']}</span><br>
                        <span style="color: #ff4b4b; font-weight: bold;">🔴 Este cupom já foi utilizado!</span>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                st.button("Cupom Queimado ✘", key=f"btn_{cupom['id']}", disabled=True, use_container_width=True)
            else:
                # Visual ativo de voucher brilhante
                st.markdown(
                    f"""
                    <div style="background-color: rgba(20, 30, 60, 0.7); border-left: 5px solid #4FEBDE; padding: 15px; border-radius: 8px; margin-bottom: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
                        <span style="font-size: 20px; font-weight: bold; color: #fff;">{cupom['titulo']}</span><br>
                        <span style="color: #ddd; font-size: 14px;">{cupom['descricao']}</span>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                botao_resgatar = st.button("🎟️ Resgatar este Voucher", key=f"btn_{cupom['id']}", type="primary", use_container_width=True)
                
                if botao_resgatar:
                    # 1. Registra o ID na lista interna da sessão
                    if "cupons_usados_ids" not in st.session_state:
                        st.session_state["cupons_usados_ids"] = []
                    st.session_state["cupons_usados_ids"].append(cupom["id"])
                    
                    # 2. Persiste a alteração no banco JSON imediatamente
                    dados.salvar_progresso_banco()
                    
                    # 3. Dispara a mensagem para o seu e-mail via Zapier
                    mensagem_notificacao = f"🚨 ALERTA DE RESGATE! 🚨\n\nA Sara acabou de resgatar um cupom no app do casal:\n\n🎟️ Cupom: {cupom['titulo']}\n📋 Detalhes: {cupom['descricao']}\n\nPrepare-se para cumprir a sua promessa! 😉"
                    notificacoes.disparar_notificacao_planilha(mensagem_notificacao)
                    
                    # 4. Feedback e recarregamento limpo
                    st.balloons()
                    st.success(f"Cupom '{cupom['titulo']}' resgatado com sucesso! O Denner foi notificado.")
                    st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)

def exibir_central_conquistas():
    st.title("🎯 Central de Conquistas da Sara")
    st.write("Acompanhe suas medalhas colecionáveis! Elas são desbloqueadas conforme você interage com o nosso universo.")
    st.markdown("---")
    
    # Carrega as conquistas validadas em tempo real com base nas ações salvas no JSON
    conquistas = dados.carregar_conquistas()
    
    # Exibe as medalhas em um grid organizado (3 por linha)
    cols = st.columns(3)
    
    for i, conquista in enumerate(conquistas):
        col_atual = cols[i % 3] # Distribui entre as 3 colunas dinamicamente
        
        with col_atual:
            if conquista["desbloqueada"]:
                # Medalha Desbloqueada: Colorida, brilhante e dourada
                st.markdown(
                    f"""
                    <div style="background-color: rgba(255, 215, 0, 0.15); 
                                border: 2px solid #FFD700; 
                                padding: 20px; 
                                border-radius: 15px; 
                                text-align: center; 
                                margin-bottom: 20px;
                                box-shadow: 0px 4px 15px rgba(255, 215, 0, 0.3);">
                        <div style="font-size: 50px; margin-bottom: 10px;">{conquista['icone']}</div>
                        <h4 style="color: #FFD700 !important; margin: 0; font-weight: bold;">{conquista['titulo']}</h4>
                        <p style="color: #fff; font-size: 13px; margin-top: 5px;">{conquista['descricao']}</p>
                        <span style="background-color: #2e7d32; color: white; padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: bold;">🔓 CONQUISTADO</span>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            else:
                # Medalha Bloqueada: Cinza, opaca e discreta
                st.markdown(
                    f"""
                    <div style="background-color: rgba(40, 40, 50, 0.3); 
                                border: 2px dashed #555; 
                                padding: 20px; 
                                border-radius: 15px; 
                                text-align: center; 
                                margin-bottom: 20px;
                                opacity: 0.5;">
                        <div style="font-size: 50px; margin-bottom: 10px; filter: grayscale(100%);">🔒</div>
                        <h4 style="color: #888 !important; margin: 0;">Bloqueada</h4>
                        <p style="color: #aaa; font-size: 13px; margin-top: 5px;">{conquista['descricao']}</p>
                        <span style="background-color: #37474f; color: #aaa; padding: 3px 10px; border-radius: 10px; font-size: 11px;">🔒 BLOQUEADO</span>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
