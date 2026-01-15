# Dice Six Checker Game
def dice_six_checker():
    print("Dice Six Checker Game")
    print("Type dice numbers between 1 and 6.\n")

    rounds = int(input("How many rounds? : "))

    for i in range(1, rounds + 1):
        x = int(input(f"Round {i} - Enter dice number (1-6): "))

        if x < 1 or x > 6:
            print("Invalid dice number! Please enter 1 to 6.\n")
        elif x == 6:
            print("YES! SIX \n")
        else:
            print("NO (Not six)\n")


dice_six_checker()
