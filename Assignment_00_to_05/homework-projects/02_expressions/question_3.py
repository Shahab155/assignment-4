# Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# solution 
INCHES_IN_FOOT: int = 12 
def main():
    # get the number of feet from user 
    foot: float = float(input("Enter feet to convert into inches: "))
    # 1 foot = 12 inches 
    number_of_inches: float = foot * INCHES_IN_FOOT
    if foot == 1:
        print(f"{foot} foot = {number_of_inches} inches ")
    else:
        print(f"{foot} feet = {number_of_inches} inches")    


if __name__ == "__main__":
    main()