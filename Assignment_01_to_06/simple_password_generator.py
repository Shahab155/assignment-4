import random 

print("\n\t\t\t🔐 Welcome to Simple Password Generator Game.🔐\n")

# define the cahracters to use in password 
chars = "abcdefghijklmnopqrstuvwxyz!@#$%&*1234567890"

# Get the user input for the number of passwords and length of each password
num_passwords = int(input("How many passwords do you want to generate? "))
length_passwords = int(input("Enter the length of password you want to generate: "))

# Solution Way:01 
password = ""
for i in range(num_passwords):
    password = ""
    for _ in range(length_passwords):
        c = random.choice(chars)
        password += c
    print(f"Password:{i + 1} {password}")    
    
# Solution Way:02
for i in range(1, num_passwords):
    password = "".join(random.choice(chars) for _ in range(length_passwords))
    print(f"Password:{i} {password}")

   