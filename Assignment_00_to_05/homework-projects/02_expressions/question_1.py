# Problem Statement

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

Solution:1
# import random

# def main():
#     print("*********** The Dice Simulator ***********")
#     DIE_SIDES = 6
#     count = 1
#     while count <= 3:
#         dice_1 = random.randint(1,DIE_SIDES)
#         dice_2 = random.randint(1, DIE_SIDES)

#         print(f"Roll: {count}")
#         print(f"First dice rolled: {dice_1}")
#         print(f"Second dice rolled: {dice_2}")

#         count += 1    

# if __name__ == "__main__":
#     main()


# Solution from repo:

"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# -> Input random library that will generate a random number 
import random

NUM_SIDES = 6

def roll_dice():
    die_1: int = random.randint(1,NUM_SIDES)
    die_2: int = random.randint(1,NUM_SIDES)
    total = die_1 + die_2
    print(f"The total of two dice = {total}")

def main():
    die_1: int = 10
    print(f"Die 1 in main() starts as: {str(die_1)}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die 1 in main() is : {die_1}") 


if __name__ == "__main__":
    main()