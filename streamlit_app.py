import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

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
st.image('./header_english.png')

col1, col2, col3 = st.columns([0.5, 1, 0.5])
 
with col2:
        st.header("Lånekassens AI")
        st.write("""
        Now that you have received your risk estimate, we want you to gain insight into how our AI suggests high-risk cases. To this end, we have calculated an importance score or feature importance for each variable used by our AI in determining the risk estimate.
        A feature (variable) with a high score means that this feature will have a large effect on the final risk assessment. A plot displaying the feature importance of all included features is included below. From this, we see that the variables number of credits passed and same municipality as parents are most influential. """)
        st.header("Feature importance plot")
        st.pyplot(fig = feat_fig, facecolor="#F4F4F4")
        st.write("""However, feature importance does not tell us how each feature affects the risk assessment. That is, whether an increase in the feature increases or decreases the risk assessment. Therefore, we also provide an effect plot below.
        This shows how much and in which direction the different values of each feature affects the risk assessment. [further explanation of the red lines, etc., depending on what we include] From this, we see that individuals who have passed more credits generally are more likely to commit fraud (?). """)
        st.header("Effect plot")
        st.image("./effect_plot.png")
        st.write("""We hope this provides you with an understanding of the contribution of each variable, in the calculation of your risk profile. """)
        st.write("""Regrettably, the above concepts cannot explain how you got your particular risk assessment. The first limitation stems directly from feature importance. When each feature is assigned an importance score, these scores cannot communicate how the different features interact and are related to each other. As a simple example, say that the AI learned that men studying philosophy are particularly likely to commit fraud. This trivial relationship cannot be detected from feature importance alone. The second limitation stems from the fact that the above explanation applies equally well to everyone. To understand why you got your particular risk score, we must take your particular case into account (i.e., a local explanation).
        We are actively discussing how to adapt this page to best suit the needs of our users. To do this, we need your feedback. 
        """)
 
        st.write("[Give feedback!](https://share.streamlit.io/gungro/eit2022v)")


