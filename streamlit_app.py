import streamlit as st

st.set_page_config(
        layout="wide"
)
st.image('./header_english.png')

col1, col2, col3 = st.columns(3)

with col2:
        st.header("Lånekassens AI")
        st.write("""
        Student loan fraud costs Lånekassen several million a year. In particular, applicants may falsely state that they are living away from home, and thus be eligible for an education grant (stipend). Lånekassen estimates that a recurring 4-5 % of students cannot prove that they’re living away from home. \n
    To combat this problem, our team has developed an AI that will suggest high-risk cases of student loan holders, whose applications will be processed manually. This initiative will help us allocate our resources more efficiently. Both in terms of time needed to process the student loan applications, and in terms of funds distributed. In the long run, this will lead to more efficient use of tax money and give more people the opportunity to get an education. \n
    To gain trust with our applicants, we strive to provide insight into how our AI suggests high-risk cases. Therefore, we have calculated the relative importance of the variables used by our AI in determining the risk estimate. \n
    In our risk calculator widget you see the most important variables in our AI model. To better understand how our model calculates risk, we invite you to manipulate the variables and see how the risk estimate changes.
    """
        )

        st.write("[Click here for the calculator](https://share.streamlit.io/gungro/eit2022v/page2)")
