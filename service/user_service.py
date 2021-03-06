import logging

from bson import ObjectId
from pymongo import MongoClient

from util.env_util import LOG_FILE_PATH, MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_COLLECTION

# set up logging
logging.basicConfig(filename=LOG_FILE_PATH, encoding='utf-8', level=logging.DEBUG)

# set up mongo
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DATABASE]
collection = db[MONGO_COLLECTION]


def insert_user(data):
    logging.info(f"inserting {data}")
    return collection.insert_one(data).inserted_id


def get_user_by_id(obj_id):
    logging.info(f"fetching {obj_id}")
    return collection.find_one({"_id": ObjectId(obj_id)})


def list_users(query):
    logging.info(f"listing {query}")
    return collection.find(query)


def update_user(find_query, update_query, multi=False):
    logging.info(f"updating find_query={find_query}, update_query={update_query}, multi={multi}")
    if multi:
        collection.update_many(find_query, {"$set": update_query})
        return list_users(find_query)
    else:
        collection.update_one(find_query, {"$set": update_query})
        return list(list_users(find_query))[0]


def delete_user(query, multi=False):
    logging.info(f"deleting query={query}, multi={multi}")
    if multi:
        return collection.delete_many(query).deleted_count
    else:
        return collection.delete_one(query).deleted_count
