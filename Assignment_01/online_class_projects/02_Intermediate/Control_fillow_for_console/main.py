# Problem: High Low

# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# -------------------------------------------------------------------------------------------------------------
# ---------------------------------------- Solution ----------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# import random

# MAX_ROUNDS = 5
# score = 1
# round = 0

# def main():
#     global score
#     global round
#     print("Welcome to High-Low Game!")
#     print("\n-------------------------------\n")
#     while round < MAX_ROUNDS:
#         round += 1
#         computer_number = random.randint(1,101)
#         my_number:int = random.randint(1,101)
#         user_choice: str = input("Tell your choice: ")

#         if my_number > computer_number and user_choice.strip().lower() == "higher":
#             print(f"\nRound {round}")
#             print(f"Your number is {my_number}")
#             print(f"Do you think your number is higher or lower than the computer's?: {user_choice}")
#             print(f"You were right! computer's number was: {computer_number}")
#             score += 1
#             print(f"You score is now {score}\n")
#         elif my_number < computer_number and user_choice.strip().lower() == "lower":
#             print(f"\nRound {round}")
#             print(f"Your number is {my_number}")
#             print(f"Do you think your number is higher or lower than the computer's?: {user_choice}")
#             print(f"You were right! computer's number was: {computer_number}")
#             score += 1
#             print(f"Your score now is {score}\n")

#         else:
#             print(f"\nRound {round}")
#             print(f"Your number is {my_number}")
#             print(f"Do you think your number is higher or lower than the computer's?: {user_choice}")
#             print(f"Aww, That's incorrect! computer's number was: {computer_number}")
#             score -= 1
#             print(f"Your score now is {score}\n")

#     if score >= 4:
#         print(f"Your score is now {score}")
#         print("Well done you played perfectly.🎉")
#     elif score >= 2 and score < 4:
#         print(f"Your score now {score}")
#         print(f"You won half of the game!🥰")
#     else:
#         print("Better Luck next time!😪")    

            

            

# if __name__ == "__main__":
#     main()            
    


def generator():
    yield 10
    yield 20
    yield 30

num1 = generator()   
print(num1[0])







