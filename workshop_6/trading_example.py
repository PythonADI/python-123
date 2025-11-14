eth = {
  "symbol": "ETHUSDT",
  "price": 3225.79
}

btc = {
  "symbol": "BTCUSDT",
  "price": 97116.35
}


print(f"{eth["symbol"]} costs {eth["price"]}")
print(f"{btc["symbol"]} costs {btc["price"]}")

ethbtc = {
    "symbol": "ETHBTC",
    "price": btc["price"] / eth["price"]
}

btceth = {
    "symbol": "BTCETH",
    "price": eth["price"] / btc["price"]
}

print(f"{ethbtc["symbol"]} costs {ethbtc["price"]}")
print(f"{btceth["symbol"]} costs {btceth["price"]}")


def convert(from_currency, to_currency):
    """This function converts from one currency to another"""
    return to_currency / from_currency


prices = {
    "BTCUSDT": 97116.35,
    "ETHUSDT": 3225.79,
}

prices.update(
    {
        "BTCETH": convert(prices["BTCUSDT"], prices["ETHUSDT"]),
        "ETHBTC": convert(prices["ETHUSDT"], prices["BTCUSDT"])
    }
)

print(prices)
