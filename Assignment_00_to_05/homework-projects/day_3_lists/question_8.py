# Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


# Solution: How I solved problem 

# MAX_LENGTH: int  = 3 


# def main():
#     # prompt use to add elements seperated by comma
#     my_lst:list = list(map(str, input("Enter an element: ").split(",")))
#     # loop throught list and print the last element untill the max-length comes
#     while  len(my_lst) > MAX_LENGTH:
#         last_element = my_lst.pop()
#         print(f"This is the last element of list: {last_element}")
        

# if __name__ == "__main__":
#     main()    

   
        
# Solution:2
# How Solution is provided in repository

MAX_LENGTH: int = 5

def shorten_lst(my_list):
    while len(my_list) > MAX_LENGTH:
        count = len(my_list)
        last_element = my_list.pop()
        print(f"\t \t \tIteration: {count}")
        print(f"The last element is list is: {last_element}.")
        count -= 1


def get_lst():
    my_list = []
    element: str = input("Enter element one by one or press enter to exits: ")
    while element != "":
        my_list.append(element)
        element: str = input("Enter element one by one or press enter to exits: ")

    return my_list
    


def main():
    my_list = get_lst()
    shorten_lst(my_list)

if __name__ == "__main__":
    main()

