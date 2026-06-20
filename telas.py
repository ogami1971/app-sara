import streamlit as st
import random
from datetime import datetime
import dados
import notifications as notificacoes # ou 'import notificacoes' dependendo do nome do seu arquivo

def exibir_inicio(capa_data, df_elogios):
    st.title(f"✨ {capa_data.get('Titulo_App', 'Nosso Universo')} ✨")
    st.markdown(f"<h3>{capa_data.get('Subtitulo_App', 'Bem-vinda')}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("❤️ Um carinho para o seu dia")
    
    if st.button("✨ Quer um carinho? (Clique aqui) ✨"):
        frases = [item['Frase'] for item in df_elogios if 'Frase' in item]
        frase_sorteada = random.choice(frases) if frases else "Você é a rosa mais preciosa do meu universo!"
        st.session_state["ultima_frase_sorteada"] = frase_sorteada
        st.balloons() 
        st.rerun()

    if "ultima_frase_sorteada" in st.session_state:
        st.markdown(f"<div class='card' style='text-align: center; font-size: 20px; font-style: italic; color: #FFFFFF;'>\"{st.session_state['ultima_frase_sorteada']}\"</div>", unsafe_allow_html=True)
    else: 
        st.info("Clique no botão acima para receber sua dose diária de amor!")

def exibir_missoes(df_missoes):
    st.title("🎯 Mural de Missões Ativas")
    st.write("Aqui estão os seus desafios temporais. Cumpra-os na vida real para ganhar XP!")
    st.markdown("---")
    
    if df_missoes is None or (hasattr(df_missoes, "empty") and df_missoes.empty):
        st.info("🎯 Nenhuma missão ativa encontrada na planilha neste momento.")
        return

    lista_missoes = df_missoes.to_dict(orient="records") if hasattr(df_missoes, "to_dict") else df_missoes

    for idx, missao in enumerate(lista_missoes):
        titulo = missao.get("Missao", "Missão Secreta")
        tipo = missao.get("Tipo_Missao", "Fácil (Cotidiana)")
        id_missao_planilha = missao.get("ID_Missao", idx)
        
        xp_ganho = 50 if "Fácil" in str(tipo) or "Diária" in str(tipo) else 150 if "Média" in str(tipo) else 500
        id_unico_missao = f"missao_num_{id_missao_planilha}"
        
        status_planilha = str(missao.get("Concluida", "FALSE")).upper() == "TRUE"
        ja_feita = id_unico_missao in st.session_state.get("feitas_hoje", []) or status_planilha
        
        st.markdown(f"""
            <div class='card' style='border-left: 5px solid #FFD700; margin-bottom: 20px; background: rgba(30,40,70,0.5); padding: 15px; border-radius: 8px;'>
                <span style='float: right; background: #1C2541; padding: 3px 8px; border-radius: 10px; font-size: 12px; color: #FFD700; font-weight: bold;'>✨ +{xp_ganho} XP</span>
                <h3 style='margin-top: 0px; color: #FFFFFF;'>{titulo}</h3>
                <p style='margin-bottom: 0px; color: #E0E1DD;'><b>Dificuldade:</b> {tipo}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if ja_feita:
            st.success("✅ Você já concluiu essa missão!")
        else:
            if st.button(f"🎯 Concluir Desafio ({xp_ganho} XP)", key=f"btn_ctrl_{id_unico_missao}"):
                if "feitas_hoje" not in st.session_state: st.session_state["feitas_hoje"] = []
                st.session_state["feitas_hoje"].append(id_unico_missao)
                dados.adicionar_xp(xp_ganho)
                
                notificacoes.disparar_notificacao_planilha(f"Completou a missão: *{titulo}*", quem_enviou="Sara")
                st.balloons()
                st.rerun()

def exibir_maquina_cupons(df_cupons):
    """
    RECEBE OS CUPONS DINÂMICOS DO SHEETS: 
    Renderiza os cupons cadastrados na aba 'Cupons_Romanticos'.
    """
    st.title("🎰 Máquina de Cupons Românticos")
    st.write("Escolha um cupom especial e resgate-o na vida real! O Denner receberá um aviso instantâneo no WhatsApp.")
    st.markdown("---")
    
    # Cruza a lista do Sheets com os salvamentos do JSON local
    cupons = dados.processar_cupons_dinamicos(df_cupons)
    
    if not cupons:
        st.info("🎰 Nenhum cupom localizado. Cadastre os cupons na sua aba 'Cupons_Romanticos' da Planilha!")
        return
    
    for cupom in cupons:
        with st.container():
            if cupom["usado"]:
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
                    if "cupons_usados_ids" not in st.session_state:
                        st.session_state["cupons_usados_ids"] = []
                    st.session_state["cupons_usados_ids"].append(cupom["id"])
                    
                    dados.salvar_progresso_banco()
                    
                    detalhe_cupom = f"Resgatou o voucher *{cupom['titulo']}* ({cupom['descricao']})."
                    notificacoes.disparar_notificacao_planilha(detalhe_cupom, quem_enviou="Sara")
                    
                    st.balloons()
                    st.success(f"Cupom '{cupom['titulo']}' resgatado! Alerta enviado para o Denner.")
                    st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)

def exibir_enviar_carinho():
    st.title("💬 Enviar um Carinho Especial")
    st.write("Escreva algo lindo para a Sara. A mensagem vai direto para o WhatsApp dela!")
    st.markdown("---")
    
    with st.form("form_carinho", clear_on_submit=True):
        texto_carinho = st.text_area("O que você quer dizer para a sua rosa hoje?")
        tipo_carinho = st.selectbox("Escolha o tom do carinho:", ["Romântico 🌹", "Engraçado 🍿", "Apoio/Motivação ✨"])
        botao_enviar = st.form_submit_button("🚀 Enviar Carinho ao Universo")
        
        if botao_enviar and texto_carinho:
            carinho_formatado = f"Carinho {tipo_carinho}:\n\"{texto_carinho}\""
            sucesso = notificacoes.disparar_notificacao_planilha(carinho_formatado, quem_enviou="Denner")
            if sucesso:
                st.balloons()
                st.success("✨ Carinho enviado com sucesso e a caminho do WhatsApp!")
            else:
                st.error("Erro ao enviar. Verifique as chaves de API.")

def exibir_central_conquistas():
    st.title("🎯 Central de Conquistas da Sara")
    st.write("Acompanhe suas medalhas colecionáveis!")
    st.markdown("---")
    conquistas = dados.carregar_conquistas()
    cols = st.columns(3)
    for i, conquista in enumerate(conquistas):
        with cols[i % 3]:
            if conquista["desbloqueada"]:
                st.markdown(f"<div style='border: 2px solid #FFD700; padding: 15px; border-radius: 10px; text-align: center;'><h2>{conquista['icone']}</h2><h4>{conquista['titulo']}</h4><p>{conquista['descricao']}</p></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='border: 2px dashed #555; padding: 15px; border-radius: 10px; text-align: center; opacity: 0.4;'><h2>🔒</h2><h4>Bloqueada</h4><p>{conquista['descricao']}</p></div>", unsafe_allow_html=True)
