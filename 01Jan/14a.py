# Person Class

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}.")


# Take input from user
user_name = input("Enter your name: ")

# Create object
p1 = Person(user_name)

# Print name and make the person talk
print("Name:", p1.name)
p1.talk()
