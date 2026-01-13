# Simple Calculator Program in Python

num1 = int(input("Enter the 1st number: "))
operator = input("Choose an operator (+, -, *, /): ")
num2 = int(input("Enter the 2nd number: "))

# Perform calculation based on the operator
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid operator! Please choose +, -, * or /.")
