from models import *
import streamlit as st

st.set_page_config(
    page_title="🐉 Gestor de Eventos de Berk",
    page_icon="🐉",
    layout="wide"
)

st.sidebar.title("🐉 Navegación")
pagina = st.sidebar.radio(
    "Selecciona una página:",
    ["🏠 Inicio", "📅 Crear Evento", "📋 Eventos Programados", "📊 Recursos", "🐲 Dragones y Guerreros"]
)
