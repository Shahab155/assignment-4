# Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

import random
# solution 

DIE_SIDES: int = 6  

def main():

    die1: int = random.randint(1, DIE_SIDES ) # random. randint generate a random number between 1 and DIE_SIDES
    die2: int = random.randint(1,DIE_SIDES) # random. randint generate a random number between 1 and DIE_SIDES

    total: int = die1 + die2
    
    print(f"Dice have {DIE_SIDES} sides each.")
    print(f"Roll Die1: {die1}")
    print(f"Roll Die2: {die2}")
    print(f"The total is: {total}")

if __name__ == "__main__":
    main()    
