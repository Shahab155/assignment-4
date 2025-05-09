import random
import string

# List of words for the game
words = ['apple', 'banana', 'cherry', 'mango', 'orange', 'kiwi', 'grape', 'lemon', 'peach', 'plum']


def get_valid_word(words):
    """
    Select the random word from list that does not contain '-' or ' '.
    Returns the word in uppercase  
       
    """
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word that need to be guessed
    alphabet = set(string.ascii_letters.upper())
    used_letters = set() # letters the user has guessed

    lives = 6
    print(f"\n\t\t\t\t{'*'*35} Let's Play Hangman😎 {'*'*35}\n")
# Game loop: Continue untill the user guesses the word or runs out of lives
    while len(word_letters) > 0 and lives > 0:
        print(f"Lives left: {lives}")
        print("Used letters: ", " ".join(sorted(used_letters)))

        # Display current progress of the word (e.g, A - PP - E)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper().strip()

        # Ensure the user enters a sinle character 
        if len(user_letter) != 1:
            print("Please enter a single letter.\n")
            continue

        # If the letter is valid and has'nt been guessed 
        if user_letter in alphabet - used_letters:

            used_letters.add(user_letter)
            if user_letter in word_letters:
               word_letters.remove(user_letter)
               print(f"Good job! {user_letter} is in the word.\n")
            else:
                lives -= 1
                print(f"Sorry, {user_letter} is not in the word.\n")
                print(f"You have {lives} lives left.\n")

        elif user_letter in used_letters:
            print("You have already guessed that letter. Try again.\n")
        else:
            print("Invalid Character. Please try again.\n")

# End of game: check if user has guessed the word or lost
    if lives == 0:
        print(f"Game Over! You lost. The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word {word} correctly.")


hangman()


