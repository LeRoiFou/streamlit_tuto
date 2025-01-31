"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Le composant st.session_state permet de stocker une valeur

Date : 31/01/25
"""

import streamlit as st

if "counter" not in st.session_state:
    # Assignation d'une valeur à stocker
    st.session_state.counter = 0

# Si le bouton "Increment Counter" a été activé...
if st.button("Increment Counter"):
    # Incrémentation
    st.session_state.counter +=1
    # Message d'information
    st.write(f"Counter incremented to: {st.session_state.counter}")

# Si le bouton "Reset" a été activé...
if st.button("Reset"):
    # Affectation d'une nouvelle valeur remplaçant celle qui été stockée
    st.session_state.counter = 0

# Si le bouton "Resete" n'a pas été activé...
else:
    # Message d'information
    st.write(f"Counter did not reset")

# Message d'information avec la valeur en stock après 
# incrémentation ou réinitialisation
st.write(f"Counter value: {st.session_state.counter}")
