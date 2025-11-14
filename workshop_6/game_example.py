hero = {
    "hp": 100,
    "damage": 15
}

monster = {
    "hp": 100,
    "damage": 15
}

while True:
    hero["hp"] -= monster["damage"]
    print(hero["hp"])
    if hero["hp"] <= 0:
        break

print(hero["hp"])
print(monster["hp"])
