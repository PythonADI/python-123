
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        # self.full_name = f"{first_name} {last_name}"
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(f"Hello {self.full_name()}, your username is {self.username}")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def change_name(self, name):
        self.first_name = name


user = User("Legend27", "Joe", "Doe")
dog = Dog("Fluffy", 3)

print(user.username, user.full_name)
user.greet()
user.change_name("Nick")
print(user.first_name)
user.greet()
print(dog.name)

users = []
for i in range(10):
    users.append(
        User(f"User {i}", f"first name {i}", f"last name {i}")
    )

for user in users:
    user.greet()

# "Hello".lower()

# lower("Hello")
