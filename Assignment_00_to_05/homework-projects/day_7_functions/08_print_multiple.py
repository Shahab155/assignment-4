# Problem Statement

# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Here's a sample run of the program (user input is in blue):

# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!

# Solution: 1
def print_multiple(meesage: str, repeat:int):
    for _ in range(repeat):
        print(meesage, end=" ")

def main():
    message:str = input("Please type a message: ")
    repeat: int = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message,repeat)

if __name__ == "__main__":
    main()