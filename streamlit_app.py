import numpy as np
import pandas as pd
import streamlit as st
from dummy_model import DummyModel
from io import BytesIO

st.set_page_config(
        layout="wide"
)

st.image('./header_english.png')

col1, col2, col3, col4 = st.columns(4)
st_dir = {}
with col2:
    st.markdown('## <span style="color:#410464"> Risk Calculator</span>', unsafe_allow_html=True)
    st_dir["age"] = st.text_input("Age", 18, 3)
    st_dir["citizen"] = st.selectbox("Citizenship", ["Norwegian", "Other"])
    st_dir["postal"] = st.text_input("Postal Code", 7000, 4)
    st_dir["annual_inc"] = st.selectbox("Annual income", ["0 NOK", "0 - 20 000 NOK", "20 000 - 100 000 NOK", "100 000 - 195 000 NOK", "195 000 - 295 000 NOK", "Above 295 000 NOK"])
    st_dir["deg"] = st.selectbox("Study Degree", ["Bachelor", "Masters", "PhD"])
    st_dir["start"] = st.text_input("Year of degree start", 2018, 4)
    st_dir["cred"] = st.selectbox("University Credits", ["0-180", "180-300", "300+"])
    st_dir["with_parent"] = st.checkbox("Live in the same municipality as parents/primary caregivers")
with col3:
    st.markdown('## <span style="color:#410464">&nbsp;</span>', unsafe_allow_html=True)
    st_dir["sex"] = st.selectbox("Sex", ["Male", "Female", "Other"])
    st_dir["country"] = st.selectbox("Country of Study", ["Norway", "Other"])
    st.selectbox("Family Status", ["Single", "Cohabitant", "Married"])
    st_dir["net_worth"] = st.selectbox("Value of personal assets", ["Below 0 NOK", "0 - 100 000 NOK", "100 000 - 400 000 NOK", "Above 400 000 NOK"])
    st_dir["subj"] = st.selectbox("Study Subject", ["Natural Sciences", "Economics", "Social Studies", "Engineering", "Philosophy"])
    st_dir["finish"] = st.text_input("Exp. year of completed educ.", 2024, 4)
    st_dir["fee"] = st.selectbox("Tuition Fees", ["0 - 999 NOK", "1000 - 10 000 NOK", "Above 10 000 NOK"])
    st_dir["is_parent"] = st.checkbox("Check the box if you have children")

model = DummyModel()
with col2:
    risk = model.get_model_output(st_dir)
    st.markdown(f"#  <span style='color:#410464'>Risk:</span> {risk :.1f}%", unsafe_allow_html=True)
    st.write(
        """This is the estimated risk of committing fraud based on the above variables. To understand how this risk is calculated, we encourage you to click the button to the right. \n\nIf the risk is above 25%, proof of residence is required."""
    )

with col3:
    st.write("[Click here for explanation](https://share.streamlit.io/gungro/eit2022v/page3)")

