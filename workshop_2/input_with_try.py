first_name = input("Name: ") # user might enter invalid data, BUT!! 

try:
    age = int(input("Number: "))
    print(age + 1)
except ValueError:
    print("Please enter correct number")

print(f"Hello {first_name}")