import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ruta a tu imagen local
img_path = "assets/main.png"
img_base64 = get_base64_of_bin_file(img_path)

st.markdown("""
<style>    
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
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
</style>
""", unsafe_allow_html=True)

st.markdown("""
        <div class="main-container">
            <div class="title">How to manager your dragon</div>
            <div class="new-event-btn" onclick="handleNewEvent()">Añadir evento</div>
            <div class="edit-events-btn" onclick="handleEditEvents()">Eventos activos</div>
        </div>
    """, unsafe_allow_html=True)

