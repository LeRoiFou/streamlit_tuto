"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Exemple d'un cas complexe

Date : 31/01/25
"""

from datetime import datetime
import streamlit as st

# Assignation d'une date minimum et d'une date maximum (date actuelle)
min_date = datetime(1970, 1, 1)
max_date = datetime.now()

# Titre principal
st.title("User Information Form")

# Formulaire
with st.form(key='user_info_form', clear_on_submit=True):
    
    # Composants
    name1 = st.text_input("Enter your first name")
    birth_date = st.date_input(
        "Enter your birth date", min_value=min_date, max_value=max_date)
    
    # Si la date de naissance a été saisie...
    if birth_date:
        
        # Détermination de l'âge de l'utilisateur en années
        age = max_date.year - birth_date.year
        
        # Si le mois de naissance > mois actuel
        if birth_date.month > max_date.month or (
            birth_date.month == max_date.month 
            and birth_date.day > max_date.day):
            
            # Désincrémentation de l'âge de 1
            age -= 1
            
            # Affichage de l'âge
            st.write(f"Your calculated age is {age} years")
        
    # Composant  
    submit_button1 = st.form_submit_button(label="Submit Form")
    
    # Si un des composants prénom ou date de naissance n'ont pas été saisis...
    if not name1 or not birth_date:
        # Message d'alerte
        st.warning("Please fill in all form inputs")
        
    # Si le prénom et la date de naissance ont été saisis...
    else:
        # Composants
        st.success(f"Thank you, {name1}. Your age is {age} year.")
        st.balloons()
