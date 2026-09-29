import streamlit as st
st.title("Welcome to my first app")
st.write("Hello")
st.header("This is My Portfolio")
name=st.text_input("Enter your name...")

if st.button("Submit"):
    st.write ("Hello",name)
st.markdown("This is **Rashmitha**")