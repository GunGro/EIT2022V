
import streamlit as st


st.header('Provotype: Model Explanation')
def click_button():
    st.write("you clicked! YAY!")

col1, col21, col22 = st.columns([3, 1, 2])
with col1:
    st.write("Hello Multiverse!")
    st.image('./Feature_importance.png')
    st.button("click me", on_click = click_button)

    st.write("Fucking hell")


with col21:
    st.markdown("Pick a number")
with col22:
    st.number_input(None,min_value=0, max_value=10)

