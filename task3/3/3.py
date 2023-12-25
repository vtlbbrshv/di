from bs4 import BeautifulSoup
import numpy as np
import re
import json
import lxml

def handle_file(file_name):
    with open(file_name, encoding="utf-8") as file:
        text = ""
        for s in file.readlines():
            text += s

        tag = BeautifulSoup(text, 'xml').star
        item = dict()
        for el in tag.contents:
            if el.name is not None:
                item[el.name] = el.get_text().strip()
                
        return item

items = []
for i in range(1, 500):
    file_name = f"zip_var_83/{i}.xml"
    items.append(handle_file(file_name))
    
with open("res.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(items))
    
items = sorted(items, key=lambda x: int(x['radius']), reverse=True)

with open("resRadius.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(items))

filtered = []
for item in items:
    if float(item['distance'].replace(' million km', '').strip()) >= 6000000:
        filtered.append(item)

with open("resDistance.json", 'w', encoding="utf-8") as result:
    result.write(json.dumps(filtered))