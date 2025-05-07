# Problem #1: List Practice

# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# # Print the length of the list.


# # Add 'mango' at the end of the list. 


# # Print the updated list.

# ---------------------------------------------------------------------------------------------
# ------------------------------- Solution:1 -------------------------------------
# ---------------------------------------------------------------------------------------------
def main():
    fruit_lst:list = ["apple","banana","orange","grape","pineapple"]
    print(f"Lenght of list is: {len(fruit_lst)}")
    print(f"Origional list = {fruit_lst}")
    fruit_lst.append("mango")
    print(f"Updated list = {fruit_lst}")

if __name__ == "__main__":
    main()