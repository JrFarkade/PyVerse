# user greeting program

def greet_user(first_name, last_name, address_place, mobile_no):
    print("\n--- Greeting Message ---")
    print(f"Hello! My name is {first_name} {last_name}.")
    print(f"I live in {address_place} with my parents.")
    print(f"My mobile number is: {mobile_no}")
    print("Nice to meet you! 😊")


print("Start")

# Taking input from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
address_place = input("Enter your address/place: ")
mobile_no = input("Enter your mobile number: ")

greet_user(first_name, last_name, address_place, mobile_no)

print("End")
