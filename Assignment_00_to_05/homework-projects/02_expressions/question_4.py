# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# Solution 
from math import sqrt
def main():
    # get the length of side 1 
    ab: float =  float(input("Enter the length of side 1: "))
    # get the length of side 2
    ac: float = float(input("Enter the length of side 2: "))

    bc: float = ab **2 + ac **2
    print(f"The length of BC (the hypotenuse) is: {sqrt(bc)}.") 



if __name__ == "__main__":
    main()    


  