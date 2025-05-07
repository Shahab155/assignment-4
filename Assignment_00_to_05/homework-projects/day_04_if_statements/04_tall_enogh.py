# Problem Statement

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# Solution

MIN_HEIGHT:int = 50
def main():
   while True:
      user_input = input("How tall are you? ")

      if user_input.strip()  == "":
         print("*********** Good Bye **************")
         break

      try:
         height = int(user_input)
         if height >= MIN_HEIGHT:
            print("You are tall enough to ride.") 
         else:
            print("You are not tall enough to ride. try next year!")
      except:
         print("Error occured") 


if __name__ == "__main__":
   main()
        
        