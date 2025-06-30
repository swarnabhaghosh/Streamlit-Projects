import streamlit as st

st.title("Hello User")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your favourite flavour of chai")

chai=st.selectbox("Your favourite chai : ", ["Masala chai", "Lemon tea", "Milk tea", "Kesar chai"])
# selected option from the dropdown is stored in the chai variable

st.write(f"You choose {chai}. Excellent choice")

st.success("Your chai has been brewed")