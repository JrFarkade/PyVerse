# Age Validator Program

try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    elif age > 120:
        print("Invalid age! Please enter a realistic age.")
    else:
        print(f"Your age is {age}.")
        print("✅ Input accepted. Thank you!")

except ValueError:
    print("❌ Invalid input! Please enter age in numbers only (example: 18).")
