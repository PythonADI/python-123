def to_celsius(fahrenheit):
    return round((5 / 9) * (fahrenheit - 32), 2)


x = to_celsius(105)
print(x)
if x > 30:
    print("It is hot outside")


x = to_celsius(109)

temps = []

if x > 12:
    temps.append(x)


print(temps)