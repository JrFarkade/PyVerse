# Rock Paper Scissors game
import random

for i in range(int(input("How many rounds: "))):
    user = input("rock / paper / scissors: ").lower()
    comp = random.choice(["rock", "paper", "scissors"])

    print("Computer:", comp)

    if user == comp:
        print("Draw")

    elif user == "rock" and comp == "scissors":
        print("You win")
    elif user == "paper" and comp == "rock":
        print("You win")
    elif user == "scissors" and comp == "paper":
        print("You win")

    elif user in ["rock", "paper", "scissors"]:
        print("Computer win")

    else:
        print("Invalid input")
