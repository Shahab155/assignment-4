# Problem Statement

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

Solution: 1

def get_user_lst():
     
    numbers = []
    while True:
       user_input = input("Enter an integer or press enter to stop: ")
       if user_input == "":
           break
       
       num = int(user_input)
       numbers.append(num)
    return numbers
   

def count_evens(lst):
    count = 0
    for num in lst:
       if num % 2 == 0:
           count += 1
    print(f"\nThere are {count} even numbers in list.\n")


def main():
    user_numbers = get_user_lst()
    count_evens(user_numbers)

if __name__ == "__main__":
    main()    






      
