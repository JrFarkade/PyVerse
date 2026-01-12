# Day Weather Checker Program

weather = input("How is the weather today? (hot/cold/normal): ").strip().lower()

if weather == "hot":
    print("It's a hot day.")
    print("Drink plenty of water 💧")

elif weather == "cold":
    print("It's a cold day.")
    print("Wear warm clothes 🧥")

elif weather == "normal":
    print("It's a normal day.")
    print("Have a great day 😊")

else:
    print("Invalid input! Please enter: hot, cold, or normal.")

print("\nWatch One Piece 🏴‍☠️🔥")
