import pymongo
from bson.son import SON
from bson.json_util import dumps
import pandas as pd
import json


def write_result(name, result):
    with open(name, "w", encoding="utf-8") as file:
        file.write(dumps(result))


def get_stats_aggregation(id, field):
    return {
        "$group": {
            "_id": id,
            "avg": {"$avg": f"${field}"},
            "min": {"$min": f"${field}"},
            "max": {"$max": f"${field}"},
        }
    }


collection = pymongo.MongoClient("localhost", 27017).mongodi.people
data = pd.read_pickle("task_2_item.pkl")
payload = json.loads(dumps(data))
collection.insert_many(payload)

first_pipeline = [get_stats_aggregation("null", "salary")]
write_result("res1.json", list(collection.aggregate(first_pipeline)))

second_pipeline = [
    {
        "$group": {"_id": "$job", "count": {"$sum": 1}},
    },
]
write_result("res2.json", list(collection.aggregate(second_pipeline)))

third_pipeline = [get_stats_aggregation("$city", "salary")]
write_result("res3.json", list(collection.aggregate(third_pipeline)))

fourth_pipeline = [get_stats_aggregation("$job", "salary")]
write_result("res4.json", list(collection.aggregate(fourth_pipeline)))

fifth_pipeline = [get_stats_aggregation("$city", "age")]
write_result("res5.json", list(collection.aggregate(fifth_pipeline)))

sixth_pipeline = [get_stats_aggregation("$job", "age")]
write_result("res6.json", list(collection.aggregate(sixth_pipeline)))

min_age_pipeline = [{"$group": {"_id": "null", "age": {"$min": "$age"}}}]
min_age = list(collection.aggregate(min_age_pipeline))[0]["age"]
seventh_pipeline = [
    {"$match": {"age": min_age}},
    {"$group": {"_id": "null", "max": {"$max": "$salary"}}},
]
write_result("res7.json", list(collection.aggregate(seventh_pipeline)))

max_age_pipeline = [{"$group": {"_id": "null", "age": {"$max": "$age"}}}]
max_age = list(collection.aggregate(max_age_pipeline))[0]["age"]
eighth_pipeline = [
    {"$match": {"age": max_age}},
    {"$group": {"_id": "null", "max": {"$min": "$salary"}}},
]
write_result("res8.json", list(collection.aggregate(eighth_pipeline)))

ninth_pipeline = [
    {"$match": {"salary": {"$gt": 50000}}},
    get_stats_aggregation("$city", "age"),
    {"$sort": SON([("age", -1)])},
]
write_result("res9.json", list(collection.aggregate(ninth_pipeline)))

tenth_pipeline = [
    {
        "$match": {
            "$and": [
                {
                    "$or": [
                        {"$and": [{"age": {"$gt": 18}}, {"age": {"$lt": 25}}]},
                        {"$and": [{"age": {"$gt": 50}}, {"age": {"$lt": 65}}]},
                    ]
                },
                {"city": {"$in": ["Варшава", "Самора", "Бишкек"]}},
                {"job": {"$in": ["Врач", "Программист", "Архитектор"]}},
            ]
        },
    },
    get_stats_aggregation("null", "salary"),
]
write_result("res10.json", list(collection.aggregate(tenth_pipeline)))

eleventh_pipeline = [
    {"$match": {"age": {"$gt": 30}}},
    get_stats_aggregation("$year", "salary"),
    {"$sort": SON([("avg", -1)])},
]
write_result("res11.json", list(collection.aggregate(eleventh_pipeline)))
