# making of chai

import streamlit as st
import datetime

st.title("Chai maker app")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome to Chai maker app {name}")

dob=st.date_input("Enter your date of birth", 
                  value=datetime.date(2000, 1, 1),
                  min_value=datetime.date(1950, 1, 1),max_value=datetime.date(2025, 1, 1)
)
if dob:
    st.write(f"Your date of birth {dob}")

if st.button("make Chai"):
    st.write("Your chai is being brewed")
    
add_masala = st.checkbox("Add masala")
if add_masala:
    st.write("Masala is added to your chai")

tea_type=st.radio("Pick your chai base:", ["Water", "Milk", "Almond Milk"])
st.write(f"Selected base {tea_type}")
flavour=st.selectbox("Choose flavour:", ["Ardrak chai", "Kesar chai", "Tulsi chai", "Rosogolla chai"])
st.write(f"Selected flavour {flavour}")

sugar=st.slider("How many spoon of sugar", 0, 5, 2) # min_val, max_val, default_val
if sugar>1:
    st.write(f"You want {sugar} spoons of sugar")
else:
    st.write(f"You want {sugar} spoon of sugar")
cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"You have ordered {cups} cups")

    

