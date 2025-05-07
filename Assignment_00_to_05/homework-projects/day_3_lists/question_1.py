# Problem Statement

# Write a function that takes a list of numbers and returns the sum of those numbers.

# Solution 

def add_numbers(num_list) -> int:

    sum = 0
    
    for number in num_list:
       sum += number
        
    return sum

def main():
#    take numbers list  from user
  try:    
    num_list: list[int] = list(map(int, input("Enter comma seperated numbers to get sum: ").split(",")))
    sum_of_numbers = add_numbers(num_list)
    print(f"\nThis is the list of numbers: {num_list}\n")
    print(f"The sum of number in the list is: {sum_of_numbers}!\n")
  except:
     print("Please enter valid numbers!")


if __name__ == "__main__":
    main()

