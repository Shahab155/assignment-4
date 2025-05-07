# Problem Statement

# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------ Solution ----------------------------------------
# ----------------------------------------------------------------------------------------------------------

import random

def main():
    random_number = random.randint(1,100)
    while True:
        user_input = input("Guess a number: ")
        if user_input == "":
           break
        num = int(user_input)
        if num < random_number:
           print("Your guess is too low!")
        elif num > random_number:
            print("Your guess is too high!")
        else:
            print(f"Congrats! The number is {random_number}")
            break

if __name__ == "__main__":
    main()