import json

file = "products/fixtures/products.json"

with open(file, "r") as json_file:
    data = json.load(json_file)
    for i in data:
        if i == "category":
            print(i)
