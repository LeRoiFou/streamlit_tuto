"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Enregistrement d'une instruction streamlit dans une variable

Date : 31/01/25
"""

import streamlit as st

pressed = st.button("Press me")
print(pressed)
print('First', pressed)   

if pressed is True:
    st.write("Bouton appuyé")
else:
    st.write("Bouton non")
    
pressed2 = st.button("Second Button")
print('Second', pressed2)   