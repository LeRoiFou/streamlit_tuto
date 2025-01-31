"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Insertion d'une image

Date : 31/01/25
"""

import streamlit as st
import os

st.image(os.path.join(os.getcwd(), 'static', 'dog.png'), width=100)
