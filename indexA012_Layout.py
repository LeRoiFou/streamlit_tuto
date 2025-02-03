"""
Cours : Streamlit Mini Course - Make Websites With ONLY Python
Lien : https://www.youtube.com/watch?v=o8p7uQCGD0U


Date : 03/02/25
"""

import streamlit as st

# Sidebar layout
st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and texte here")
sidebar_input = st.sidebar.text_input("Entre something in the sidebar")

# Tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Your are in Tab 1")
    
    # Columns layout
    col1, col2 = st.columns(2)

    with col1:
        st.header("Column 1")
        st.write("Content for column 1")
        
        # Popover (tooltip)
        st.write("Hover over this buttoon for tooltip")
        st.button("Button with tooltip", 
                  help="This is a tooltip or popover on hover")
        
    with col2:
        st.header("Column 2")
        st.write("Content for column 2")
        
        # Sidebar input handling
        if sidebar_input:
            st.write(f"You entered in the sidebar : {sidebar_input}")
    
with tab2:
    st.write("Your are in Tab 2")
    
    # Containers exemple
    with st.container(border=True):
        st.write("This is a container")
        st.write("You can think of containers as a grouping for elements")
        st.write("Containers help manage sections of the page")
        
    # Expander
    with st.expander("Expand for more details"):
        st.write("This is additional information that is hidden by default")
        st.write("You can use expanders to keep your interface cleaner")
        
with tab3:
    st.write("Your are in Tab 3")
        
    # Empty placeholder
    placeholder = st.empty()
    placeholder.write("This is an empty placeholder, useful for dynamic constant")
    if st.button("Update Place holder"):
        placeholder.write("The content of this placeholder has been updated")
        