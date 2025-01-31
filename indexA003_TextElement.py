"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Fonctionnalités sur les éléments de texte

Date : 31/01/25
"""

import streamlit as st

st.title("Super Simple Title")

st.header("This is a header")

st.subheader('Subheader')

st.markdown("This is **Markdown**")

st.caption("Small text")

code_example="""
def greet(name):
    print('hello', name)
"""
st.code(code_example, language='python')

st.divider()