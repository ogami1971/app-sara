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
    elogios = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=123456")
    missoes = ler_aba_csv(f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=789101")
    
    if not capa: 
        capa = [{"Titulo_App": "Nosso Universo", "Subtitulo_App": "Bem-vinda, minha rosa."}]
    if not elogios: 
        elogios = [{"Frase": "Você é o meu momento favorito do dia!"}, {"Frase": "Seu sorriso ilumina meu world."}]
    if not missoes: 
        missoes = [
            {"ID": "1", "Titulo": "Cozinhar algo juntos", "Tipo_Missao": "Média", "Status": "Pendente", "Gif": "comida.gif"},
            {"ID": "2", "Titulo": "Assistir um filme cobertos", "Tipo_Missao": "Fácil", "Status": "Concluída", "Gif": "coberta.gif"}
        ]
    return capa[0], elogios, missoes
