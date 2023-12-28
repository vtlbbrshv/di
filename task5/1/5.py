import pymongo
from bson.son import SON
from bson.json_util import dumps
import pandas as pd
import json


def write_result(name, result):
    with open(name, "w", encoding="utf-8") as file:
        file.write(dumps(result))


collection = pymongo.MongoClient("localhost", 27017).mongodi.people

data = pd.read_csv("task_1_item.csv", sep=";")
payload = json.loads(data.to_json(orient="records"))
collection.insert_many(payload)

first_pipeline = [
    {"$limit": 10},
    {"$sort": SON([("salary", -1)])},
]
write_result("res1.json", list(collection.aggregate(first_pipeline)))

second_pipeline = [
    {"$limit": 15},
    {"$match": {"age": {"$lt": 30}}},
    {"$sort": SON([("salary", -1)])},
]
write_result("res2.json", list(collection.aggregate(second_pipeline)))

third_pipeline = [
    {"$limit": 10},
    {
        "$match": {
            "$and": [
                {"city": "Фигерас"},
                {"job": {"$in": ["Психолог", "Учитель", "Водитель"]}},
            ]
        }
    },
    {"$sort": SON([("age", 1)])},
]
write_result("res3.json", list(collection.aggregate(third_pipeline)))

fourth_pipeline = [
    {
        "$match": {
            "$and": [
                {"$and": [{"age": {"$lt": 30}}, {"year": {"$in": [2019, 2022]}}]},
                {
                    "$or": [
                        {
                            "$and": [
                                {"salary": {"$gt": 50000}},
                                {"salary": {"$lte": 75000}},
                            ]
                        },
                        {
                            "$and": [
                                {"salary": {"$gt": 125000}},
                                {"salary": {"$lt": 150000}},
                            ]
                        },
                    ]
                },
            ]
        }
    }
]
write_result("res4.json", list(collection.aggregate(fourth_pipeline)))
