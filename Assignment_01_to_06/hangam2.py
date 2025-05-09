import string 
import random

words = ["Badaruddin","Sadar","Mazhar","Shahab","Salahuddin","Shoaib"]

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6 
    print("\n\t\t\tlet's Play Hangman") 

  


    while len(word_letters) > 0 and lives > 0:
        print("Lives left: ", lives)
        print("Used letters: ", " ".join(sorted(used_letters)))

        # show current progress 
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current Word = ", " ".join(word_list))


        user_letter = input("Guess a number: ").upper().strip()

        if len(user_letter) > 1:
          print("Please enter only one letter!") 
          continue 

  
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good Job😎! {user_letter} is in the word.\n")
            else:
                lives -= 1
                print(f"Sorry😪, {user_letter} is not in word.\n")
                print(f"You have {lives} lives left.")
        elif user_letter in used_letters:
            print("You have already guessed letter, try again.\n")
        else:
            print("Invalid Character🔻\n")

    if lives == 0:
        print(f"You lost❌! the word was {word}")
    else:
        print(f"Congratulations!🎉 You guessed {word} correctly✅")                
                        
hangman()
