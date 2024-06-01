import streamlit as st

st.title("Movies")

st.write("hello world")
movie_name = st.text_input("Favourite Movie?")

st.write(f"Your favourite movie is: {movie_name}")

