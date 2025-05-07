# Problem Statement

# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

# Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# If the user enters anything else we print out:

# Sorry I only tell jokes

# You should use the three constants:

# PROMPT JOKE SORRY

# which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.

# Your program will need to use an if statement which checks if the user input is Joke:

# if user_input == "Joke":

# Recall that == is a comparison which tests if two values are equal to one another.

# Here is a full run of the program (user input is in blue):

# What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'


# -----------------------------------------------------------------------------------------------------
# --------------------------------------------- Solution -------------------------------------------
# -----------------------------------------------------------------------------------------------------

import random

# The prompt the user computer will ask from user to enter

PROMPT:str = input("What do you want?: ")
# list of jokes 

JOKES:str = ["1. Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'😅","2. My friend had surgery to transition from a man to a woman. I asked her, 'Of all the things they cut, what hurt the most?' 'The salary,' she said.","3. My Tinder bio says that I have a corner office with views of the entire city, drive a $500,000 vehicle, and that I'm paid to travel. My dates never seem too happy when I tell them I'm a bus driver.","4. Overheard two ladies talking — One said, 'I'm getting a boob job.' The other said, 'Well, I'm getting my asshole bleached.' The first one looked at her surprised and said, 'I can't picture your husband as a blonde.'","5. Fred came home from university in tears. 'Mum, am I adopted?' 'Of course not,' his mother replied. 'Why would you think such a thing?' Fred showed her his genealogy DNA test results — he was no match for any of his relatives and a strong match for a family living on the city's other side."]
# sorry message when user input is not joke
 
SORRY:str = "Sorry I only tell jokes😪"


def main():
    user_input = PROMPT.strip()

    if "joke" in user_input:
        print("\n",random.choice(JOKES),"\n")
    else:
        print("\nSorry! I only tell jokes.\n                                                                                                                                                                                 ")


if __name__ == "__main__":
    main()


