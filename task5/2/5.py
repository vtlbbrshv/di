import pymongo
from bson.son import SON
from bson.json_util import dumps
import pandas as pd
import json


def write_result(name, result):
    with open(name, "w", encoding="utf-8") as file:
        file.write(dumps(result))


collection = pymongo.MongoClient("localhost", 27017).mongodi.people
data = pd.read_pickle("task_2_item.pkl")
payload = json.loads(dumps(data))
collection.insert_many(payload)

# write_result("for_me.json", data)

first_pipeline = [
    {
        "$group": {
            "_id": "null",
            "avg": {"$avg": "$salary"},
            "min": {"$min": "$salary"},
            "max": {"$max": "$salary"},
        }
    }
]

write_result("res1.json", list(collection.aggregate(first_pipeline)))
