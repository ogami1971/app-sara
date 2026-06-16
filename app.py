# --- TELA 4: ENVIAR CARINHO ---
elif tela_selecionada == "💬 Enviar Carinho":
    st.title("💬 Espaço do Carinho")
    st.write("Como você está se sentindo agora, minha rosa? Escolha uma reação ou escreva uma mensagem para atualizar nosso espaço em tempo real!")
    st.markdown("---")
    
    # Dicionário mapeando as reações aos nomes exatos dos arquivos na sua raiz do GitHub
    opcoes_reacoes = {
        "Selecione uma reação...": None,
        "Estou com saudades 🦊": "raposa.gif",
        "Quero dengo / manhosa 🐱": "Gato fazendo mirra.gif",
        "Tô brava com você! 😤": "brava.gif",
        "Te acho um bobo (Deboche) 😜": "deboche.gif",
        "Mostrando a língua para você 👅": "Monstrando a lingua.gif",
        "Estou com fome! 🍕": "comida.gif",
        "Quero coberta e cafuné 🛌": "coberta.gif"
    }
    
    reacao_escolhida = st.selectbox("Como está seu humor hoje?", list(opcoes_reacoes.keys()))
    mensagem_personalizada = st.text_input("Quer deixar um recado extra? (Opcional)", placeholder="Escreva algo aqui para o Denner ler...")
    
    if st.button("🚀 Enviar para o Nosso Universo"):
        agora = datetime.now().strftime("%H:%M")
        
        if reacao_escolhida != "Selecione uma reação..." or mensagem_personalizada.strip() != "":
            novo_carinho = {
                "hora": agora,
                "reacao_texto": reacao_escolhida if reacao_escolhida != "Selecione uma reação..." else None,
                "gif": opcoes_reacoes[reacao_escolhida] if reacao_escolhida != "Selecione uma reação..." else None,
                "mensagem": mensagem_personalizada.strip() if mensagem_personalizada.strip() != "" else None
            }
            # Insere no início da lista para ordenação decrescente (mais recente no topo)
            st.session_state["historico_carinhos"].insert(0, novo_carinho)
            st.toast("Carinho enviado com sucesso! ✨", icon="❤️")
        else:
            st.warning("Por favor, selecione uma reação ou digite uma mensagem antes de enviar!")
            
    # Painel dinâmico que renderiza as ações salvas na memória da sessão
    if st.session_state["historico_carinhos"]:
        st.markdown("### 🌟 Painel de Reações em Tempo Real")
        
        ultimo_envio = st.session_state["historico_carinhos"][0]
        st.markdown(f"#### 🏹 O que a Sara está sentindo agora ({ultimo_envio['hora']}):")
        
        if ultimo_envio["mensagem"]:
            st.markdown(f"<div class='card' style='font-size: 18px; text-align: center;'>💭 <b>Recado da Sara:</b> <br><i>\"{ultimo_envio['mensagem']}\"</i></div>", unsafe_allow_html=True)
            
        if ultimo_envio["gif"]:
            try:
                st.image(ultimo_envio["gif"], caption=f"Humor atual: {ultimo_envio['reacao_texto']}", use_container_width=True)
            except Exception:
                st.error(f"🎬 O arquivo animado '{ultimo_envio['gif']}' não pôde ser renderizado.")
                
        # Expander elegante para listar as reações passadas da navegação atual
        if len(st.session_state["historico_carinhos"]) > 1:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander("⏳ Ver histórico de reações anteriores da sessão"):
                for antigo in st.session_state["historico_carinhos"][1:]:
                    texto_historico = f"⏱️ **{antigo['hora']}** -"
                    if antigo['reacao_texto']:
                        texto_historico += f" Reação: *{antigo['reacao_texto']}*"
                    if antigo['mensagem']:
                        texto_historico += f" | Mensagem: *\"{antigo['mensagem']}\"*"
                    st.write(texto_historico)
