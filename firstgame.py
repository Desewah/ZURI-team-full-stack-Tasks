# Rock, Paper, Scissors game.
""" This is a hand game in which players simultaneously form one of three shapes
 identical to rock, paper and scissors with an outstreched hand """

# welcome the player


import random
print("Welcome to Rock, Paper and Scissors 1.0!")
print("-------------------------")

name = input("What's your name?: ").strip().title()

print("Player One ready")
print("Player Two,", name + ", Ready")

print("R = Rock")
print("P = Paper")
print("S = Scissors")
while True:

    choices = ["R", "P", "S"]

    playerOne = random.choice(choices)
    playerTwo = None

    while playerTwo not in choices:
        playerTwo = input("Pick your choice?: ").upper()

    if playerTwo == playerOne:
        print("Player One: ", playerOne)
        print("Player Two: ", playerTwo)
        print("Tie")

    elif playerTwo == "R":
        if playerOne == "P":
            print("Player One: ", playerOne)
            print("playerTwo: ", playerTwo)
            print("You lose!,\n Paper wraps Rock.")
        if playerOne == "S":
            print("Player One: ", playerOne)
            print("playerTwo: ", playerTwo)
            print("Congratulations!, You won\nRock breaks Scissors. ")

    elif playerTwo == "P":
        if playerOne == "R":
            print("Player One: ", playerOne)
            print("playerTwo: ", playerTwo)
            print("Congratulations!, You won\nPaper wraps Rock. ")
        if playerOne == "S":
            print("Player One: ", playerOne)
            print("playerTwo: ", playerTwo)
            print("You lose!,\nScissors cuts Paper. ")

    elif playerTwo == "S":
        if playerOne == "P":
            print("Player One: ", playerOne)
            print("playerTwo: ", playerTwo)
            print("Congratulations, You won!,\nScissors cuts Paper. ")
        if playerOne == "R":
            print("Player One: ", playerOne)
            print("playerTwo: ", playerTwo)
            print("You lose!,\nRock breaks Scissors. ")
    playAgain = input("Do you wish to Play the game Again [Y / N]?: ").upper()
    if playAgain == "N":
        break
    else:
        print("Welcome back!!")

print("Bye\nThanks for Playing")
