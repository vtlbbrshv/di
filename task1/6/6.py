import pip._vendor.requests 
from json2html import json2html

data = pip._vendor.requests.get("https://random-data-api.com/api/v2/users",
                   params={ 'size': 2 }).json()


html_table = json2html.convert(json=data)

with open('res.html', 'w', encoding='utf-8') as f:
    f.write(html_table)