product = {
    # key : value
    "name": "Cabbage",
    "price": 3.99
}

print(product["name"])
# print(product["sku"])
product["sku"] = "1U78HVEXD"
product["name"] = "Cabbage (Expired)"
product.pop("price")

print(product)