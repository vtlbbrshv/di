# На всякий случай, здесь и во всех остальных случаях выходные данные
# в формате json форматирую с помощью prettier
# для читаемости (html в предыдущем задании кстати тоже)

import json
import numpy as np

data = np.load('matrix_83.npy')
size = len(data)

res = dict()
res['sum'] = 0
res['avr'] = 0
res['sumMD'] = 0
res['avrMD'] = 0
res['sumSD'] = 0
res['avrSD'] = 0
res['max'] = data[0][0]
res['min'] = data[0][0]

for i in range(0, size):
    for j in range(0, size):
        res['sum'] += data[i][j]

        if i == j:
            res['sumMD'] += data[i][j]

        if i + j == (size - 1):
            res['sumSD'] += data[j][j]

        res['max'] = max(res['max'], data[i][j])
        res['min'] = max(res['min'], data[i][j])

res['avr'] = res['sum'] / (size ** 2)
res['avrMD'] = res['sumMD'] / size
res['avrSD'] = res['sumSD'] / size

for key in res.keys():
    res[key] = float(res[key])

with open('res.json', 'w') as file:
    file.write((json.dumps(res)))

data = np.ndarray((size, size), dtype=float)

for i in range(0, size):
    for j in range(0, size):
        data[i][j] = data[i][j] / res['sum']


perem = 0
for i in data:
    perem+=sum(i)

np.save('res_norm', data)