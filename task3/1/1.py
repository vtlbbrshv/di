from bs4 import BeautifulSoup
import re
import json
import numpy as np


def min_rate(items):
    filtered_items = []
    for building in items:
       if building['views'] > 200:
           filtered_items.append(building)

    with open('filteredRes.json', 'w', encoding='utf-8') as f:
      f.write(json.dumps(filtered_items))


def handle_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        text = ''
        for row in file.readlines():
            text += row
            
        site = BeautifulSoup(text, 'html.parser')
        item = dict()
        item['city'] = site.find_all("span", string=re.compile("Город:"))[0].get_text().replace("Город:", "").strip()
        item['building'] = site.find_all("h1", string=re.compile("Строение:"))[0].get_text().replace("Строение:", "").strip().split("Индекс")
        address = site.find_all('p', attrs={'class': 'address-p'})[0].get_text()
        item['street'] = address[0].replace('Улица:', '').strip()
        item['index'] = address[1].strip()
        item['floors'] = int(site.find_all('span', attrs={'class': 'floors'})[0].get_text().split(':')[1].strip())
        item['year'] = int(site.find_all('span', attrs={'class': 'year'})[0].get_text().split('в')[1].strip())
        item['parking'] = site.find_all("span", string=re.compile("Парковка:"))[0].get_text().split(':')[1].strip()
        item['img'] = site.find_all('img')[0]['src']
        item['views'] = int(site.find_all("span", string=re.compile("Просмотры:"))[0].get_text().split(':')[1].strip())
        item['rating'] = float(site.find_all("span", string=re.compile("Рейтинг:"))[0].get_text().split(':')[1].strip())

        return item
    
items = []
for i in range(1,999):
    file_name = f'zip_var_83/{i}.html'
    result = handle_file(file_name)
    items.append(result)

items = sorted(items, key=lambda x: x['views'], reverse=True)

with open('res.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(items))

min_rate(items)

views = list()

for item in items:
    views.append(int(item['views']))

result_num = {}
result_num['max'] = str(np.max(views))
result_num['min'] = str(np.min(views))
result_num['avg'] = str(np.average(views))
result_num['sum'] = str(np.sum(views))
result_num['std'] = str(np.std(views))
result_text = {}


for item in items:
    print(item, item['city'])
    print(" ")
    elements = item['city']
    if(elements in result_text):
        result_text[elements] += 1
    else:
        result_text[elements] = 1

result_num['text'] = result_text

with open('stat.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(result_num))
