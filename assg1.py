import streamlit as st

st.title("Welcome coders")
st.subheader("We are interested to know about your favourite programming language:")

st.write("Choose your favourite programming language")
language=st.selectbox("Youe favourite:", ["Python", "JavaScript", "C++", "Java", "Go", "Rust", "C#", "Ruby", "Swift", "TypeScript"])

st.text(f"Your favourite programming language is {language}. Excellent choice")

st.success("Thank you for your time")