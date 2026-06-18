import streamlit as st
import pandas as pd
import json
import os

def carregar_dados():
    """
    Carrega as informações do ecossistema de planilhas.
    Certifique-se de que a conexão ou leitura real da sua planilha 
    esteja apontando para as abas certas!
    """
    # Exemplo de estrutura estruturada. Substitua pela sua chamada real do gsheets se necessário.
    capa_data = {"Titulo_App": "App Pequeno Príncipe - Sara", "Subtitulo_App": "Bem-vinda ao nosso universo!"}
    
    # Mocks vazios seguros para caso a planilha falhe na leitura inicial
    df_elogios = [] 
    df_missoes = pd.DataFrame(columns=["ID_Missao", "Missao", "Concluida", "Tipo_Missao"])
    
    return capa_data, df_elogios, df_missoes

# ------------------------------------------------------------------
# 🎰 SISTEMA DE BANCO DE DADOS PERSISTENTE (JSON)
# ------------------------------------------------------------------

ARQUIVO_BANCO = "progresso_sara.json"

def inicializar_banco_local():
    """
    Cria o arquivo de banco de dados com os valores zerados/iniciais 
    caso ele ainda não exista no servidor.
    """
    if not os.path.exists(ARQUIVO_BANCO):
        dados_iniciais = {
            "xp": 0,
            "nivel": 1,
            "cupons_usados": [],
            "conquistas_desbloqueadas": ["primeiro_passo"] # Ganha de brinde ao entrar
        }
        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f:
            json.dump(dados_iniciais, f, indent=4, ensure_ascii=False)

def carregar_progresso_banco():
    """
    Carrega os dados do arquivo JSON para o st.session_state do Streamlit.
    Roda uma vez logo quando o aplicativo é aberto.
    """
    inicializar_banco_local()
    
    try:
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as f:
            dados_carregados = json.load(f)
            
        # Transfere os dados salvos para a memória do app
        st.session_state["xp_atual"] = dados_carregados.get("xp", 0)
        st.session_state["nivel_atual"] = dados_carregados.get("nivel", 1)
        st.session_state["cupons_usados_ids"] = dados_carregados.get("cupons_usados", [])
        st.session_state["conquistas_ids"] = dados_carregados.get("conquistas_desbloqueadas", ["primeiro_passo"])
    except Exception:
        # Fallback de segurança para o app nunca quebrar
        if "xp_atual" not in st.session_state: st.session_state["xp_atual"] = 0
        if "nivel_atual" not in st.session_state: st.session_state["nivel_atual"] = 1
        if "cupons_usados_ids" not in st.session_state: st.session_state["cupons_usados_ids"] = []
        if "conquistas_ids" not in st.session_state: st.session_state["conquistas_ids"] = ["primeiro_passo"]

def salvar_progresso_banco():
    """
    Pega os dados atuais da navegação da Sara e salva permanentemente no arquivo.
    """
    dados_para_salvar = {
        "xp": st.session_state.get("xp_atual", 0),
        "nivel": st.session_state.get("nivel_atual", 1),
        "cupons_usados": st.session_state.get("cupons_usados_ids", []),
        "conquistas_desbloqueadas": st.session_state.get("conquistas_ids", ["primeiro_passo"])
    }
    
    try:
        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f:
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
    except Exception:
        pass

# ------------------------------------------------------------------
# 🎟️ GERENCIADORES DE CONTEÚDO (CUPONS E CONQUISTAS)
# ------------------------------------------------------------------

def carregar_cupons():
    """
    Retorna a lista estruturada de cupons marcando dinamicamente 
    quais já foram utilizados com base no banco de dados.
    """
    # Garante que o estado dos IDs usados existe
    if "cupons_usados_ids" not in st.session_state:
        carregar_progresso_banco()
        
    cupons_base = [
        {"id": 1, "titulo": "Vale 1 Massagem de 30 min 💆‍♀️", "descricao": "Direito a óleo perfumado e música calma."},
        {"id": 2, "titulo": "Vale 1 Jantar Especial 🍝", "descricao": "Pago e escolhido inteiramente pelo Denner."},
        {"id": 3, "titulo": "Vale Cinema em Casa 🍿", "descricao": "Você escolher o filme e eu faço a pipoca (sem reclamar!)."},
        {"id": 4, "titulo": "Vale Rodada de Cafuné Unlimited 🧸", "descricao": "Válido até você ou eu dormirmos."},
        {"id": 5, "titulo": "Vale Sair para comer Doce 🍰", "descricao": "Uma caçada aos melhores doces da Asa Norte."},
    ]
    
    # Adiciona a marcação True/False dinamicamente baseada no banco de dados JSON
    for cupom in cupons_base:
        cupom["usado"] = cupom["id"] in st.session_state.get("cupons_usados_ids", [])
        
    return cupons_base

def carregar_conquistas():
    """
    Lista de Medalhas da Sara. Valida se ela conquistou cada uma
    olhando direto no histórico persistente do banco de dados.
    """
    cupons_usados = st.session_state.get("cupons_usados_ids", [])
    
    # Regras dinâmicas para desbloqueio
    cafune_desbloqueado = 4 in cupons_usados   # ID 4 é o cupom de cafuné
    cinema_desbloqueado = 3 in cupons_usados   # ID 3 é o cupom de cinema
    nivel_rpg = st.session_state.get("nivel_atual", 1)

    conquistas = [
        {
            "id": "primeiro_passo",
            "titulo": "✨ O Início de Tudo",
            "descricao": "Abra o aplicativo e explore o Universo do Casal.",
            "icone": "🚀",
            "desbloqueada": True
        },
        {
            "id": "cafune_master",
            "titulo": "🥇 Maratonista de Cafuné",
            "descricao": "Resgate o Cupom de Cafuné Unlimited na máquina de vouchers.",
            "icone": "💆‍♀️",
            "desbloqueada": cafune_desbloqueado
        },
        {
            "id": "critica_cinema",
            "titulo": "🍿 Crítica de Cinema",
            "descricao": "Resgate o Cupom de Cinema em Casa para uma noite de filmes.",
            "icone": "🎬",
            "desbloqueada": cinema_desbloqueado
        },
        {
            "id": "mestre_rpg",
            "titulo": "⚔️ Guerreira de Elite",
            "descricao": "Evolua o seu nível de RPG de Casal até o Nível 3.",
            "icone": "👑",
            "desbloqueada": nivel_rpg >= 3
        }
    ]
    
    # Atualiza a lista oficial de IDs salvos para guardar no arquivo JSON
    st.session_state["conquistas_ids"] = [c["id"] for c in conquistas if c["desbloqueada"]]
    salvar_progresso_banco()
    
    return conquistas

def adicionar_xp(quantidade):
    if "xp_atual" not in st.session_state:
        carregar_progresso_banco()
        
    st.session_state["xp_atual"] += quantidade
    
    # Sistema de Level Up (Cada 100 de XP = 1 Nível)
    while st.session_state["xp_atual"] >= 100:
        st.session_state["xp_atual"] -= 100
        st.session_state["nivel_atual"] += 1
        st.toast(f"🎉 PARABÉNS! Você subiu para o Nível {st.session_state['nivel_atual']}!", icon="⭐")
        
    # Salva fisicamente o novo XP no JSON!
    salvar_progresso_banco()
