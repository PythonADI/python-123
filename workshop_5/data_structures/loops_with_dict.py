person = {
    "first_name": "George",
    "last_name": "Washington",
    "age": 25
}


# explicit is always better than implicit
# for key in person:
#     print(key, person[key])

for value in person.values():
    print(value)

for key in person.keys():
    print(key)

print("-------")
for key, value in person.items():
    print(key, value)
