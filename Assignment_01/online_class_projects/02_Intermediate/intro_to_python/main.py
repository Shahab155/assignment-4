# Problem: Planetary Weight Calculator

# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.


# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------- Solution: -----------------------------------------
# -------------------------------------------------------------------------------------------------------------

print("\n\t******************* Welcome to Weight Conversion for different planets *********************")

MARS_MULTIPLE = 3.7
GRAVITAIOPNAL_FORCE = 10

weight_on_earth = float(input("Enter  your weight: "))

weight_on_mars = weight_on_earth * (MARS_MULTIPLE/GRAVITAIOPNAL_FORCE)
print(f"Your weight {weight_on_earth}kg is equaivalent on mars is: {weight_on_mars}kg")

















# wight_on_earth = int(input("\nEnter weight on earth: "))
# convert_into = input("\nEnter a planet: ")
# weight_on_other_planets = 0

# def main():
    
#     global weight_on_other_planet
#     planets = {
#                "Mars":3.7,
#                "Venus":8.89,
#                "Mercury":3.76,
#                "Jupiter":24.79,
#                "Saturn":10.44,
#                "Uranus":8.15,
#                "Neptune":11.15
#                }
    
#     if convert_into in planets:
#         gravitational_constant = planets[convert_into]
#         weight_on_other_planet = user_wight * (gravitational_constant / 10)
#         print(f"\nThe equivalent weight on {convert_into} is {round(weight_on_other_planet,2)}kg\n")
#     else:
#         print("\nInvalid planet name. Please enter a valid planet name!\n")    
        

# if __name__ == "__main__":
#     main()


