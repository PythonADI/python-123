temps = [17, 18, 17, 16, 17, 18, 20, 21, 22, 23, 30, 31]

print(type(temps))
print(temps)
print(len(temps))

for temp in temps:
    print(f"{temp} celsius")

    if temp > 30:
        print("It was hot")
    elif temp < 20:
        print("it was chill")
    else:
        print("Fine temperature")


print("-" * 10)
print(temps[0])
print(temps[1])
print(temps[3])
# print(temps[len(temps) - 1])
print(temps[-1])



# change elements
temps[0] = 25
temps[len(temps) // 2] = 28

print(temps)



# appending new elements
print("-" * 10)
temps.append(25)
temps.append(29)
temps.insert(len(temps) // 2, -17)
print(temps)


# Deleing elements
print("-" * 10)
temps.pop()
temps.append(-17)

temps.remove(-17)
# temps.remove(-17)
print(temps)


# print(temps.index(-17))

# Be careful

# print(temps[1000])
# temps.pop(1000)
