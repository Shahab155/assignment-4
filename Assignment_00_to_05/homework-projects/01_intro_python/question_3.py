# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

def main():
    """This function will c"""
    degree_fahrenheit: str = input("Enter temperature in Fahrenheit: ")
    # convert str into  float 
    degree_fahrenheit: float = float(degree_fahrenheit)
    # convert temperature from fahrenheit to celsius
    degree_celsius: float = (degree_fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {degree_fahrenheit}F = {degree_celsius}C")


if __name__ == "__main__":
    main()
        