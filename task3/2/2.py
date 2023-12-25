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

        site = BeautifulSoup(text, 'html.parser')
        products = site.find_all("div", attrs={'class': 'product-item'})
        item = dict()
        for product in products:

            item['id'] = product.a['data-id']
            item['link'] = product.find_all('a')[1]['href']
            item['img_link'] = product.find_all('img')[0]['src']
            item['product_name'] = product.find_all('span')[0].get_text().strip()
            item['price'] = int(product.price.get_text().replace('₽', '').replace(' ', '').strip())
            item['bonus'] = int(product.strong.get_text().replace('+ начислим ', '').replace('бонусов', '').strip())

            props = product.ul.find_all("li")

            for prop in props:
                item[prop['type']] = prop.get_text().strip()

            items.append(item)

        return items


items = []
for i in range(1, 91):
    file_name = f"zip_var_83/{i}.html"
    items += handle_file(file_name)
with open("res.json", 'w', encoding="utf-8") as result:
        result.write(json.dumps(items))

items = sorted(items, key=lambda x: x['price'], reverse=True)

with open("resPrice.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(items))

filtered = []

for item in items:
    if item['price'] > 100000:
        filtered.append(item)

with open("resBonus.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(filtered))
