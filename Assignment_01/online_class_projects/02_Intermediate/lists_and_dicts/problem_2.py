# Problem #2: Index Game

# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.


# -----------------------------------------------------------------------------------------------
# ----------------------------- Solution -------------------------------------------
# ----------------------------------------------------------------------------------------------

# Task:1 Create a list with atleat 5 elements 


def accessing_lst(lst):
    index = int(input("Enter a index value to print the on that index: "))
    if index >= -len(lst) and index < len(lst):
        print(f"\nThe value on {index} index is \"{lst[index]}\".\n")
    else:
        print("\nThis index is out of range!\n")    

fruit_lst: list = ["apple","mango","banana","cherry","watermelon"]
accessing_lst(fruit_lst)         

