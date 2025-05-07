# Problem Statement

# Write a function that takes two numbers and finds the average between the two.


# Soultion:1


# def get_average(num1,num2):

#     average = (num1 + num2 ) / 2
#     print(f"The average of {num1} and {num2} is {average}.")

# def main():
#     get_average(10,20)

# if __name__ == "__main__":
#     main()


# Solution:2

def average(a: float, b: float):
    """Return the of way between two numbers"""

    sum = a + b
    return sum / 2


def main():

    avrg_1 = average(30,23)
    avrg_2 = average(100,200)

    final = average(avrg_1, avrg_2)

    print(f"Avrg_1 =  {avrg_1}")
    print(f"Avrg_2 =  {avrg_2}")
    print(f"Final =  {final}")


if __name__ == "__main__":
    main()    