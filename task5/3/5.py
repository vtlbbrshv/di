import json
import msgpack
import pandas as pd
from bson.json_util import dumps

import pymongo


def write_result(name, result):
    with open(name, "w", encoding="utf-8") as file:
        file.write(dumps(result))


collection = pymongo.MongoClient("localhost", 27017).mongodi.people
f = open("task_3_item.json")
data = json.load(f)
collection.insert_many(data)


res = collection.delete_many(
    {
        "$or": [
            {"salary": {"$lt": 25_000}},
            {"salary": {"$gt": 175_000}},
        ]
    }
)
print(res)


res = collection.update_many({}, {"$inc": {"age": 1}})
print(res)


res = collection.update_many(
    {"job": {"$in": ["Повар", "Учитель", "Бухгалтер"]}}, {"$mul": {"salary": 1.05}}
)
print(res)


res = collection.update_many(
    {"city": {"$in": ["Ереван", "Махадаонда", "Тбилиси"]}},
    {"$mul": {"salary": 1.07}},
)
print(res)


res = collection.update_many(
    {
        "$and": [
            {"city": {"$in": ["Ереван", "Москва", "Тбилиси"]}},
            {"job": {"$in": ["Программист", "IT-специалист", "Инженер"]}},
            {"age": {"$gt": 50}},
        ]
    },
    {"$mul": {"salary": 1.1}},
)
print(res)


res = collection.delete_many(
    {
        "$and": [
            {"city": {"$in": ["Ташкент"]}},
            {"job": {"$in": ["Косметолог", "IT-специалист", "Бухгалтер"]}},
        ]
    }
)
print(res)
