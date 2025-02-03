"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Les callbacks : interactions entre composants
Ici on applique des fonctions pour certains boutons d'exécution

Date : 31/01/25
"""

import streamlit as st

def go_to_step2(name):
    """
    Récupération du nom saisi + changement de la valeur numérique de variable stockée
    args : nom saisi
    """
    st.session_state.info['name'] = name
    st.session_state.step = 2
    
def return_to_step1():
    """
    Modification des valeurs stockées en numérique et en dictionnaire (réinitialisation)
    """
    st.session_state.step = 1
    st.session_state.info = {}

# Assignation d'une valeur numérique stockée
if "step" not in st.session_state:
    st.session_state.step = 1

# Assignation d'un dictionnaire vide stocké 
if "info" not in st.session_state:
    st.session_state.info = {}

# Si la valeur numérique stockée est égale à 1...
if st.session_state.step == 1:
    
    # Titre
    st.header("Part 1 : Info")
    
    # Stockage du nom saisi dans la zone de texte
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    
    # Exécution de la fonction go_to_step2 au moment où le bouton est activé
    st.button("Next", # Nom attribué au bouton
              on_click=go_to_step2, # Fonction
              args=(name,) # Argument de la fonction toujours entre () et une virgule
              )

# Si la valeur numérique stockée est égale à 2...
if st.session_state.step == 2:
    
    # Titre
    st.header("Part 2: Review")
    
    # Sous-titre
    st.subheader("Please review this:")
    
    # Texte d'info récumérant le nom saisi
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")
    
    # Si le bouton "Submit" est activé...
    if st.button("Submit"):
        
        # Message d'info incluant le nom saisi dans la zone de texte
        st.success(f"Great! Hello {st.session_state.info.get('name', '')}!")
        
        # Ballons
        st.balloons()
        
        # Réinitialisation de valeur stockée dans le dictionnaire
        st.session_state.info = {}
    
    # Exécution de la fonction return_to_step1() si le bouton 'Back' est activé
    st.button('Back', on_click=return_to_step1)
