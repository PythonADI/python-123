import random

tries = 0
x = random.randint(0, 100)
while x != 56:
    tries += 1
    x = random.randint(0, 100)

print(x)
print(f"We found {x} in {tries} tries")
