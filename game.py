import random

rating = open('rating.txt')
def get_rating(name):
    for line in rating:
        if line.split()[0] == name:
            return line.split()[1]
    return 0

def input_checked():
    choice = input()
    if choice not in ["!exit", "paper", "scissors", "rock", "!rating"]:
        print("Invalid input")
    else:
        return choice

def game(choice):
    global points
    computer_choice = random.choice(["rock", "scissors", "paper"])
    if choice == "rock":
        if computer_choice == "rock":
            print("There is a draw (rock)")
            points += 50
        elif computer_choice == "scissors":
            print("Well done. The computer chose {} and failed".format(computer_choice))
            points += 100
        else:
            print("Sorry, but the computer chose paper")
    elif choice == "paper":
        if computer_choice == "paper":
            print("There is a draw (paper)")
            points += 50
        elif computer_choice == "rock":
            print("Well done. The computer chose {} and failed".format(computer_choice))
            points += 100
        else:
            print("Sorry, but the computer chose scissors")
    elif choice == "scissors":
        if computer_choice == "scissors":
            print("There is a draw (scissors)")
            points += 50
        elif computer_choice == "paper":
            print("Well done. The computer chose {} and failed".format(computer_choice))
            points += 100
        else:
            print("Sorry, but the computer chose rock")


name = input("Enter your name!")
print("Hello, " + name)
points = int(get_rating(name))
while True:
    choice = input_checked()
    if choice == "!exit":
        print("Bye!")
        rating.close()
        exit()
    elif choice == "!rating":
        print("Rating:", points)
    else:
        game(choice)


