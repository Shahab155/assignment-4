# Problem Statement

# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# Solution :01 How I solved problem 

# define a function that will return the list of doubled numbers 
# def double_the_list(num_list) -> list[int]:
#     # initally list will be empty 
#     doubled_list: list[int] = []
#     # user for to iterate over each element of num_list and multiply them with two 
#     for num in num_list:
#         num *= 2
#     #   add the doubled number into to the list
#         doubled_list.append(num)
        
#     return doubled_list


# def main():
#     # take the list of numbers from user 
#     num_list: list[int] = list(map(int, input("Enter numbers seperated by comma: ").split(",")))

#     # print list with initial values
#     print(f"\n Initial list: {num_list}\n")

#     # delcare a variable and call function into it 
#     list_of_doubled_numbers = double_the_list(num_list)
#     #  print doubled list   
#     print(f"Doubled list: {list_of_doubled_numbers}\n")


# if __name__ == "__main__":
#     main()

# ***************************** Solution:2 provided in repo ****************************

def main():
    numbers = [1,2,3,4,5]

    for i in range(len(numbers)):
       ele_in_index = numbers[i]
       numbers[i] = ele_in_index *2
    print(numbers)


if __name__ == "__main__":
    main()
