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
        #st.header("Lånekassens AI")
        st.markdown('## <span style="color:#410464">Lånekassens AI</span>', unsafe_allow_html=True)
        st.write("""In the previous page you were asked to insert information into the risk calculator, in the end you were shown a number that shows your risk percentage out of 100 for committing fraud. (e.g. 5% risk of committing fraud, but 95% of not committing fraud). In this page we hope you will gain insight into how our AI calculates such risk percentages.

                """)

        #st.header("Feature importance plot")
        st.markdown('## <span style="color:#410464">Importance plot</span>', unsafe_allow_html=True)
        st.write("Each input in the calculator is given an individual score that measures how important it is for calculating risk. Inputs with higher scores have a larger effect on the final percentage. The graph below shows that the inputs ‘Number of Credits Passed’ and ‘Same municipality as Parents’ have the highest importance scores; they are the most important indicators that show a person's risk of committing fraud.")
        st.pyplot(fig = feat_fig, facecolor="#F4F4F4")
        st.markdown('## <span style="color:#410464">Effect plot</span>', unsafe_allow_html=True)
        st.write("Although we are able to understand what input contributes to your risk, we can only be sure of what direction your inputs affect your risk with an effect plot. This shows how much, and in which direction, the different values of each input on average affects the risk assessment. \n\nAn example of one such effect plot of passed university credits is provided below. This shows how much and in which direction the different values of the passed university credits on average affect the risk assessment. From this, we see that individuals who have passed more credits generally are less likely to commit fraud.")
        st.image("./uni_cred2.png")
        st.markdown('## <span style="color:#410464">Feedback!</span>', unsafe_allow_html=True)
        st.write("We hope this provides you with an understanding of the model used in the calculation of your risk profile. We wish to give our users the best possible explanation of our AI. If you feel like something is inadequate or missing, we encourage you to send us feedback.")
 
        st.write("[Give feedback!](https://share.streamlit.io/gungro/eit2022v)")


