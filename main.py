from random import choice

print("\t\t\tWelcome to Rock paper sissor\t\t\t\n\n")

user = str(input("Select one of the Following:\nRock[r]\npaper[p]\nSissor[s]\n"))
computer = choice(['r', 'p', 's'])


def playGame(user, computer):
    
    if user == computer:
        print("It\'s a Tie")

    if is_win(user, computer):
        return 1
    
    return 0

def is_win(player, opponent):
    if((player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r")):
        return True
    else:
        return False
    

game = playGame(user, computer)
if game == 0:
    print("you Win")
    print(computer)
else:
    print("You Lost")
    print(computer)