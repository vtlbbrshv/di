import json, os, msgpack

with open('products_83.json') as f:
    data = json.load(f)
    products = dict()

    for item in data:
        if item['name'] in products:
            products[item['name']].append(item['price'])
        else:
            products[item['name']] = list()
            products[item['name']].append(item['price'])

    result = list()

    for name, prices in products.items():
        sum_price = 0
        max_price = prices[0]
        min_price = prices[0]
        size = len(prices)

        for price in prices:
            sum_price += price
            max_price = max(max_price, price)
            min_price = min(min_price, price)

        result.append({
            'name': name,
            'max': max_price,
            'min': min_price,
            'avr': sum_price / size,
        })

    with open('res.json', 'w') as r_json:
        r_json.write(json.dumps(result))

    with open('res.msgpack', 'wb') as r_msgpack:
        r_msgpack.write(msgpack.dumps(result))
