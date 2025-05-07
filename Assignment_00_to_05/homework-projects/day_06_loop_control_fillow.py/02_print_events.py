# Problem Statement

# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# Solution .

def first_twenty_even():
    for i in range(20):
        i = i * 2
        print(i)
      


def main():
    first_twenty_even()

if __name__ == "__main__":
    main()    