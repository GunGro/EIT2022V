import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

feature_importance = pd.DataFrame(
    {
        "Number of credits passed": [0.20],
        "Same muncipality as parents": [0.19],
        "Age": [ 0.18],
        "Annual personal income": [ 0.12],
        "Study degree": [ 0.11],
        "Country of study": [ 0.105],
        "Startup year": [ 0.09],
        "Citizenship": [ 0.085],
        "Value of personal assests": [ 0.080],
        "Family status": [ 0.075],
        "Postal code": [ 0.05],
        "Sex": [ 0.03],
        "Tuition fees": [ 0.025],
        "Study subject": [ 0.02],
        "Expected year of completed education": [ 0.01],
    }
)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
feature_importance.plot.barh(ax = ax)

st.set_page_config(layout="wide")

st.image('./header_lonekassen.png')
st.markdown('# Our Use of AI')
col1, col2= st.columns([3, 2])
with col2:
    st.markdown('## Model Calculator')
with col1:
    st.markdown('')

col1, col2, col3= st.columns([3, 1, 1])
with col1:
    st.write("""
    Student loan fraud costs Lånekassen approximately 26 million kroner (2018) a year. In particular, applicants may falsely state that they are living away from home, and thus be eligible for an education grant (stipend). Lånekassen estimates that a recurring 4-5 % of students cannot prove that they’re living away from home. \n
To combat this problem, our team has developed an AI that will suggest high-risk cases of student loan holders, whose applications will be processed manually. This initiative will help us allocate our resources more efficiently. Both in terms of time needed to process the student loan applications, and in terms of funds distributed. In the long run, this will lead to more efficient use of tax money and give more people the opportunity to get an education. \n
To gain trust with our applicants, we strive to provide insight into how our AI suggests high risk cases. Therefore, we have calculated the relative importance of the variables used by our AI in determining the risk estimate. \n
In our risk calculator widget to the right, you see the most important variables in our AI model. To better understand how our model calculates risk, we invite you to manipulate the variables below and see how the risk estimate changes. 
"""
    )
    st.markdown("## Feature Importance")
    st.pyplot(fig = feature_importance.plot.barh())

with col2:
    st.text_input("Age", 18, 3)
    st.selectbox("Citizenship", ["Norwegian", "Other"])
    st.text_input("Postal Code", 7000, 4)
    anual_inc = st.selectbox("Annual income", ["0 NOK", "0 - 20 000 NOK", "20 000 - 100 000 NOK", "100 000 - 195 000 NOK", "Above 195 000 NOK"])
    st.selectbox("Study Degree", ["Bachelor", "Master", "PhD"])
    st.text_input("Startup year", 2018, 4)
    st.selectbox("University Credits", ["0-179", "180-300", "300+"])
    st.checkbox("Same municipality as parents")
    risk = np.random.uniform(low = 0, high = 100)
    st.markdown(f"# Risk: {risk :.1f}%") 
with col3:
    st.selectbox("Sex", ["Male", "Female", "Other"])
    st.selectbox("Country of Study", ["Norway", "Other"])
    st.selectbox("Family Status", ["Parent", "Child"])
    st.selectbox("Value of personal assets", ["Below 0 NOK", "0 - 100 000 NOK", "100 000 - 400 000 NOK", "Above 400 000 NOK"])
    st.selectbox("Study Subject", ["Natural Sciences", "Economics", "Social Studies", "Engineering", "Philosophy"])
    st.text_input("Exp. year of completed educ.", 2024, 4)
    st.selectbox("Tuition Fees", ["0-999", "1000-10000", "10000+"])

