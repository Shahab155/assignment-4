# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1. Prompt the user to enter the first number.

# 2. Read the input and convert it to an integer.

# 3. Prompt the user to enter the second number.

# 4. Read the input and convert it to an integer.

# 5. Calculate the sum of the two numbers.

# 6. Print the total sum with an appropriate message.

# Solution:

def main():
    """This function will add two numbers."""
    print("**************** This program will add two numbers ******************")
    # Takes the first input as string
    num1: str = input("Enter first number: ")
    # converts str into ini type 
    num1: int = int(num1)
    # Takes the second input as string 
    num2: str = input("Enter second number: ")
    # converts str into ini type 
    num2: int = int(num2)

    result = num1 + num2
    print(f"The sum of {num1} and {num2} = {result}")

# print the output in terminal  



if __name__ == "__main__":
    main()



