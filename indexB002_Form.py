"""
La fonction st.form de Streamlit en Python sert à créer un formulaire 
qui regroupe plusieurs éléments et widgets avec un bouton :
-> Elle permet de regrouper visuellement des éléments et widgets 
dans un conteneur
-> Elle contient un bouton de soumission qui, lorsqu'il est pressé, 
envoie toutes les valeurs des widgets à l'intérieur du formulaire à Streamlit 
en une seule fois
-> Elle empêche le rechargement automatique du script à chaque modification 
d'un widget, contrairement au comportement par défaut de Streamlit
-> Elle permet de traiter les entrées utilisateur par lots, 
ce qui peut être utile pour optimiser les performances de l'application

Mais :
-> Chaque formulaire doit contenir un st.form_submit_button
-> st.download_button ne peut pas être ajouté dans un formulaire
-> Les formulaires peuvent apparaître n'importe où dans l'application, 
mais ne peuvent pas être imbriqués les uns dans les autres

Date : 04/03/2025
Editeur : Laurent Reynaud
"""

import streamlit as st

class App:
    
    def app():
        
        # Titre principal
        st.title('Streamlit - form')
        
        # Widgets
        my_textin1 = st.text_input('Entrer votre nom')
        my_check1 = st.checkbox('Je valide')
        my_slider1 = st.select_slider(
            "Sélectionner une couleur", options=['rouge', 'jaune', 'bleu'],)
        my_button1 = st.button('Valider')
        
        # Si le bouton a été appuyé...
        if my_button1:
            st.write(f"Texte saisi : {my_textin1}")
            st.write(f"Case à cocher : {my_check1}")
            st.write(f"Glisseur - option choisie : {my_slider1}")
        
        # Formulaire contenant les widgets ci-après
        form = st.form(key='my-form')
        my_textin2 = form.text_input('Entrer votre nom')
        my_check2 = form.checkbox('Je valide')
        my_slider2 = form.select_slider(
            "Sélectionner une couleur", options=['rouge', 'jaune', 'bleu'],)
        my_button2 = form.form_submit_button('Valider')
        
        # Si le bouton a été appuyé...
        if my_button2:
            st.write(f"Texte saisi : {my_textin2}")
            st.write(f"Case à cocher : {my_check2}")
            st.write(f"Glisseur - option choisie : {my_slider2}")
        
        

if __name__ == '__main__':
    
    # Configuration de la page web
    st.set_page_config(
        page_title='form',
        page_icon='😨',
        layout='centered',
    )
    
    # Instanciation de la classe ci-avant
    app = App.app()
