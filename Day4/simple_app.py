import streamlit as st
st.title("Welcome to my first app")
st.write("Hello")
name = st.text_input("What is your name?")
st.write("Hello",name)