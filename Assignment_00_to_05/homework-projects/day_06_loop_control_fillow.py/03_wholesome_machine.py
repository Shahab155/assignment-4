# <!-- Problem Statement

# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :) -->

# Solution 

MY_AFFIRMATION = "I am the best python developer!"

def main():
    while True:
        user_input = input(f"Please type the following affirmation: {MY_AFFIRMATION}\n")
        if user_input == MY_AFFIRMATION:
            print("\nThat\'s right!\n")
            break
        else:
            print("\nThat\'s not the following affirmation. Try again!\n")

if __name__ == "__main__":
    main()


             