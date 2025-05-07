# Problem Statement

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# ************************ Solution:1 *************************

# SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my ___ ___ ___!"

# def main():
#     # get an adjective user as input 
#     adjective: str = input("Please enter an adjective and press enter: ")
#     # get a noun from user as an input 
#     noun: str = input("Please enter an adjective and press enter: ")
#     # get a verb from user as an input 
#     verb: str = input("Please enter a verb and press enter: ")

#     SENTENCE_START = f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!"

#     print(SENTENCE_START)


# if __name__ == "__main__":
#     main() 



# ************************ Solution:2 *************************

SENTENCE_START:str = "Panaversity is fun. I learned to program and used Python to make my " 

def main():

    adjective:str = input("Please enter an adjective and press enter: ")
    noun: str = input("Please enter a noun and press enter: ")
    verb:str = input("Please enter a verb and press enter: ")

     # print the sentence show output  
    print(SENTENCE_START + adjective + " " +  noun  + " "  + verb + "!"  )


if __name__ == "__main__":
    main()


