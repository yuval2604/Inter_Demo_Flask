import pymongo
from pymongo import MongoClient
from flask.json import JSONEncoder
from bson import ObjectId
from datetime import date


MONGO_URI = "mongodb://user:Aa123456@ds055980.mlab.com:55980/flaskinterview"
client = pymongo.MongoClient(MONGO_URI, retryWrites=False)
db = client.get_default_database('flaskinterview')

user_records = db.user_records
message_records = db.message_records


# GET METHODS:

# To pull data from collection use
# db.user_records.find_one({'_id': ObjectId('5f631c6f9e6f2c95e3f688d5')} )
"""
INPUT : user_id
OUTPUT: User record - Info of the user
"""


def getOneUserRecord(user_id):
    record = user_records.find_one({"id": user_id}, {'_id': 0})
    return record


"""
INPUT : user_id
OUTPUT: All messages of a specific user
"""


def getAllRecords(user_id):
    records = message_records.find({'receiver': (user_id)}, {'_id': 0})
    return convertCursorToObject(records)


"""
INPUT : user_id
OUTPUT: All unread messages of a specific user
"""


def getAllUnreadRecords(user_id):
    records = message_records.find({
        'receiver': (user_id),
        'Seen': 'False'
    }, {'_id': 0})
    return convertCursorToObject(records)


# UPDATE METHOD

"""
INPUT : message_id
OUTPUT:
"""


def ReadMessageFunc(message_id):
    record = message_records.find_one_and_update(
        {'_id': ObjectId(message_id)},
        {"$set":
         {"Seen": "True"}
         },
        upsert=True)
    record.pop('_id')
    return (record)


# DELETE METHOD

"""
INPUT : message_id
OUTPUT:
"""


def DeleteMessageFunc(message_id):
    message_records.delete_one(
        {
            "_id": ObjectId(message_id)
        }
    )


# CREATE METHOD
# To push data to the collection


def pushMessage(sender_id, receiver_id, message, subject, creation_date):
    record = {
        "sender": sender_id,
        "receiver": receiver_id,
        "message": message,
        "subject": subject,
        "creation_date": creation_date,
        'Seen': 'False'
    }
    message_records.insert_one(record)


# Convert pymongo.cursor -> dict
def convertCursorToObject(cursor):
    x = []
    for i in cursor:
        x.append(i)
    return x
