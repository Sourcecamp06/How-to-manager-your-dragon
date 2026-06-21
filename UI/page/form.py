import streamlit as st
import base64
import os
import datetime
from datetime import time
from models.creador_de_eventos import Evento
from models.gestor_de_recursos import GestorEventos
from models.validador_de_reglas import *

def pagina_formulario():
    if "gestor" not in st.session_state:
        st.session_state.gestor = GestorEventos()

    gestor = st.session_state.gestor
    
    st.markdown("""<h2 class="header">Crea tu nuevo evento</h2>""", unsafe_allow_html=True)

    st.markdown(f"""
    <style>
        .header{{
            justify-content:center;
            margin-top: 30px;
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
    </style>
    """,  unsafe_allow_html=True)

    #Convertir la imagen local a base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img_path = "assets/main.png"
    img_base64 = get_base64_of_bin_file(img_path)

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
    div.stButton > button:first-child {
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
}
    
    div.stButton > button:first-child:hover {
        transform: scale(1.1) !important;
        background-color: rgb(170, 40, 0) !important;
        box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.9) !important;
        text-decoration: none !important;
    }

    .stApp, .block-container, .main, 
    .stTextInput, .stSelectbox, .stDateInput, .stTimeInput,
    .stMultiSelect, .stNumberInput, .stButton,
    .stMarkdown:not(.st-emotion-cache-16txtl3),
    .stSubheader {
        font-family: Georgia, serif !important;
    }

    label[data-testid="stWidgetLabel"] p {
        font-family: Georgia, serif !important;
        font-size: 16px !important;
        color: #2a1a0a !important;
    }

    input, select, textarea, button:not(.streamlit-expanderHeader) {
        font-family: Georgia, serif !important;
        font-size: 16px !important;
    }

    div[data-testid="stExpander"] div[role="region"] * {
        font-family: Georgia, serif !important;
        font-size: 16px !important;
    }

    div[data-testid="stExpander"] > details > summary,
    div[data-testid="stExpander"] div[role="button"],
    div[data-testid="stExpander"] .streamlit-expanderHeader,
    div[data-testid="stExpander"] button[data-testid="baseButton-header"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        all: revert !important;
    }

    div[data-testid="stExpander"] .streamlit-expanderHeader svg,
    div[data-testid="stExpander"] button[data-testid="baseButton-headerNoPadding"] svg {
        font-family: "Material Icons" !important;
    }

    div[data-testid="stExpander"] div[role="button"] p,
    div[data-testid="stExpander"] .st-emotion-cache-16txtl3 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        font-weight: 600 !important;
    }

    div[data-testid="stExpander"] .streamlit-expanderHeader::before,
    div[data-testid="stExpander"] div[role="button"]::before,
    div[data-testid="stExpander"] button::before {
        content: none !important;
        display: none !important;
    }

    div[data-testid="stExpander"] summary::before,
    div[data-testid="stExpander"] summary::marker,
    div[data-testid="stExpander"] summary::-webkit-details-marker {
        display: none !important;
        content: "" !important;
    }

    div[data-testid="stExpander"] .streamlit-expanderHeader {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }

    div[data-testid="stExpander"] div[role="button"] {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }

    .header{
        justify-content:center;
        margin-top: 30px;
        font-family: Georgia, serif;
        color: rgb(202, 48, 1) !important;
        font-size: 60px !important; 
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
    }
    </style>
    """, unsafe_allow_html=True)


    #Formulario para crear evento
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
        
        warriors = []
        
        with st.expander("⚔️ Guerreros de la saga", expanded=False):
            st.markdown("""
            <style>
            div[data-testid="stColumn"] label p {
                font-size: 12px !important;
                white-space: nowrap; 
                overflow: hidden;
                text-overflow: ellipsis;
            }
            div[data-testid="stColumn"] img {
                width: 80px !important;
                height: 80px !important;
                object-fit: contain !important;
            }
            </style>
            """, unsafe_allow_html=True)

            cols = st.columns(4)
            for i, (warrior, img_path) in enumerate(gestor.franquicia_warriors.items()):
                with cols[i % 4]:
                    
                    st.image(img_path, width=80)
                    
                    key_name = f"chk_warrior_{warrior}"
                    if st.checkbox(warrior, key=key_name):
                        warriors.append(warrior)
        
        dragons = []
        
        with st.expander("🐉 Dragones de la saga", expanded=False):
            st.markdown("""
            <style>
            div[data-testid="stColumn"] label p {
                font-size: 12px !important;
                white-space: nowrap; 
                overflow: hidden;
                text-overflow: ellipsis;
            }
            div[data-testid="stColumn"] img {
                width: 80px !important;
                height: 80px !important;
                object-fit: contain !important;
            }
            </style>
            """, unsafe_allow_html=True)

            cols = st.columns(4)
            for i, (dragon, img_path) in enumerate(gestor.franquicia_dragons.items()):
                with cols[i % 4]:
                    
                    st.image(img_path, width=80)
                    
                    key_name = f"chk_dragon_{dragon}"
                    if st.checkbox(dragon, key=key_name):
                        dragons.append(dragon)
        
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
                    c1, c2 = st.columns([1, 5], gap="small")
                    with c1:
                        if hasattr(gestor, 'weapons_images') and arma in gestor.weapons_images:
                            st.image(gestor.weapons_images[arma], width=100)
                    with c2:
                        weapons_selected[arma] = st.number_input(
                            f"{arma} (disponibles: {cantidad})", 
                            min_value=0, max_value=cantidad, value=0, label_visibility="collapsed"
                        )

        with col_armaduras:
            with st.expander("🥋 Armaduras"):
                armors_selected = {}
                for armadura, cantidad in gestor.armors.items():
                    c1, c2 = st.columns([1, 5], gap="small")
                    with c1:
                        if hasattr(gestor, 'armors_images') and armadura in gestor.armors_images:
                            st.image(gestor.armors_images[armadura], width=100)
                    with c2:
                        armors_selected[armadura] = st.number_input(
                            f"{armadura} (disponibles: {cantidad})", 
                            min_value=0, max_value=cantidad, value=0, label_visibility="collapsed"
                        )

        with st.expander("🐑 Ovejas"):  
                c1, c2 = st.columns([1, 5], gap="small")
                with c1:
                    st.image("assets/sheeps/oveja.png", width=100)
                with c2:
                    ovejas_selected = st.number_input(
                    f"Ovejas (disponibles: {gestor.ovejas})", 
                    min_value=0, max_value=gestor.ovejas, value=0
                )

        col_left, col_spacer, col_right = st.columns([1,2,1])

        with col_left:
            submitted = st.form_submit_button("Guardar evento")

        with col_right:
            reset = st.form_submit_button("Borrar formulario")

        if reset:
            st.session_state.clear()
            st.rerun()

        if submitted:
            #verificar que sea un evento futuro, no en una fecha q ya paso y q la fecha de inicio sea menor q la de fin
            actual_date=datetime.now().date()
            actual_time=datetime.now().time()
            fecha_actual = datetime.combine(actual_date, actual_time)
            fecha_escogida_inicial = (datetime.combine(start_date, start_time))
            fecha_escogida_final = (datetime.combine(finish_date, finish_time))
            if actual_date >= start_date:
                st.error("Tienes que planificar los eventos con al menos un día de antelación")
                st.stop()

            if fecha_escogida_inicial > fecha_escogida_final:
                st.error("La fecha inicial no puede ser mayor que la final")
                st.stop()


            #Verificar nombre del evento
            if not title.strip():
                st.error("El evento debe tener un nombre")
                st.stop()

            for evento_existente in gestor.eventos:
                if evento_existente.title == title:
                    st.error(f"Ya existe un evento con el nombre '{title}'")
                    st.stop()
            
            #duracion del evento
            if gestor.duration(start_date, start_time, finish_date, finish_time) == 0:
                st.error("El evento no puede durar 0 minutos")
                st.stop()

            #Regla 1: Verificar disponibilidad de arena
            disponibilidad_arena, msg= gestor.verificar_disponibilidad_arena(arena, start_date, start_time, finish_date, finish_time)
            if not disponibilidad_arena:
                st.error(msg)
                st.info(gestor.recomendar_fecha(arena, start_date, start_time, finish_date, finish_time))
                st.stop()

            #Regla 2: Verificar participacion diaria
            participacion_diaria, msg = verificar_participacion_diaria(gestor, warriors, dragons, start_date) 
            if not participacion_diaria: 
                st.error(msg) 
                st.stop()

            #Regla 3: Verificar dragones con sus guerreros
            dragones_con_sus_guerreros, msg = verificar_dragones_con_su_guerrero(gestor, warriors, dragons, type_of_event) 
            if not dragones_con_sus_guerreros: 
                st.error(msg) 
                st.stop()

            #Regla 4: Verificacion del Cremallerus
            cremallerus_ok, msg = verificacion_del_cremallerus(gestor, type_of_event, dragons, free_dragons_selected, warriors, randoms_selected) 
            if not cremallerus_ok: 
                st.error(msg) 
                st.stop()

            #Regla 5: Verificacion del evento de las ovejas
            ovejas_ok, msg = verificacion_evento_ovejas(gestor, type_of_event, arena, ovejas_selected) 
            if not ovejas_ok: 
                st.error(msg) 
                st.stop()
            
            #Regla 6: Verificacion del evento excursion
            excursion_ok, msg = verificacion_evento_excursion(gestor, type_of_event, arena) 
            if not excursion_ok: 
                st.error(msg) 
                st.stop()

            #Regla 7: Verificacion de dragones obligatorios
            oblig_ok, msg = verificacion_dragones_obligatorios(gestor, type_of_event, free_dragons_selected, dragons)
            if not oblig_ok:
                st.error(msg)
                st.stop()
                
            #Regla 8: Verificacion de dragones innecesarios
            innece_ok, msg = verificacion_no_dragones(gestor, type_of_event, free_dragons_selected, dragons)
            if not innece_ok:
                st.error(msg)
                st.stop()

            #Regla 9: colision de personajes
            colisiones_ok, msg = colision_personajes(gestor, warriors)
            if not colisiones_ok:
                st.error(msg)
                st.stop()

            else: 
                new_evento = Evento( 
                    title=title, 
                    start_date=start_date,
                    start_time=start_time, 
                    finish_date=finish_date, 
                    finish_time=finish_time, 
                    type_of_event=type_of_event, 
                    arena=arena,
                    franquicia_warriors=warriors,
                    randoms_warriors=sum([[w]*c for w,c in randoms_selected.items()], []), 
                    franquicia_dragons=dragons,
                    free_dragons=sum([[d]*c for d,c in free_dragons_selected.items()], []), 
                    weapons=[w for w,c in weapons_selected.items() for _ in range(c)], 
                    armors=[a for a,c in armors_selected.items() for _ in range(c)], 
                    extra=ovejas_selected 
                    ) 
                gestor.eventos.append(new_evento) 

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

                if start_date not in gestor.daily_participation: 
                    gestor.daily_participation[start_date] = {"guerreros": set(), "dragones": set()} 
                gestor.daily_participation[start_date]["guerreros"].update(new_evento.franquicia_warriors) 
                gestor.daily_participation[start_date]["dragones"].update(new_evento.franquicia_dragons)


                gestor.guardar_en_json()
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
