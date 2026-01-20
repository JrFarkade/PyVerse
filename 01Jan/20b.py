# Guess The Number
import random

secret = random.randint(1, 7)

print("Guess the number between 1 to 7. You have 3 chances.")

for chance in range(3):
    guess = int(input("Enter number: "))

    if guess == secret:
        print("✅ Correct! Number was:", secret)
        break
    else:
        print("❌ Wrong!")
else:
    print("💀 Game Over! Number was:", secret)
