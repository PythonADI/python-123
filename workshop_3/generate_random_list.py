import random

numbers = []

for i in range(100):
    numbers.append(random.randint(-100, 100))

s = 0
for number in numbers:
    s += number

print(numbers)
print(s / len(numbers))
print(sum(numbers) / len(numbers))
