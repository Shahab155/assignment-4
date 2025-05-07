# Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# Solution: How I solved the problem 

# def get_first_element(lst):
#        print(f"The first element in the list is: {lst[0]}")
       


# def main():
#     my_list = list(map(str,input("Enter a number seperated by space: ").split())) 
#     print(f"Current list {my_list}")
#     get_first_element(my_list)
    


# if __name__ == "__main__":
#     main()



# ********************************** Solution in repo ******************************
def get_lst_element(lst):
    """Prints the first element from list"""
    print(lst[0])


def get_lst():
    """Prompts user to enter an element of list on at a time or press enter to stop."""
    lst = []
    element:str = input("Enter a element of list at a time or press enter to stop: ")

    while element != "":
        lst.append(element)
        element: str = input("Enter a element of list at a time or press enter to stop: ")
        
    return lst

def main():
    lst = get_lst()
    print(lst)
    get_lst_element(lst)


if __name__ == "__main__":
    main()
        
