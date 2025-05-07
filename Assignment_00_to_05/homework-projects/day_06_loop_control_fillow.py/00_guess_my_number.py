# Problem Statement

# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Solution 

from random import randint

# generate a random number 

def main():
    while True:
        
        random_number = randint(1,10)

        user_input = input("\nGuess a number between 1 and 99: ")

        if user_input == "":
            print("Good bye! You ended guessing....")
            break

        num = int(user_input)
        if num > random_number:
            print(f"\n\tYour guess is too high: {random_number}")
        elif num < random_number:
            print(f"\n\t😪Your guess is too low: {random_number}")
         
    print(f"\n\t\tCongratulations🎉 you guessed right: {random_number}")        


if __name__ == "__main__":
    main()