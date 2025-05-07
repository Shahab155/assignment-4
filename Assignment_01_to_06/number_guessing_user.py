import streamlit as st
import random


if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1,10)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0
    st.set_page_config(page_title="Guess the number", page_icon="🎲", layout="centered")


st.markdown("""
    <style>
          body {
          background: linear-gradient(135deg,#393E46, #fad0c4);
          }
            
          h1 {
            color: red;

            }  
            
          .stApp {
            background: linear-gradient(135deg,#393E46, #DFD0B8);
            padding: 20px;
            border-radius: 15px;
            }  
         
          .stTextInput, stNumberInput {
            background-color: #ffffff !important;
            border-radius: 10px
            }  

            .stButton > button {
              background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
            }  

            .stButton > button:hover {
            background: linear-gradient(135deg, #f8b95, #f67280);
            color: white; 
            }  
           
      </style>      
""",
unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center; color:black' >💥Number Guessing Game🎲 </h1>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center; color: #4388db' >Guess a number between 1 and 10</h4>",unsafe_allow_html=True)

user_guess = st.number_input("Enter your guess: ", min_value=1, max_value=10, step=1)


if st.button("Check Result"):
     st.session_state.attempts += 1
     if user_guess < st.session_state.random_number:
         st.warning("❌ Too low! Please try again 🔽")
     elif user_guess > st.session_state.random_number:
         st.warning("❌ Too High! Please try again 🔼") 
     else:
         st.success(f"Congratulations! 🎉 You guessed the correct number in {st.session_state.attempts} attempt.")
         st.session_state.random_number = random.randint(1,10)
         st.session_state.attempts = 0
   
     if st.button("Reset Game"):
         st.session_state.random_number = random.randint(1,10)
         st.session_state.attempts = 0
         st.rerun()