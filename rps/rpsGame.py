import random


def rpsChoices():
    playerChoice = input("Choose one of the three: ")
    computerOptions = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerOptions)
    
    choices = {"player" : playerChoice, "computer" : computerChoice}
    return choices

def checkCondition(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    
    if player == computer:
        return "tie"
    
    elif player == "rock":
        if computer == "scissors":
            return "player won"
        else:
            return " computer won"
    
    elif player == "paper":
        if computer == "rock":
            return "player won"
        else:
            return " computer won"

    elif player == "scissors":
        if computer == "paper":
            return "player won"
        else:
            return " computer won"
    
choicesTest = rpsChoices()
result = checkCondition(choicesTest["player"], choicesTest["computer"])
print(result)




