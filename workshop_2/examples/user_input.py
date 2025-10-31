user_input = input("Enter your age: ")
try:
    age = int(user_input)
    print(f"In 5 years, you will be {age + 5} years old.")
except ValueError:
    print("Please enter a valid number.")
