import streamlit as st
import base64
import datetime
from datetime import time
from models.creador_de_eventos import Evento
from models.gestor_de_recursos import GestorEventos
from models.validador_de_fechas import *
from models.validador_de_reglas import *

# Inicializar gestor (puedes usar st.session_state para persistencia)
if "gestor" not in st.session_state:
    st.session_state.gestor = GestorEventos()

gestor = st.session_state.gestor

def pagina_formulario():
    st.markdown("<h2 style='text-align: center; background-color:rgb(202, 48, 1), font-family: Georgia, serif;'>Crea tu nuevo evento</h2>", unsafe_allow_html=True)


    # Convertir la imagen local a base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Ruta a tu imagen local
    img_path = "assets/main.png"
    img_base64 = get_base64_of_bin_file(img_path)

    # Inyectar CSS con la imagen de fondo y formulario semitransparente
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    }}

    div[data-testid="stForm"] {{
        background-color: rgba(255, 255, 255, 0.60); /* blanco semitransparente */
        padding: 20px;
        border-radius: 12px;
    }}
    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
    <style>
    label[data-testid="stWidgetLabel"] {
        display: flex;
        justify-content: center;
        text-align: center;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
    <style>          
    /* Aplicar fuente a elementos específicos */

    /* 1. Contenido principal de la app */
    .stApp, .block-container, .main, 
    .stTextInput, .stSelectbox, .stDateInput, .stTimeInput,
    .stMultiSelect, .stNumberInput, .stButton,
    .stMarkdown:not(.st-emotion-cache-16txtl3),
    .stSubheader {
        font-family: Georgia, serif !important;
    }

    /* 2. Labels de formularios */
    label[data-testid="stWidgetLabel"] p {
        font-family: Georgia, serif !important;
        font-size: 16px !important;
        color: #2a1a0a !important;
    }

    /* 3. Inputs y controles */
    input, select, textarea, button:not(.streamlit-expanderHeader) {
        font-family: Georgia, serif !important;
        font-size: 16px !important;
    }

    /* 4. Contenido dentro de expanders EXCLUYENDO el header */
    div[data-testid="stExpander"] div[role="region"] * {
        font-family: Georgia, serif !important;
        font-size: 16px !important;
    }

    /* 5. CRUCIAL: Excluir COMPLETAMENTE el header del expander */
    div[data-testid="stExpander"] > details > summary,
    div[data-testid="stExpander"] div[role="button"],
    div[data-testid="stExpander"] .streamlit-expanderHeader,
    div[data-testid="stExpander"] button[data-testid="baseButton-header"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        all: revert !important;
    }

    /* 6. Asegurar que los íconos dentro del header usen la fuente Material Icons */
    div[data-testid="stExpander"] .streamlit-expanderHeader svg,
    div[data-testid="stExpander"] button[data-testid="baseButton-headerNoPadding"] svg {
        font-family: "Material Icons" !important;
    }

    /* 7. Texto dentro del expander header */
    div[data-testid="stExpander"] div[role="button"] p,
    div[data-testid="stExpander"] .st-emotion-cache-16txtl3 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        font-weight: 600 !important;
    }

    /* 8. ELIMINAR LA FLECHA NEGRA ADICIONAL (pseudo-elemento ::before) */
    div[data-testid="stExpander"] .streamlit-expanderHeader::before,
    div[data-testid="stExpander"] div[role="button"]::before,
    div[data-testid="stExpander"] button::before {
        content: none !important;
        display: none !important;
    }

    /* 9. Eliminar cualquier otro pseudo-elemento que pueda causar flechas dobles */
    div[data-testid="stExpander"] summary::before,
    div[data-testid="stExpander"] summary::marker,
    div[data-testid="stExpander"] summary::-webkit-details-marker {
        display: none !important;
        content: "" !important;
    }

    /* 10. Asegurar que solo quede el ícono de Material Icons */
    div[data-testid="stExpander"] .streamlit-expanderHeader {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }

    /* 11. Opcional: Mejorar el espaciado entre el emoji y el texto */
    div[data-testid="stExpander"] div[role="button"] {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)



    # --- Formulario para crear evento ---
    with st.form("crear_evento"):
        title = st.text_input("Título del evento")
        type_of_event = st.selectbox("Tipo de evento", gestor.type_of_events)
        arena = st.selectbox("Arena", gestor.arenas)

        col1, col2 = st.columns(2) 
        with col1: 
            start_date = st.date_input("Fecha de inicio", datetime.today()) 
            start_time = st.time_input("Hora de inicio", time(10, 0)) 
        with col2: 
            finish_date = st.date_input("Fecha de fin", datetime.today()) 
            finish_time = st.time_input("Hora de fin", time(10, 0))

        warriors = st.multiselect("Guerreros de la saga", gestor.franquicia_warriors)
        dragons = st.multiselect("Dragones de la saga", gestor.franquicia_dragons)

        with st.expander("⚔️ Guerreros de Berk"):
            randoms_selected = {}
            for grupo, cantidad in gestor.randoms_warriors.items():
                randoms_selected[grupo] = st.number_input(
                    f"{grupo} (disponibles: {cantidad})", 
                    min_value=0, max_value=cantidad, value=0
                )

        with st.expander("🐉 Dragones libres"):
            free_dragons_selected = {}
            for dragon, cantidad in gestor.free_dragons.items():
                free_dragons_selected[dragon] = st.number_input(
                    f"{dragon} (disponibles: {cantidad})", 
                    min_value=0, max_value=cantidad, value=0
                )

        col_armas, col_armaduras = st.columns(2)

        with col_armas:
            with st.expander("🛡️ Armas"):
                weapons_selected = {}
                for arma, cantidad in gestor.weapons.items():
                    weapons_selected[arma] = st.number_input(
                        f"{arma} (disponibles: {cantidad})", 
                        min_value=0, max_value=cantidad, value=0
                    )

        with col_armaduras:
            with st.expander("🥋 Armaduras"):
                armors_selected = {}
                for armadura, cantidad in gestor.armors.items():
                    armors_selected[armadura] = st.number_input(
                        f"{armadura} (disponibles: {cantidad})", 
                        min_value=0, max_value=cantidad, value=0
                    )

        with st.expander("🐑 Ovejas"):
            ovejas_selected = st.number_input(
                f"Ovejas (disponibles: {gestor.ovejas})", 
                min_value=0, max_value=gestor.ovejas, value=0
            )

        # --- Botones en extremos ---
        col_left, col_spacer, col_right = st.columns([1,2,1])

        with col_left:
            submitted = st.form_submit_button("Guardar evento")

        with col_right:
            reset = st.form_submit_button("Borrar formulario")

        # Lógica de los botones
        if reset:
            st.session_state.clear()
            st.rerun()



        if submitted:
            # Validaciones básicas
            disponible = True  # aquí podrías llamar a verificar_disponibilidad_arena
            participacion_ok, msg = verificar_participacion_diaria(warriors, dragons, str(start_date))

            if not participacion_ok:
                st.error(msg)
            else: 
                evento = Evento( title, start_date, start_time, finish_date, finish_time, type_of_event, arena, warriors + sum([[w]*c for w,c in randoms_selected.items()], []), dragons + sum([[d]*c for d,c in free_dragons_selected.items()], []), [w for w,c in weapons_selected.items() for _ in range(c)], [a for a,c in armors_selected.items() for _ in range(c)], ovejas_selected ) 
                gestor.eventos.append(evento) 
                # Restar recursos del almacén 
                for grupo, cantidad in randoms_selected.items(): 
                    gestor.randoms_warriors[grupo] -= cantidad 
                for dragon, cantidad in free_dragons_selected.items(): 
                    gestor.free_dragons[dragon] -= cantidad 
                for arma, cantidad in weapons_selected.items(): 
                    gestor.weapons[arma] -= cantidad 
                for armadura, cantidad in armors_selected.items(): 
                    gestor.armors[armadura] -= cantidad 
                gestor.ovejas -= ovejas_selected 
                st.success(f"Evento '{title}' creado exitosamente 🎉")

    st.markdown("""
    <div class=extra_btns>
    """, unsafe_allow_html=True)

    col1, spacer, col2 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("Menú principal", key="main_menu"):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("Eventos activos", key="edit_events_btn"):
            st.session_state.page = "eventos_activos"
            st.rerun()

    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
