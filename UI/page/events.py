import streamlit as st
import base64
from models.gestor_de_recursos import GestorEventos

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
        margin-top: 25px !important;
        font-family: Georgia, serif !important;
        color: rgb(202, 48, 1) !important;
        font-size: 55px !important; 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        margin: 0 auto !important;
        text-align: center !important;
        padding: 10px !important; 
        align-items: center !important;
        justify-content: center !important;
        height: fit-content !important;
        box-sizing: border-box !important;
    }}
    div[data-testid="stExpander"] {{
        background: white;
        border: 2px solid rgba(255,140,0,0.2);
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        color: black !important;
    }}
    div[data-testid="stExpander"] p, div[data-testid="stExpander"] span, div[data-testid="stExpander"] div {{
        color: black !important;
    }}
    div[data-testid="stExpander"]:hover {{
        border-color: rgba(202,48,1,0.4);
    }}
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h2 class='header'>Eventos activos</h2>", unsafe_allow_html=True)

    # Lista de eventos
    if eventos:
        for idx, ev in enumerate(eventos):
            with st.expander(f"🗡️ {ev.title} — {ev.type_of_event} ({ev.arena})"):
                st.markdown(f"**📅 Inicio:** {ev.start_date} {ev.start_time}")
                st.markdown(f"**📅 Fin:** {ev.finish_date} {ev.finish_time}")
                st.markdown(f"**⚔️ Guerreros:** {', '.join(ev.warriors) if ev.warriors else '—'}")
                st.markdown(f"**🐉 Dragones:** {', '.join(ev.dragons) if ev.dragons else '—'}")
                st.markdown(f"**🗡️ Armas:** {', '.join(ev.weapons) if ev.weapons else '—'}")
                st.markdown(f"**🛡️ Armaduras:** {', '.join(ev.armors) if ev.armors else '—'}")
                st.markdown(f"**🐑 Ovejas:** {ev.extra if hasattr(ev,'extra') else 0}")

                if st.button(f"🗑️ Eliminar '{ev.title}'", key=f"del_{idx}"):
                    evento_eliminado = eventos.pop(idx)
                    # Devolver recursos
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
                    if hasattr(evento_eliminado, "extra") and evento_eliminado is not None:
                        gestor.ovejas += evento_eliminado.extra
                    st.success(f"✅ Evento '{evento_eliminado.title}' eliminado y recursos devueltos")
                    st.rerun()
    else:
        st.info("No hay eventos activos en este momento.")

    # Botones navegación
    col1, spacer, col2 = st.columns(3)
    with col1:
        if st.button("Menú principal", key="main_menu"):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("Añadir evento", key="new_event_btn"):
            st.session_state.page = "añadir_evento"
            st.rerun()
