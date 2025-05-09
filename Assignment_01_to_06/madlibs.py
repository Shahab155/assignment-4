# # # Project: 1 "Madlibs"
import streamlit as st

st.title("Story Generator😍💖")
st.write("Welcome to the story generator game in which you will write, adject, verbs and a name of person. The story will generated by filling in the blanks with your words.")

col1,col2 = st.columns(2)

with col1:
    adjective = st.text_input("Adjective: ")
with col2: 
   verb1 = st.text_input("Verb1: ")

with col1: 
   verb2 = st.text_input("Verb2: ")

with col2:    
   famous_person = st.text_input("Famous Person: ")

madlib = f"""\nGenerated story: Computer programming is so {adjective}! It makes me so excited all the time\
    I love to {verb1}. Stay hydrated and {verb2} like your are {famous_person}."""

if st.button("Show result"):
    if not adjective:
          st.error("Required!")
    elif not verb1:
        st.error("Required!")
    elif not verb2:
        st.error("Required!")
    elif not famous_person:
        st.error("Required!")        
    else:
       st.success("Here is the story!")
       st.info(madlib)

