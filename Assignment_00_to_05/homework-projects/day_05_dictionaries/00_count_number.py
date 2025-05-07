# Problem Statement

# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# Solution 

# def get_user_numbers():
#     """ Initiallize a empty lst and add number by get input from user one by one"""

#     user_numbers = []
#     while True:
#         user_input = input("Enter a number: ")

#         if user_input == "":
#             break 
        
#         try:
#           num = int(user_input)
#           user_numbers.append(num)
#         except:
#             print("Enter a valid integer!")  

#     return user_numbers

# def count_numbers(num_lst):
#     """Create empty dict, and loop through list check a number does not exist in list than add that number a key in dict with value 1 """
    
#     num_dict = {}
#     for num in num_lst:
#         if num not in num_dict:
#             num_dict[num] = 1
#         else:
#             num_dict[num] += 1

#     return num_dict

# def print_counts(num_dict):
#     """loop through dictionary and print the appearance of each number""" 
#     for num in num_dict:
#         print(f"{num} appears {num_dict[num]} times.")

# def main():
#     user_numbers = get_user_numbers()
#     num_dict = count_numbers(user_numbers)
#     print_counts(num_dict)


# if __name__ == "__main__":
#     main()




# *********************************************************************************************
# ************************ Problem Two *****************************
# ********************************************************************************************

def get_user_words():
    """This function will prompt your to enter a word, one at a time, and it will append it into list"""

    user_words = []
    while True:
        user_input = input("Enter a word: ")

        if user_input.strip() == "":
            break

        try:
            word = user_input
            user_words.append(word)
        except:
            print("Please enter only strings!")

    return user_words        


def count_words(word_lst):
    """This function will check words inside list and store there key and value inside a dictionary."""

    word_dict = {}
    for word in word_lst:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict


def print_counts(word_dict):
    for word in word_dict:
        print(f"{word} appears {word_dict[word]} times.") 


def main():
    user_words = get_user_words()
    word_dict = count_words(user_words)
    print_counts(word_dict)

if __name__ == "__main__":
    main()