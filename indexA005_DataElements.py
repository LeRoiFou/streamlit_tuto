"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Fonctionnalités sur les tables

Date : 31/01/25
"""

import pandas as pd
import streamlit as st

# Title
st.title("Streamlit Elements Demo")

# DF Section
st.subheader("Dataframe")

df = pd.DataFrame({
    'Name':['Alice', 'Bob', 'Charlie', 'David'],
    'Age':[25, 32, 37, 45],
    'Occupation':['Engineer', 'Doctor', 'Artist', 'Chef'],
})
st.dataframe(df)

# Data Editor Section (Editable DF)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

# Static Table Section
st.subheader("Static Table")
st.table(df)

# Metric Section
st.subheader("Metrics")
st.metric(label='Total Rows', value=len(df))
st.metric(label='Average Age', value=round(df['Age'].mean(), 1))

# JSON and Dict Section
st.subheader("JSON")
sample_dict = {
    'name': 'Alice',
    'age': 25,
    'skills': ['Python', 'Data Science', 'Machine Learning']
}
st.json(sample_dict)

# Also show it as dictionary
st.write("Dictionnary view:", sample_dict)
