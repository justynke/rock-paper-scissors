import random

rating = open('rating.txt', 'a')

def input_checked():
    choice = input()
    if choice not in ["!exit", "paper", "scissors", "rock"]:
        print("Invalid input")
    else:
        return choice

def game(choice):
    computer_choice = random.choice(["rock", "scissors", "paper"])
    if choice == "rock":
        if computer_choice == "rock":
            print("There is a draw (rock)")
        elif computer_choice == "scissors":
            print("Well done. The computer chose {} and failed".format(computer_choice))
        else:
            print("Sorry, but the computer chose paper")
    elif choice == "paper":
        if computer_choice == "paper":
            print("There is a draw (paper)")
        elif computer_choice == "rock":
            print("Well done. The computer chose {} and failed".format(computer_choice))
        else:
            print("Sorry, but the computer chose scissors")
    elif choice == "scissors":
        if computer_choice == "scissors":
            print("There is a draw (scissors)")
        elif computer_choice == "paper":
            print("Well done. The computer chose {} and failed".format(computer_choice))
        else:
            print("Sorry, but the computer chose rock")

while True:
    
    choice = input_checked()
    if choice == "!exit":
        print("Bye!")
        exit()
    else:
        game(choice)
