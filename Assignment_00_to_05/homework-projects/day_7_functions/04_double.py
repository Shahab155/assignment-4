# Problem Statement

# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4

# Solution: 01

def double(num):
    """This function takes a user input and return its double."""
    doubled = num * 2
    return f"{num} double is {doubled}."

  
def main():
    num = int(input("Enter a integer: "))
    print(double(num))


if __name__ == "__main__":
    main()


    