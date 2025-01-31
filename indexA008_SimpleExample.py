"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Exemple d'un cas simple

Date : 31/01/25
"""

from datetime import datetime
import streamlit as st

# Titre principal
st.title("User Information Form")

# Assignation d'un dictionnaire
form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
    "location": None
}

# Assignation de date mini et max (date actuelle) pour la date d'anniversaire
min_date = datetime(1970, 1, 1)
max_date = datetime.now()

# Formulaire
with st.form(key='user_info_form'):
    
    # Déclaration de différentes composants
    form_values['name'] = st.text_input("Enter your name: ")
    form_values['height'] = st.number_input("Enter your height (cm): ")
    form_values['gender'] = st.selectbox("Gender", ['Male', 'Female'])
    form_values['dob'] = st.date_input(
        "Enter your birthday: ", max_value=max_date, min_value=min_date)
    form_values['location'] = st.text_input("Enter your location: ")
    submit_button = st.form_submit_button(label='Submit')
    
    # Si le bouton d'exécution est enclenché...
    if submit_button:
        
        # Si toutes les données du formulaire n'ont pas été toutes saisies
        if not all(form_values.values()):       
            # Message d'alerte
            st.warning("Please fill in all of the fields")
            
        # Si toutes les données du formulaire ont été saisies
        else:       
            # Ballons 😁
            st.balloons()
      
            # Titre H3
            st.write("### Info")
            
            # Affichage des informations saisies
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")

