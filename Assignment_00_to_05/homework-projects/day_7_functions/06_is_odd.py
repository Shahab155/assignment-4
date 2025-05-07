# Problem

# Write a function that check weather number is even or odd?


def is_odd():
    num = int(input("\nEnter a number: "))

    for num in range(10):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")    


def main():
    is_odd()

if __name__ == "__main__":
    main()        