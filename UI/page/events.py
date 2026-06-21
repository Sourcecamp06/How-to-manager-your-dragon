import streamlit as st
import base64
import json
import random
from models.gestor_de_recursos import GestorEventos
from models.creador_de_eventos import Evento

def pagina_eventos_activos():
    # Inicializar gestor
    if 'gestor' not in st.session_state:
        st.session_state.gestor = GestorEventos()
    gestor = st.session_state.gestor
    eventos = gestor.eventos

    # Fondo
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
    .header {{
        font-family: Georgia, serif !important;
        color: rgb(202, 48, 1) !important;
        font-size: 55px !important; 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        margin: 30px auto 40px auto !important;
        text-align: center !important;
        padding: 10px !important; 
        align-items: center !important;
        justify-content: center !important;
        height: fit-content !important;
        box-sizing: border-box !important;
    }}
    div[data-testid="stExpander"] {{
        border: none !important;
        box-shadow: none !important;
    }}

    div[data-testid="stExpander"] details {{
        background-color: rgba(255, 255, 255, 0.60) !important;
        border-radius: 12px !important;
        border: none !important;
        margin-bottom: 10px !important;
    }}
    div[data-testid="stExpander"] p, div[data-testid="stExpander"] span, div[data-testid="stExpander"] div {{
        color: black !important;
    }}
    div[data-testid="stExpander"] details:hover {{
        background-color: rgba(255, 255, 255, 0.70) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h2 class='header'>Eventos activos</h2>", unsafe_allow_html=True)

    def cargar_eventos(): 
        try: 
            with open("data/eventos.json", "r", encoding="utf-8") as f: 
                data = json.load(f) 
                return [Evento(**evento) for evento in data] 
        except FileNotFoundError: 
            return []


    #Lista de eventos
    if eventos:
        for idx, ev in enumerate(eventos):
            with st.expander(f"🗡️ {ev.title} — {ev.type_of_event} ({ev.arena})"):
                st.markdown(f"**📅 Inicio:** {ev.start_date} {ev.start_time}")
                st.markdown(f"**📅 Fin:** {ev.finish_date} {ev.finish_time}")

                st.markdown("**⚔️ Guerreros:**")
                if ev.warriors:
                    warriors_with_img = [w for w in ev.warriors if w in gestor.franquicia_warriors]
                    other_warriors = [w for w in ev.warriors if w not in gestor.franquicia_warriors]

                    #Mostrar imágenes
                    if warriors_with_img:
                        cols = st.columns(6)
                        for i, w in enumerate(warriors_with_img):
                            with cols[i % 6]:
                                img_path = gestor.franquicia_warriors[w]
                                try:
                                    b64_img = get_base64_of_bin_file(img_path)
                                    st.markdown(f'<img src="data:image/png;base64,{b64_img}" style="width:80px; height:80px; object-fit:contain; display:block; margin: 0 auto;">', unsafe_allow_html=True)
                                except:
                                    st.image(img_path, width=80)
                                st.markdown(f"<div style='text-align: center; color: grey; font-size: small;'>{w}</div>", unsafe_allow_html=True)
                    
                    #Mostrar el resto como texto
                    if other_warriors:
                        st.write(", ".join(other_warriors))
                else:
                    st.write("—")

                st.markdown("**🐉 Dragones:**")
                if ev.dragons:
                    dragons_with_img = [d for d in ev.dragons if d in gestor.franquicia_dragons]
                    other_dragons = [d for d in ev.dragons if d not in gestor.franquicia_dragons]

                    if dragons_with_img:
                        cols = st.columns(6)
                        for i, d in enumerate(dragons_with_img):
                            with cols[i % 6]:
                                #Renderizar imagen con estilo inline especifico
                                img_path = gestor.franquicia_dragons[d]
                                try:
                                    b64_img = get_base64_of_bin_file(img_path)
                                    st.markdown(f'<img src="data:image/png;base64,{b64_img}" style="width:80px; height:80px; object-fit:contain; display:block; margin: 0 auto;">', unsafe_allow_html=True)
                                except:
                                    st.image(img_path, width=80) 
                                st.markdown(f"<div style='text-align: center; color: grey; font-size: small;'>{d}</div>", unsafe_allow_html=True)
                    
                    if other_dragons:
                        st.write(", ".join(other_dragons))
                else:
                    st.write("—")

                """ st.markdown(f"**🗡️ Armas:** {', '.join(ev.weapons) if ev.weapons else '—'}") """
                st.markdown("**🗡️ Armas:**")
                if ev.weapons:
                    weapons = [w for w in ev.weapons]

                    #Mostrar imagenes
                    if weapons:
                        cols = st.columns(9)
                        for i, w in enumerate(weapons):
                            with cols[i % 9]:
                                img_path = gestor.weapons_images[w]
                                try:
                                    b64_img = get_base64_of_bin_file(img_path)
                                    st.markdown(f'<img src="data:image/png;base64,{b64_img}" style="width:30px; height:30px; object-fit:contain; display:block; margin: 0 auto;">', unsafe_allow_html=True)
                                except:
                                    st.image(img_path, width=80)
                                st.markdown(f"<div style='text-align: center; color: grey; font-size: small;'>{w}</div>", unsafe_allow_html=True)
                else:
                    st.write("—")
                    
                st.markdown("**🛡️ Armaduras:**")
                if ev.armors:
                    armors = [w for w in ev.armors]

                    #Mostrar imagenes
                    if armors:
                        cols = st.columns(9)
                        for i, a in enumerate(armors):
                            with cols[i % 9]:
                                img_path = gestor.armors_images[a]
                                try:
                                    b64_img = get_base64_of_bin_file(img_path)
                                    st.markdown(f'<img src="data:image/png;base64,{b64_img}" style="width:30px; height:30px; object-fit:contain; display:block; margin: 0 auto;">', unsafe_allow_html=True)
                                except:
                                    st.image(img_path, width=80)
                                st.markdown(f"<div style='text-align: center; color: grey; font-size: small;'>{a}</div>", unsafe_allow_html=True)
                else:
                    st.write("—")
                
                num_ovejas = ev.extra if hasattr(ev,'extra') and ev.extra else 0
                st.markdown(f"**🐑 Ovejas:**")
                
                if num_ovejas > 0:
                    cols = st.columns(10)
                    for i in range(num_ovejas):
                        with cols[i % 10]:
                            rng = random.Random(f"{ev.title}_{i}")
                            es_negra = rng.random() < 0.2
                            
                            img_path = "assets/sheeps/ovejaNegra.png" if es_negra else "assets/sheeps/oveja.png"
                            label = "Oveja negra" if es_negra else "Oveja común"

                            try:
                                b64_img = get_base64_of_bin_file(img_path)
                                st.markdown(f'<img src="data:image/png;base64,{b64_img}" style="width:40px; height:40px; object-fit:contain; display:block; margin: 0 auto;">', unsafe_allow_html=True)
                            except:
                                st.image(img_path, width=40)
                            st.markdown(f"<div style='text-align: center; color: grey; font-size: small;'>{label}</div>", unsafe_allow_html=True)

                if st.button(f"🗑️ Eliminar '{ev.title}'", key=f"del_{idx}"):
                    evento_eliminado = eventos.pop(idx)
                    #Devolver recursos
                    for grupo in gestor.randoms_warriors.keys():
                        count = sum(1 for w in evento_eliminado.warriors if w == grupo)
                        gestor.randoms_warriors[grupo] += count
                    for dragon in gestor.free_dragons.keys():
                        count = sum(1 for d in evento_eliminado.dragons if d == dragon)
                        gestor.free_dragons[dragon] += count
                    for arma in gestor.weapons.keys():
                        count = sum(1 for a in evento_eliminado.weapons if a == arma)
                        gestor.weapons[arma] += count
                    for armadura in gestor.armors.keys():
                        count = sum(1 for a in evento_eliminado.armors if a == armadura)
                        gestor.armors[armadura] += count
                    if hasattr(evento_eliminado, "extra") and evento_eliminado.extra is not None:
                        gestor.ovejas += evento_eliminado.extra

                    gestor.guardar_en_json() 
                    st.success(f"✅ Evento '{evento_eliminado.title}' eliminado y recursos devueltos")
                    st.rerun()
    else:
        st.info("No hay eventos activos en este momento")

    col1, spacer, col2 = st.columns(3)
    with col1:
        if st.button("Menú principal", key="main_menu"):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("Añadir evento", key="new_event_btn"):
            st.session_state.page = "añadir_evento"
            st.rerun()
