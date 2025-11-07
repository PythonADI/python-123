# products = [
#     "Cabbage",
#     "Snickers",
#     "Cold Drinks",
#     "Bananas",
#     "Cheese",
#     "Beef"
# ]

# prices = [
#     3.99,
#     2.5,
#     12,
#     5,
#     12,
#     20
# ]

# products = [
#     ["Cabbage", 3.99],
#     ["Snickers", 2.5],
#     ["Cold Drinks", 12],
# ]

products = [
    {
        "name": "Cabbage",
        "price": 3.99
    },
    {
        "name": "Snickers",
        "price": 2.5
    },
    {
        "name": "Cold Drinks",
        "price": 12
    }
]


# print(products[0]["name"])
# Summarry
for product in products:
    print(product["name"], product["price"])

# checkout

s = 0 
for product in products:
    s += product["price"]

s = round(s, 2)
print(s)
