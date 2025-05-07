# Game Interaction:

# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.


# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------- Solution --------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

import streamlit as st

st.title("The List Slicing Game")

fruits = st.subheader(["apple","mango","banana","graps","watermelon"])
# print("\nWhat do you want to do?\n")
# print("1. Access elements")
# print("2. Replace Element")
# print("3. Slice over elements")
# print("4. Exit")
# user_choice = input("\nEnter your choice: ")

# while True:
#     if user_choice == "1":
#         index = int(input("Enter index of fruit you want to access: "))
#         if index > -len(fruits) and index <= len(fruits):
#             print(f"The fruit on \"{index}\" index is \"{fruits[index]}\"")
#             break
#         else:
#             print("Index is out of range!")
#             # continue
#     elif user_choice == "2":
#         index = int(input("Enter index of fruit you want to replace: "))
#         new_fruit = input("Enter name of new fruit: ")
#         if index > -len(fruits) and index <= len(fruits):
#            fruits[index] = new_fruit
#            print(fruits)
#         else:
#             print("Index out of range!")
#     elif user_choice == "3":
#         start_index = int(input("Enter starting index: "))
#         end_index = int(input("Enter ending index: ")) 
#         if start_index or end_index >= -len(fruits) and start_index or end_index <= len(fruits):
           
#             print(f"Fruits are printed from {start_index} to {end_index}")
#             print(fruits[start_index:end_index])
#     elif user_choice == "4":
#         print("Exiting program.......")
#         break
#     else:
#         print("Please enter a valid choice!")

             
                   


