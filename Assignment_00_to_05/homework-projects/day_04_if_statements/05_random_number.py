# Problem Statement

# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Solution 
import random

N_NUMBERS: int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    count = 0
    while count < N_NUMBERS:
        user_answer = input("Do you want a random number? yes/no: ")
        count += 1 
        if user_answer.lower() == "yes":
            print(f"\nAt {count} iteration the generated number is {random.randint(MIN_VALUE, MAX_VALUE)}.\n")
        else:
           print(f"Good Bye!")    
  

if __name__ == "__main__":
    main()