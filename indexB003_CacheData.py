"""
Le décorateur @st.cache_data

Dans cet exemple, cette fonction simule un chargement de données long (5 secondes) 
et retourne un DataFrame.

Lors de la première exécution, le chargement prendra 5 secondes. 
Streamlit exécute la fonction et stocke le résultat en cache.

Lors des exécutions suivantes (par exemple, en cliquant sur le bouton 
"Recharger la page"), le chargement sera instantané. 
Streamlit récupère le résultat directement depuis le cache au lieu de réexécuter 
la fonction (un peu comme la fonction lazy() de polars).

st.cache_data est particulièrement utile pour :
- Optimiser les performances en évitant les calculs ou chargements de 
données redondants.
- Améliorer l'expérience utilisateur en réduisant les temps de chargement.
- Gérer efficacement les données sérialisables comme les DataFrames, listes, 
ou dictionnaires.

Cette fonctionnalité permet de construire des applications Streamlit plus rapides 
et plus réactives, en particulier lorsqu'elles impliquent des opérations coûteuses 
en temps ou en ressources.

Documentation sur les paramètres de la fonction bénéficiant de cette intruction :
https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data

Date : 04/03/25
Editeur : Laurent Reynaud
"""

import streamlit as st
import pandas as pd
import time

class App:
    
    def app(data):
        
        st.title("Démonstration de st.cache_data")

        st.write("Chargement des données...")
        data = data()
        st.write("Données chargées !")

        st.dataframe(data)

        st.button("Recharger la page")

        # Suppression des données conservées avec l'instruction cache_data
        if st.button("Effacer toutes les données stockées"):
            st.cache_data.clear()
             

if __name__ == '__main__':
    
    # Configuration de la page web
    st.set_page_config(
        page_title='form',
        page_icon='😱',
        layout='centered',
    )
    
    @st.cache_data(ttl=30) # mise en cache pendant 30 secondes : au-delà non conservation
    def load_data():
        # Simulation d'un chargement de données long
        time.sleep(5)
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [10, 20, 30, 40]
        })
        return df
    
    # Instanciation de la classe ci-avant
    app = App.app(load_data)
    