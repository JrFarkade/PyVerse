# Head or Tails
import random

print("=== Head or Tails ===")

choice = input("Choose (Head/Tail): ").strip().lower()

if choice not in ["head", "tail"]:
    print("Invalid choice! Please choose only Head or Tail.")
else:
    toss = random.choice(["head", "tail"])

    print(f"\nCoin Toss Result: {toss.capitalize()}")

    if choice == toss:
        print("You Win!")
    else:
        print("You Lose!")
