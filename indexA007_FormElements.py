"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U

Fonctionnalités sur divers composants

Date : 31/01/25
"""

import streamlit as st

# Title
st.title("STreamlit Form Demo")

# Form to hold the interactive elements
with st.form(key='sample_form'):
    
    # Text Input
    st.subheader('Text Inputs')
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")
    
    # Date and Time Inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")
    
    # Selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox("Select your gender", ['Male', 'Female'])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])
    
    # Toggles and Checkboxes
    st.subheader("Toggles & Checkboxes")
    notification = st.checkbox("Receive notification")
    toogle_value = st.checkbox("Enable dark mode?", value=False)
    
    # Submit Button for the Form
    submit_button = st.form_submit_button(label='Submit')
    
# Outside of the forms
st.subheader("Buttons")
if st.button("Click Me!"):
    st.write(f"Hello, {name}!")

# Link button
st.link_button("Tuto", "https://www.youtube.com/watch?v=o8p7uQCGD0U")