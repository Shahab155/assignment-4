# Problem Statement

# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    """This will take user name with his number and save inside a dictionary."""
    
    phone_book = {}
    while True:
        name = input("Name: ")
        if name == "":
            break 
        number = int(input("Number: "))

        phone_book[name] = number

    return phone_book

def print_phonebook(phonebook):
    """This will print out name/number from dictionary"""
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}") 


def lookup_phonebook(phonebook):
    while True:
       name = input("Enter name to lookup: ")
       if name == "":
           break
                 
       
       if name not in phonebook:
            print(f"{name} is not in phonebook.")
       else:
            print(f"{name}")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_phonebook(phonebook)

if __name__ == "__main__":
    main()     
                    
