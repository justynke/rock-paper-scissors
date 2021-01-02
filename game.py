import random

rating = open('rating.txt')
def get_rating(name):
    for line in rating:
        if line.split()[0] == name:
            return line.split()[1]
    return 0

def input_checked():
    global options
    while True:
        choice = input()
        if choice not in ["!exit", "!rating"] + options:
            print("Invalid input")
        else:
            return choice

def winner_list(computer_choice):
    global options
    global choice
    new_options = []
    for i in range(options.index(choice)+1, len(options)):
        new_options.append(options[i])
    for i in range(options.index(choice)):
        new_options.append(options[i])
    if new_options.index(computer_choice)+1 > (len(new_options) // 2):
        return True
    return False


def game(choice):
    global options
    global points
    computer_choice = random.choice(options)
    if computer_choice == choice:
        points += 50
        print("There is a draw ({})".format(choice))
    else:
        if winner_list(computer_choice):
            print("Well done. The computer chose {} and failed".format(computer_choice))
            points += 100
        else:
            print("Sorry, but the computer chose {}".format(computer_choice))


name = input("Enter your name!")
print("Hello, " + name)
points = int(get_rating(name))
options = input()
if options == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options.split(",")
print("Okay, let's start")
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


