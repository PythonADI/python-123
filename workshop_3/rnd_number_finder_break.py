import random

SEARCH_NUMBER = 56
tries = 0
while True:
    tries += 1
    x = random.randint(0, 100)
    if x == SEARCH_NUMBER:
        break

print(f"we found {x} in {tries} tries")
