import random

def get_choices():
    player_choice = input("Enter a choice (rock,paper or scissors): ") 
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer": computer_choice}
    return choices


def check_win(player,computer):
    print(f"you chose {player}\ncomputer chose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock beats scissors, you win dude"
        else:
            return "paper beats rock, you lose dude"
    elif player == "paper":
        if computer == "scissors":
            return "scissors beats paper, you lose dude"
        else:
            return "paper beats rock, you win dude"
    elif player == "scissors":
        if computer == "rock":
            return "rock beats scissors, you lose dude"
        else:
            return "scissors beats paper, you win dude"
    
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)  



