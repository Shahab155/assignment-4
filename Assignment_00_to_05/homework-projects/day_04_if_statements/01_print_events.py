# Problem Statement

# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements.

# Solution 
# Define a function named main, it will print the some of first 20 even numbers
def main():
    sum = 0
    for i in range(20):
        i = i * 2 
        sum += i 
    print(f"The sum of first 20 even numbers is {sum}.")
        
if __name__ == "__main__":
    main()