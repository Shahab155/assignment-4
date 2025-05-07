# Problem Statement

# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
    
import math
# Solution: 

def main():
    print(f"******** This program will perform division and return result and reminder.********")
    # get the first number from user 
    num1: float = float(input("Enter first number: "))
    # get the second number from user 
    num2: float = float(input("Enter second number: "))

    result = num1 / num2
    reminder = num1 % num2

    print(f"The result of this division is: {math.floor(result)} with reminder of {reminder}.")


if __name__ == "__main__":
    main()