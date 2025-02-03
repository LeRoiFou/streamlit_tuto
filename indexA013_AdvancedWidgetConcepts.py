"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Onglets, volet à gauche, cadrage, colonnes séparées, message remplacé...

Date : 03/02/25
"""

import streamlit as st

# Argument key pour éviter l'erreur d'un doublon (même composant et même intitulé)
st.button("Ok")
st.button("Ok", key='btn2')

# Lien entre deux barre de défilement (sliders)
if "slider" not in st.session_state:
    st.session_state.slider = 25
    
min_value = st.slider("Set min value", 0, 50, 25)

st.session_state.slider = st.slider(
    "Slider", min_value, 100, st.session_state.slider)

