import random

def f(x):
    return x ** 2


def t(x):
    return f(x) + 2


def check_balance():
    print("Checking balance ...")
    return random.choice((True, False))


def complete_transaction():
    print("Completing transaction ...")


def place_order():
    if check_balance():
        complete_transaction()
        return {
            "order_id": random.randint(0, 10000),
            "total": random.randint(500, 10000),
            "status": "Success"     
        }
    return {
        "order_id": None,
        "total": None,
        "status": "Failed"
    }

print(f"composition {__name__ = }")



if __name__ == "__main__":
    # print(f(2))
    # print(t(3))

    orders = [
        place_order(),
        place_order(),
        place_order(),
    ]

    for order in orders:
        if order["status"] == "Failed":
            print("Check your balance")
        print(order)
