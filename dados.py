import streamlit as st
import pandas as pd
import json
import os

def carregar_dados():
    """
    Conecta diretamente com a sua planilha do Google Sheets e puxa os dados reais
    das abas 'Capa_app', 'Banco_De_Elogios', 'Missoes_Romanticas' e 'Cupons_Romanticos'.
    """
    ID_PLANILHA = "11_R_3hNyr18YPPdHzM58iEKxG7_uorm0TBaHIeg36F8"
    
    url_capa = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/gviz/tq?tqx=out:csv&sheet=Capa_app"
    url_elogios = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/gviz/tq?tqx=out:csv&sheet=Banco_De_Elogios"
    url_missoes = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/gviz/tq?tqx=out:csv&sheet=Missoes_Romanticas"
    url_cupons = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/gviz/tq?tqx=out:csv&sheet=Cupons_Romanticos"
    
    try:
        df_capa = pd.read_csv(url_capa)
        if not df_capa.empty:
            capa_data = df_capa.iloc[0].to_dict()
        else:
            capa_data = {"Titulo_App": "App Pequeno Príncipe - Sara", "Subtitulo_App": "Bem-vinda ao nosso universo!"}
    except Exception:
        capa_data = {"Titulo_App": "App Pequeno Príncipe - Sara", "Subtitulo_App": "Bem-vinda ao nosso universo!"}
        
    try:
        df_elogios_raw = pd.read_csv(url_elogios)
        df_elogios = df_elogios_raw.to_dict(orient="records")
    except Exception:
        df_elogios = []

    try:
        df_missoes = pd.read_csv(url_missoes)
    except Exception:
        df_missoes = pd.DataFrame(columns=["ID_Missao", "Missao", "Concluida", "Tipo_Missao"])
        
    try:
        # 📊 Puxa a nova aba de cupons direto da planilha
        df_cupons = pd.read_csv(url_cupons)
    except Exception:
        # Caso a aba ainda não exista ou dê erro, cria um DataFrame reserva vazio
        df_cupons = pd.DataFrame(columns=["ID_Cupom", "Titulo", "Descricao"])
    
    return capa_data, df_elogios, df_missoes, df_cupons

# ------------------------------------------------------------------
# 🎰 SISTEMA DE BANCO DE DADOS PERSISTENTE (JSON)
# ------------------------------------------------------------------

ARQUIVO_BANCO = "progresso_sara.json"

def inicializar_banco_local():
    if not os.path.exists(ARQUIVO_BANCO):
        dados_iniciais = {
            "xp": 0,
            "nivel": 1,
            "cupons_usados": [],
            "conquistas_desbloqueadas": ["primeiro_passo"]
        }
        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f:
            json.dump(dados_iniciais, f, indent=4, ensure_ascii=False)

def carregar_progresso_banco():
    inicializar_banco_local()
    
    try:
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as f:
            dados_carregados = json.load(f)
            
        st.session_state["xp_atual"] = dados_carregados.get("xp", 0)
        st.session_state["nivel_atual"] = dados_carregados.get("nivel", 1)
        st.session_state["cupons_usados_ids"] = dados_carregados.get("cupons_usados", [])
        st.session_state["conquistas_ids"] = dados_carregados.get("conquistas_desbloqueadas", ["primeiro_passo"])
    except Exception:
        if "xp_atual" not in st.session_state: st.session_state["xp_atual"] = 0
        if "nivel_atual" not in st.session_state: st.session_state["nivel_atual"] = 1
        if "cupons_usados_ids" not in st.session_state: st.session_state["cupons_usados_ids"] = []
        if "conquistas_ids" not in st.session_state: st.session_state["conquistas_ids"] = ["primeiro_passo"]

def salvar_progresso_banco():
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
# 🎟️ GERENCIADORES DE CONTEÚDO (INTEGRAÇÃO DINÂMICA)
# ------------------------------------------------------------------

def processar_cupons_dinamicos(df_cupons):
    """
    Recebe os cupons vindos do Sheets e cruza com os IDs salvos localmente
    no progresso_sara.json para saber o que já foi usado.
    """
    if "cupons_usados_ids" not in st.session_state:
        carregar_progresso_banco()
        
    if df_cupons is None or (hasattr(df_cupons, "empty") and df_cupons.empty):
        return []
        
    # Converte o DataFrame para lista de dicionários
    lista_bruta = df_cupons.to_dict(orient="records") if hasattr(df_cupons, "to_dict") else df_cupons
    cupons_formatados = []
    
    for idx, c in enumerate(lista_bruta):
        id_original = c.get("ID_Cupom", idx + 1)
        
        cupom_dict = {
            "id": int(id_original),
            "titulo": c.get("Titulo", "Cupom Sem Nome 🎟️"),
            "descricao": c.get("Descricao", "Nenhuma descrição informada."),
            "usado": int(id_original) in st.session_state.get("cupons_usados_ids", [])
        }
        cupons_formatados.append(cupom_dict)
        
    return cupons_formatados

def carregar_conquistas():
    cupons_usados = st.session_state.get("cupons_usados_ids", [])
    
    cafune_desbloqueado = 4 in cupons_usados   
    cinema_desbloqueado = 3 in cupons_usados   
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
    
    st.session_state["conquistas_ids"] = [c["id"] for c in conquistas if c["desbloqueada"]]
    salvar_progresso_banco()
    
    return conquistas

def adicionar_xp(quantidade):
    if "xp_atual" not in st.session_state:
        carregar_progresso_banco()
        
    st.session_state["xp_atual"] += quantidade
    
    while st.session_state["xp_atual"] >= 100:
        st.session_state["xp_atual"] -= 100
        st.session_state["nivel_atual"] += 1
        st.toast(f"🎉 PARABÉNS! Você subiu para o Nível {st.session_state['nivel_atual']}!", icon="⭐")
        
    salvar_progresso_banco()
