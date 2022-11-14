import json

file = "main_dataset.json"

with open(file, "r") as json_file:
    data = json.load(json_file)
    for product_data in range(len(data)):
        products = {
                    "pk": product_data+1,
                    "modal": "product.products",
                    "fields": data[product_data]
                    }
        with open('products_new.json', 'a', newline="") as f:
            books = products, ''
            json.dump(books, f, indent=4)


# with open('products_test.json', 'a', newline="") as f:
#     books = []
#     json.dump(books, f, indent=4)
