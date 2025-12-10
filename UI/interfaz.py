import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    
    style = f"""
    <style>
    /* ELIMINAR TODOS LOS ELEMENTOS DE STREAMLIT */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
    .stToolbar {{display:none;}}
    .stStatusWidget {{display:none;}}
    
    .stApp {{
        background-image: url("data:image/png;base64,{b64_encoded}");
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        min-height: 100vh;
        overflow: hidden;
    }}
    
    /* ELIMINAR PADDING DE STREAMLIT */
    .main .block-container {{
        padding-top: 0px;
        padding-bottom: 0px;
        padding-left: 0px;
        padding-right: 0px;
        max-width: 100%;
    }}
    
    .main-container {{
        display: grid;
        justify-content: center;
        align-items: baseline;
        height: 100vh;
        width: 50%;
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
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        color: rgb(202, 48, 1);
        font-size: 60px; 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin: 0;
        padding: 25px; 
        display: flex;
        align-items: center;
        justify-content: center;
        height: fit-content;
        box-sizing: border-box;
    }}
    
    .new-event-btn {{
        grid-row: 2 / 3;
        grid-column: 1;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        color: rgb(202, 48, 1);
        font-size: 25px; 
        background-color: rgb(255, 255, 255);
        width: 220px; /* Reducido de 220px */
        border-radius: 10px;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        padding: 15px; 
        cursor: pointer;
        transition: transform 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0;
        box-sizing: border-box;
        border: none;
        text-decoration: none; /* Elimina subrayado */
    }}
    
    .new-event-btn:hover {{
        transform: scale(1.1);
        text-decoration: none; /* Elimina subrayado en hover */
    }}
    
    .edit-events-btn {{
        grid-row: 2 / 3;
        grid-column: 2;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        color: rgb(202, 48, 1);
        font-size: 25px; /* Reducido de 30px */
        background-color: rgb(255, 255, 255);
        width: 220px; /* Reducido de 220px */
        border-radius: 10px;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        padding: 15px; /* Reducido */
        cursor: pointer;
        transition: transform 0.3s ease;
        justify-self: end;
        margin-top: 90px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        border: none;
        text-decoration: none; /* Elimina subrayado */
    }}
    
    .edit-events-btn:hover {{
        transform: scale(1.1);
        text-decoration: none; /* Elimina subrayado en hover */
    }}
    
    /* ELIMINAR SCROLL COMPLETAMENTE */
    html, body, [data-testid="stAppViewContainer"] {{
        overflow: hidden !important;
    }}
    
    section.main > div:first-child {{
        padding-top: 0 !important;
    }}
    
    /* OCULTAR ELEMENTOS DE STREAMLIT QUE CREAN ESPACIO */
    div[data-testid="stVerticalBlock"] {{
        gap: 0px;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Gestor de Eventos de Berk",
        page_icon="🐉",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Ocultar más elementos de Streamlit
    hide_streamlit_style = """
        <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        div[data-testid="stToolbar"] { display: none; }
        .stAlert { display: none; }
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Establecer el fondo
    set_background("main.png")
    
    # Crear la estructura usando divs en lugar de enlaces para eliminar subrayado
    st.markdown("""
        <div class="main-container">
            <div class="title">How to manager your dragon</div>
            <div class="new-event-btn" onclick="handleNewEvent()">Añadir evento</div>
            <div class="edit-events-btn" onclick="handleEditEvents()">Eventos activos</div>
        </div>
        
        <script>
        function handleNewEvent() {
            // Aquí puedes redirigir o mostrar un modal
            alert("Añadir evento");
        }
        
        function handleEditEvents() {
            // Aquí puedes redirigir o mostrar un modal  
            alert("Eventos activos clickeado");
        }
        </script>
    """, unsafe_allow_html=True)
    
    # Espacio oculto para evitar que Streamlit añada elementos automáticamente
    st.markdown("<div style='display:none'>.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()