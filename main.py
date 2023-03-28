from random import choice

print("Welcome to Rock Paper Scissors\n")

user = input("Select one of the following:\nRock[r]\nPaper[p]\nScissors[s]\n").lower()
computer = choice(['r', 'p', 's'])

def play_game(user, computer):
    if user == computer:
        print("It's a tie")
        return False
    elif is_win(user, computer):
        print("You win!")
        return True
    else:
        print("You lost!")
        return False

def is_win(player, opponent):
    winning_conditions = {'r': 's', 's': 'p', 'p': 'r'}
    return winning_conditions[player] == opponent

game = play_game(user, computer)
if not game:
    print("Computer chose", computer)

