"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

L'instruction rerun() permet d'activer immédiatement une instruction

Date : 05/02/25
"""

import streamlit as st

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    # Initialisation de la valeur à stocker
    st.session_state.count = 0
    
def increment_and_rerun():
    # Incrémentation de la valeur à stocker
    st.session_state.count +=1
    
    # Dès le lancement, appuyer une fois sur le bouton d'exécution permet
    # d'incrémenter de suite la valeur stockée. Sans cette instruction, lors
    # du lancement de la page @, il faut appuyé deux fois le bouton d'exécution
    # pour la première incrémentation
    st.rerun() 
    
st.write(f"Current count : {st.session_state.count}")

if st.button("Increment and Update Immediately"):
    
    # Appel de la fonction ci-avant
    increment_and_rerun()
    
