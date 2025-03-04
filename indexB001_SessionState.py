"""
La fonction st.session_state permet de ne pas réinitialiser la valeur lorsqu'on
réexécute l'application

Date : 04/03/2025
Editeur : Laurent Reynaud
"""

import streamlit as st

class App:
    
    def app():
        
        # Titre principal
        st.title('Streamlit - session state')
        
        # Création d'une variable qui n'est pas en session
        not_a_session_state = 0
        
        # Si la variable 'number' n'est pas en session
        if 'number' not in st.session_state:
            # Création d'une variable en session
            st.session_state.number = 0
        
        # Ajout d'un bouton avec incrémentation des variables ci-avant
        if st.button('Appuyez-moi !'):
            not_a_session_state += 1    
            st.session_state['number'] += 1
        
        st.write(f"Variable qui n'est pas en session state : 
                 {not_a_session_state}")
        st.write(f"Variable en session state : {st.session_state.number}")
        

if __name__ == '__main__':
    
    # Configuration de la page web
    st.set_page_config(
        page_title='session_state',
        page_icon='😨',
        layout='centered',
    )
    
    # Instanciation de la classe ci-avant
    app = App.app()
