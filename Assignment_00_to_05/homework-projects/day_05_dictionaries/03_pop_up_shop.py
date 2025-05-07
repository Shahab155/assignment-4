# Problem Statement

# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# ************************************************************************************************
# *********************************** Solution ****************************************
# ************************************************************************************************

def main():
    # create a dictionary 
    fruits = {"apple":6.5, "mango":4, "banana":2, "kiwi":10, "durain":20, "watermalon":8, "orange":3.5}
    # initiallize a dictionary with 0 as initial value 
    total_cost = 0
    # loop through dictionary 
    for fruit_name, price in fruits.items():
        try:
        # ask user for the amount of fruit he wants to buy 
            bought_amount = int(input(f"How much ({fruit_name}) do you want buy? "))
            if bought_amount > -1:
              total_cost += price * bought_amount
            else:
               print("\nPlease enter a non-negative number.\n")
        except:
            print("\nPlease enter a non negative integer!\n")   
    print(f"\nYour total bill is ${total_cost}\n")
       

       
if __name__ == "__main__":
    main()    


    