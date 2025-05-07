# Problem Statement

# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Solution 

def get_last_element(lst):
    """Print the last element from list"""
    print(f"This is the last element of the list: {lst[-1]}\n")


def get_lst():
    """Prompts user to enter an element of list or press enter to stop."""
    lst = []
    element: str = input("Enter an element of list one at a time or press enter to stop: ")

    while element != "":
        lst.append(element)
        element: str = input("Enter an element of list one at a time or press enter to stop: ")
        

    return lst     

def main():
    lst = get_lst()
    print(f"\nOrigional List: {lst}\n")
    get_last_element(lst)

if __name__ == "__main__":
    main()    
