# Problem Statement

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Solution: How I solved the question 
# define a function in which the there will be three prompts taking the sides of triangle as an input.

# def main():
#     # Value of side 1
#     side_1 = input("Enter the value of side 1: ")
#     # convert str to int be casting the type 
#     side_1 = int(side_1)
#     # value of side_2 
#     side_2 = input("Enter the value of side 2: ")
#     # convert str to int be casting the type 
#     side_2 = int(side_2)
#     # Value of side 3
#     side_3 = input("Enter the value of side 2: ")
#     # convert str to int be casting the type 
#     side_3 = int(side_3)
    
#     perimter_of_triangle = float(side_1 + side_2 + side_3)
#     print(f"The perimter of triangle is {perimter_of_triangle}.")


# if __name__ == "__main__":
#     main()


# Solution:2 How the solution was provided at the end of task 

def main():
    # Take input from the user to calculate the perimter of triangle    
    side_1: float = float(input("Enter the length of side 1: "))
    side_2: float = float(input("Enter the length of side 2: "))
    side_3: float = float(input("Enter the length of side 3 : "))

    print(f"The perimter of triangle is: {str(side_1 + side_2 + side_3)}")


if __name__ == "__main__":
    main()


