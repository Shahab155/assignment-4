# Problem Statement

# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

# Here's a sample run of the program (user input is in blue):

# Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!

# Solution:1

# def make_sentence(word,part_of_speech):
#     if part_of_speech == 0:
#         print(f"I am excited to add this {word} to my vast collection of them!")
#     elif part_of_speech == 1:
#         print(f"It's so nice outside today it makes me want to {word}!")
#     elif part_of_speech == 2:
#         print(f"Looking out of my window, the sky is big and {word}!")

# def main():
#     word: str = input("\nPlease type a noun, verb, or adjective: ")
#     part_of_speech:int = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))           
#     make_sentence(word,part_of_speech)

# if __name__ == "__main__":
#     main()
     


# **************************************************************************************************
# ****************************************** Problem 2 ********************************
# **************************************************************************************************

# 🟢 Problem Statement:
# Write a helper function called describe_feeling(feeling, intensity), which takes:

# A string feeling (like "happy", "sad", "excited", etc.)

# An integer intensity from 1 to 3

# Based on the intensity level, print a sentence that uses the feeling word in a different way:

# If intensity is 1:
# "I'm feeling a little bit ____ today."

# If intensity is 2:
# "I'm feeling pretty ____ right now."

# If intensity is 3:
# "Wow! I'm feeling super ____!!!"


# Solution:2
def describe_feeling(feeling, intensity):
    if intensity == 1:
        print(f"I am feeling a little bit {feeling} today.")
    elif intensity == 2:
        print(f"I am feeling pretty {feeling} right now.")
    elif intensity == 3:
        print(f"Wow! I am feeling super {feeling}!!!")
    else:
        print("Intensity should be less than 3.") 

def main():
    feeling: str = input("\nHow are you feeling today? ")
    intensity: int = int(input("\nOn scale of 1 to 3 how strong is your feeling? "))
    describe_feeling(feeling, intensity)

if __name__ == "__main__":
    main()                   
