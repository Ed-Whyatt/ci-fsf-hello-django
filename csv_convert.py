import json
import csv


with open("main_data_test.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"image": row[0], "name": row[1], "auther": row[2], "format": row[3], "book_depository_stars": row[4], "price": row[5], "currency": row[6], "old_price": row[7], "isbn": row[8], "category": row[9], "img_paths": row[10]})
        print(data)
