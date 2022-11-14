import json


def new_info(data, filename="main_data_test.json"):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        for product_data in range(len(data)):
            products = {
                        "pk": product_data+1,
                        "modal": "product.products",
                        "fields": data[product_data]
                        }
            books = products, ","
            return books

#     with open(filename, "r") as json_file:
#         data = json.load(json_file)
#         for product_data in range(len(data)):
#             products = {}
#             products["pk"] = product_data+1
#             products["modal"] = "product.products"
#             products["fields"] = data[product_data]
#             return products
#             print(products)


def write_json(data, filename="new_product.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


with open("new_product.json", "r") as json_file:
    data = json.load(json_file)
    temp = data["books"]
    y = new_info(data)
    temp.append(y)

write_json(data)
