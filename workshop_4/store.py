"""
let's imagine that we have a store. we have robotic carts,
when user add an item to their cart item will be automatically detected
and added to their bill.

we have list of users with their carts, and in these carts we have items.
we have to process these carts and generate bills for each user.
when we process current we have to remove them from list. first users is in front
"""

users = [
    {
        "name": "Alice",
        "cart": [
            {"name": "Cabbage", "price": 3.99},
            {"name": "Snickers", "price": 2.5},
            {"name": "Cold Drinks", "price": 12}
        ]
    },
    {
        "name": "Bob",
        "cart": [
            {"name": "Bananas", "price": 5},
            {"name": "Cheese", "price": 12},
            {"name": "Beef", "price": 20}
        ]
    },
    {
        "name": "Charlie",
        "cart": [
            {"name": "Apples", "price": 4.5},
            {"name": "Bread", "price": 3.25},
            {"name": "Milk", "price": 2.75}
        ]
    },
    {
        "name": "Diana",
        "cart": [
            {"name": "Eggs", "price": 6},
            {"name": "Orange Juice", "price": 4.5},
            {"name": "Yogurt", "price": 3}
        ]
    }
]

while len(users) != 0:
    user = users.pop(0)
    print(f"Hello {user["name"]}")
    amount = 0
    for product in user["cart"]:
        print(f"{product["name"]} costs ${product["price"]}")
        amount += product["price"]
    
    amount = round(amount, 2)
    print(f"Total: ${amount}")

    print(f"There are currently {len(users)} in queue")
    print("\n")