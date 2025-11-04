import random

x = random.randint(0, 100)
tries = 7

# secret number - 56
# 50
# higher
# 75
# lower
# 56
# correct - stop program
while True:
    if tries <= 0:
        print("You lose")
        break
    tries -= 1
    guess = int(input("Guess: "))

    if guess > x:
        print("Lower")
        continue
    if guess < x:
        print("Higher")
        continue

    print("Correct")
    break
