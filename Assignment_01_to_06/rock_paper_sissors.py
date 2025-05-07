import random

def play():
    # ask your for his choice 
    user = input("What is your choice? 'r' for rock, 's' for sissors and 'p' for paper:\n")
    # what computer will choice randomly 
    computer = random.choice(["r","p","r"])
    
    # if both have choosen same the game will be tie
    if user == computer:
        return "It\'s tie."
    # if is win function will retrun true user will win
    if is_win(user, computer):
        return "You Win!"
    
    return "You lost!"


def is_win(player,oppenent):
    if (player == "r" and oppenent == "s") or (player == "s" and oppenent == "p") or (player == "p" and oppenent == "r"):
        return True    

print(play())


