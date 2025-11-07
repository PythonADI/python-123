numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -100, -99, 18, 746, 24, 677545]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

print("----------")
# for i in range(5):
#     print(i, numbers[i])

# for i in range(len(numbers) - 5, len(numbers)):
#     print(i, numbers[i])

for number in numbers[:5]:
    print(number)

# print(numbers[len(numbers) - 5:len(numbers)])
print(numbers[-5:])
# print(numbers[:])

print(numbers[::2])
print(numbers[::-1])


