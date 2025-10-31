# Implicit conversion
total = 5 + 3.2  # int + float → float
print(total)  # Output: 8.2

print(9 / 3, type(9 / 3))

# Explicit conversion
count_str = "42"
count_int = int(count_str)
print(count_int + 8)  # Output: 50


x = 27
print(str(x), type(str(x)))

x = 9.8
print(int(x))
