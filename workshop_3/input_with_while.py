user_input = input("Please Enter PIN: ")
# print(f"{len(user_input) == 4 = }")
# print(f"{user_input.isdigit() = }")

while len(user_input) != 4 or not user_input.isdigit():
    print("user input is incorrect, please use only numbers and make it 4 digits")
    user_input = input("Please Enter PIN: ")


number = int(user_input)
print("Successfully saved PIN")
