import streamlit as st
import base64
from test import pagina_formulario

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ruta a tu imagen local
img_path = "assets/main.png"
img_base64 = get_base64_of_bin_file(img_path)

if "page" not in st.session_state:
    st.session_state.page = "home"

st.markdown(f"""
<style>    
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    }}

    .main-container {{
        display: grid;
        justify-content: center;
        align-items: center;
        height: 50vh;
        width: 100%;
        margin-top: 10px;
        grid-template-rows: 1fr 1fr;
        grid-template-columns: 1fr 1fr;
        gap: 50px;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        position: relative;
    }}
    
    .title {{
        justify-content:center;
        margin-top: 30px;
        grid-column: 1 / 3;
        grid-row: 1 / 2;
        font-family: Georgia, serif;
        color: rgb(202, 48, 1);
        font-size: 60px; 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin: 0;
        padding: 10px; 
        display: flex;
        align-items: center;
        justify-content: center;
        height: fit-content;
        box-sizing: border-box;
    }}
    
    /* CONTENEDOR FLEX PARA BOTONES PEGADOS A EXTREMOS */
    .buttons-container {{
        grid-column: 1 / 3;
        grid-row: 2 / 3;
        display: flex;
        justify-content: space-between; /* ← UNO IZQUIERDA, OTRO DERECHA */
        align-items: center;
        width: 100%;
        padding: 0px; /* Ajusta este padding según necesites */
        box-sizing: border-box;
    }}
    
     /* ESTILOS PARA LOS BOTONES DE STREAMLIT */
    div.stButton > button:first-child {{
        letter-spacing: 1px;
        font-weight: 900 !important;
        font-family: Georgia, serif !important;
        color: rgb(255, 255, 255) !important;
        font-size: 40px !important; 
        background-color: rgb(202, 48, 1) !important;
        width: 220px !important;
        border-radius: 15px !important;
        box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.7) !important;
        padding: 15px !important;
        cursor: pointer !important;
        transition: transform 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        border: none !important;
        text-decoration: none !important;
        height: auto !important;
        min-height: 70px !important;
    }}
    
    div.stButton > button:first-child:hover {{
        transform: scale(1.1) !important;
        background-color: rgb(170, 40, 0) !important;
        box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.9) !important;
        text-decoration: none !important;
    }}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "home":
    # Contenedor principal
    st.markdown("""
    <div class="main-container">
        <div class="title">How to manager your dragon</div>
        <div class="buttons-container">
    """, unsafe_allow_html=True)

    # Crear un contenedor flex dentro del grid
    col1, spacer, col2 = st.columns([1, 1, 1])

    with col1:
        # Botón izquierdo - PEGADO A LA IZQUIERDA
        if st.button("Añadir evento", key="new_event_btn"):
            st.session_state.page = "añadir_evento"
            st.rerun()

    with col2:
        # Botón derecho - PEGADO A LA DERECHA
        if st.button("Eventos activos", key="edit_events_btn"):
            st.session_state.page = "eventos_activos"
            st.rerun()

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Router de páginas ---
page = st.session_state.page

if page == "añadir_evento":
    pagina_formulario()
# elif page == "eventos_activos":
#     pagina_eventos_activos()
else:
    # Home por defecto (título y botones que ya tienes)
    pass
