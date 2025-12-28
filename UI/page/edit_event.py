import streamlit as st

def mostrar():
    st.title("New-Event")
    if st.button("Volver al inicio"):
        st.experimental_set_query_params(pagina="inicio")
        st.experimental_rerun()