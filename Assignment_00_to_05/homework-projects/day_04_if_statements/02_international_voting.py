# Problem Statement

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.


# Solution
# Define a function that will ask user his age 

def main():
    # ask your his/her age by using input function
    user_age = int(input("Who old are you? "))
    # for age greater than or less than 16
    if user_age >= 16 and user_age < 25:
        print(f"\nYou can vote in Peturksbouipo countries, where votting age is 16. But you can not vote in Stanlau, where voting age is 25. And also you cannot vote in Mayengua, where voting age 48.\n")
    # for age greater than or less than 25
    elif user_age >= 25 and user_age < 48:
        print("\nYou can vote in Peturksboupio where voting age is 16. You can also vote in Stanlau, where voting age is 25. But you cannot vote in Mayengua.\n")
    # for age greater than or less than 48
    elif user_age >= 48:
        print("\nYou can vote all over the world!\n")
    else:
        print("\nYou cannot vote anywhere.\n") 

if __name__== "__main__":
    main()                   



