import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from dummy_model import DummyModel
from io import BytesIO

feature_importance = pd.DataFrame({
    'Variables': [
        "Number of credits passed",
        "Same muncipality as parents",
        "Age",
        "Annual personal income",
        "Study degree",
        "Country of study",
        "Startup year",
        "Citizenship",
        "Value of personal assests",
        "Family status",
        "Postal code",
        "Sex",
        "Tuition fees",
        "Study subject",
        "Expected year of completed education"
    ],
    'Importance': [
        0.20,
        0.19,
        0.18,
        0.12,
        0.11,
        0.105,
        0.09,
        0.085,
        0.080,
        0.075,
        0.05,
        0.03,
        0.025,
        0.02,
        0.015
    ]
})

feature_importance.sort_values(by = ['Importance'], inplace = True)
x_labels = np.linspace(start = 0, stop = 0.2, num = 5, endpoint=True)

feat_fig = plt.figure()
ax = feat_fig.add_subplot(1,1,1)
ax.set_xticks(x_labels)
ax.set_facecolor("#F4F4F4")
feature_importance.plot.barh(x='Variables', y='Importance', ax = ax, color ="#410464")

st.set_page_config(layout="wide")
do_randomization = st.sidebar.checkbox("Use random risk calculation")

st.image('./header_english.png')
st.markdown('# <span style="color:#410464">Our use of AI </span>', unsafe_allow_html=True)
col1, col2= st.columns([3, 2])
with col2:
    st.markdown('## <span style="color:#410464"> Risk Calculator</span>', unsafe_allow_html=True)
with col1:
    st.markdown('')

col1, placeholder, col2,  col3 = st.columns([3, 0.2, 1, 1])
with col1:
    st.write("""
    Student loan fraud costs Lånekassen several million a year. In particular, applicants may falsely state that they are living away from home, and thus be eligible for an education grant (stipend). Lånekassen estimates that a recurring 4-5 % of students cannot prove that they’re living away from home. \n
To combat this problem, our team has developed an AI that will suggest high-risk cases of student loan holders, whose applications will be processed manually. This initiative will help us allocate our resources more efficiently. Both in terms of time needed to process the student loan applications, and in terms of funds distributed. In the long run, this will lead to more efficient use of tax money and give more people the opportunity to get an education. \n
To gain trust with our applicants, we strive to provide insight into how our AI suggests high-risk cases. Therefore, we have calculated the relative importance of the variables used by our AI in determining the risk estimate. \n
In our risk calculator widget to the right, you see the most important variables in our AI model. To better understand how our model calculates risk, we invite you to manipulate the variables to the right and see how the risk estimate changes. 
"""
    )
    st.markdown("## <span style='color:#410464'>Feature Importance </span>", unsafe_allow_html=True)
    st.write("Feature Importance refers to techniques that calculate a score for all the input features (variables) for a given model — the scores simply represent the “importance” of each feature. A higher score means that the specific feature will have a larger effect on the model that is being used to predict the risk.")
    st.pyplot(fig = feat_fig, facecolor="#F4F4F4")

st_dir = {}
with col2:
    st_dir["age"] = st.text_input("Age", 18, 3)
    st_dir["citizen"] = st.selectbox("Citizenship", ["Norwegian", "Other"])
    st_dir["postal"] = st.text_input("Postal Code", 7000, 4)
    st_dir["annual_inc"] = st.selectbox("Annual income", ["0 NOK", "0 - 20 000 NOK", "20 000 - 100 000 NOK", "100 000 - 195 000 NOK", "195 000 - 295 000 NOK", "Above 295 000 NOK"])
    st_dir["deg"] = st.selectbox("Study Degree", ["Bachelor", "Masters", "PhD"])
    st_dir["start"] = st.text_input("Year of degree start", 2018, 4)
    st_dir["cred"] = st.selectbox("University Credits", ["0-180", "180-300", "300+"])
    st_dir["with_parent"] = st.checkbox("Live in the same municipality as parents/primary caregivers")
with col3:
    st_dir["sex"] = st.selectbox("Sex", ["Male", "Female", "Other"])
    st_dir["country"] = st.selectbox("Country of Study", ["Norway", "Other"])
    st.selectbox("Family Status", ["Single", "Cohabitant", "Married"])
    st_dir["net_worth"] = st.selectbox("Value of personal assets", ["Below 0 NOK", "0 - 100 000 NOK", "100 000 - 400 000 NOK", "Above 400 000 NOK"])
    st_dir["subj"] = st.selectbox("Study Subject", ["Natural Sciences", "Economics", "Social Studies", "Engineering", "Philosophy"])
    st_dir["finish"] = st.text_input("Exp. year of completed educ.", 2024, 4)
    st_dir["fee"] = st.selectbox("Tuition Fees", ["0 - 999 NOK", "1000 - 10 000 NOK", "Above 10 000 NOK"])
    st_dir["is_parent"] = st.checkbox("Check the box if you have children")

with col2:
    if do_randomization:
        risk = np.random.uniform(low = 0, high = 100)
    else:
        model = DummyModel()
        risk = model.get_model_output(st_dir) #np.random.uniform(low = 0, high = 100)
    st.markdown(f"#  <span style='color:#410464'>Risk:</span> {risk :.1f}%", unsafe_allow_html=True)
    st.write(
        """This is the estimated risk of committing fraud based on the above variables. To understand how this risk is calculated, we encourage you to look at the feature importance of the different variables to the left. \n\nIf the risk is above 25%, proof of residence is required."""
    )
if not do_randomization:
    with col1:
        buf = BytesIO()
        fig = model.create_effects_image(st_dir)
        fig.savefig(buf, format = "png", facecolor="#F4F4F4")

        st.image(buf)
