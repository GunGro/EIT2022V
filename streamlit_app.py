import streamlit as st
from bokeh.models.widgets import Div
st.set_page_config(
    layout="wide"
)

st.image('./header_english.png')
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('./style.css')

col1, col2, col3 = st.columns([0.5, 1, 0.5])

with col2:
    st.markdown('# <span style="color:#410464"> Lånekassens AI</span>', unsafe_allow_html=True)
    st.write("""
    Student loan fraud costs Lånekassen several million kroner a year. In particular, applicants may falsely state that they are living away from home, and thus receive an education grant (stipend) they’re not eligible for. Lånekassen estimates that a recurring 4-5 % of students cannot prove that they’re living away from home.\n 
To combat this problem, our team has developed an AI that will suggest high-risk cases of student loan holders, whose applications will be processed manually. This initiative will help us allocate our resources more efficiently. Both in terms of time needed to process the student loan applications, and in terms of funds distributed. In the long run, this will lead to more efficient use of tax money and give more people the opportunity to get an education. \n
To promote responsible and transparent use of AI we allow users to calculate their own risk here before they fill out their application. 

"""
    )

    if st.button('Calculate your risk!'):
        # js = "window.open('https://share.streamlit.io/gungro/eit2022v/page2')"  # New tab or window
        js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
