# Problem Statement

# Ask the user for a number and print its square (the product of the number times itself).

def main():
    # Get the number from user as input 
    user_input: float = float(input("Enter a number to see its square: "))

    squared: float = user_input ** 2

    print(f"The square of {user_input} is {squared}.")

if __name__ == "__main__":
    main()    