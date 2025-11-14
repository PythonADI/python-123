import random

FIRST_NAMES = ("John", "Jane", "Alex", "Emily", "Chris", "Katie")
LAST_NAMES = ("Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas")

def create_random_user():
    return {
        "name": random.choice(FIRST_NAMES),
        "last_name": random.choice(LAST_NAMES),
        "age": random.randint(0, 100)
    }


# user = {
#     # "name": FIRST_NAMES[random.randint(0, len(FIRST_NAMES) - 1)],
#     # "last_name": LAST_NAMES[random.randint(0, len(LAST_NAMES) - 1)]
#     "name": random.choice(FIRST_NAMES),
#     "last_name": random.choice(LAST_NAMES)
# }


user = create_random_user()
user2 = create_random_user()

print(user)
print(user2)
