import streamlit as st 

st.set_page_config(page_title="BMI Calculator", page_icon="📏")

st.markdown("""
    
    <style>
            
      .stApp {
            background: linear-gradient(to right, #e0f7fa, #e1bee7)
            }  
        h1{
            color: #4a148c;
            text-align: center;
        
        } 

        .stButton > button {
            padding: 10px 20px;
            background-color: #393E46;
            color: white;
            border: 1px solid #fff;
            width: 100%
            }    
        
        .stButton > button:hover {

            color:white
            }  
            

    </style>

""",unsafe_allow_html=True)


st.title("📏BMI (Body Mass Index) Calculator")
st.subheader("Calculate your BMI to find out if you're underweight, normal weight, overweight, or obese!")


# Input sliders for height and weight 
# height = st.slider("Select you height (in cm): ", min_value=100 , max_value= 250, value = 175)
# weight = st.slider("Select your weight (in kgs): ", min_value=40 , max_value= 150, value=70)
height = st.number_input("Enter your height in cm: ", value=155 ,min_value=100, max_value=250)
weight = st.number_input("Enter your weight in kgs: ", value=80 ,min_value=40, max_value=150)

# Calculate Bmi 
bmi = weight / ((height / 100) ** 2)  

# display bmi result 
if st.button("Check BMI"):
    st.subheader(f"Your BMI is {bmi:.2f}")
    # Determine BMI Category 
    if bmi < 18.5:
      st.error("Your are underweight. 🥗 Consider a balanced diet to reach a healthy weight.")
    elif 18.5 <= bmi < 24.9:
      st.success("You have normal weight. 🥰 Keep up the work!")   
    elif 25 <= bmi < 29.9:
      st.info("You are overweight. 🏃‍♂️ Consider regular exercise and a healthy diet.")
    else:
        st.error("You are in the obese category.It's important to consult with a healthcare provider.")



# Display BMI categories 
with st.expander("About BMI Categories"):
    st.write("""
    - **Underweight:** BMI less than 18.5
    - **Normal weight:** BMI between 18.5 and 24.9
    - **Overweiight:** BMI between 25 and 29.9
    - **Obesity:** BMI 30 or greater                  
""")




