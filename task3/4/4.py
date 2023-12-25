from bs4 import BeautifulSoup
import numpy as np
import re
import json

def handle_file(file_name):
    items = list()

    with open(file_name, encoding="utf-8") as file:
        text = ""
        for row in file.readlines():
            text += row

        root = BeautifulSoup(text, 'xml')
        for clothing in root.find_all("clothing"):
            item = dict()
            for el in clothing.contents:
                if el.name is None:
                    continue
                elif el.name == "price" or el.name == "reviews":
                    item[el.name] = int(el.get_text().strip())
                elif el.name == "rating":
                    item[el.name] = float(el.get_text().strip())
                elif el.name == "new":
                    item[el.name] = el.get_text().strip() == "+"
                elif el.name == "exclusive" or el.name == "sporty":
                    item[el.name] = el.get_text().strip() == "yes"
                else:
                    item[el.name] = el.get_text().strip()
            items.append(item)

        return items


items = []
for i in range(1, 100):
    file_name = f"zip_var_83/{i}.xml"
    items += handle_file(file_name)
    
with open("res.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(items))

filtered = []
for item in items:
    if item['price'] >= 500000:
        filtered.append(item)
with open("resPrice.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(filtered))
    

items = sorted(items, key=lambda x: x['rating'], reverse=True)
with open("resRating.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(items))