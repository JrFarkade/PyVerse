# Student Marks Calculator

name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

# Grade system
if percentage >= 95:
    print("Grade: A+")
elif percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 55:
    print("Grade: D")
elif percentage >= 35:
    print("Grade: E")
else:
    print("Grade: Fail")
