hero = {
    "name": "Test",
    "class": "Knight of an order",
    "rank": "Grand Master",
    "gold": 0,
    "hp": 100,
    "xp": 0,
    "inventory": [1, 2, 3, 4],
    "weapon": None
}


print(hero)

hero["weapon"] =  {
    "name": "bow",
    "damage": 25,
    "description": "Jin Sakai's bow",
    "rarity": "Epic"
}


print(hero["weapon"])
print(hero["weapon"]["damage"])
