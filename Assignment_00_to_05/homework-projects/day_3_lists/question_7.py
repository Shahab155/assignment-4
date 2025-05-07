# Problem Statement

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Solution:01

# def get_lst():
#     """Prompts user to enter an input one at a time and store that element into list. If user press enter without typing anything it should print list"""
#     lst = []
#     element: str = input("Enter an element: ")

#     while element != "":
#         lst.append(element)
#         element: str = input("Enter an element: ")

#     return lst 

# def main():
#     lst = get_lst()
#     print(lst)

# if __name__ == "__main__":
#     main()



# Solution:2

def main():
    my_list = list(map(str, input("Enter a value to store in list (seperated by comma): ").split(",")))
    print(my_list)


if __name__ == "__main__":
    main()    