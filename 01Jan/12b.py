# Weight Converter Program (Kilograms ↔ Pounds)

weight = float(input("Enter your weight: "))
unit = input("Is this weight in (K) kilograms or (P) pounds? ").strip().upper()

if unit == "K":
    pounds = weight * 2.2046226218
    print(f"Your weight in pounds is: {pounds:.2f} lbs")

elif unit == "P":
    kilograms = weight * 0.45359237
    print(f"Your weight in kilograms is: {kilograms:.2f} kg")

else:
    print("Invalid input! Please enter 'K' for kilograms or 'P' for pounds.")
