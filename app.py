from flask import Flask
import pymongo
from pymongo import MongoClient
app = Flask(__name__)

MONGO_URI = "mongodb://user:Aa123456@ds055980.mlab.com:55980/flaskinterview"
client = pymongo.MongoClient(MONGO_URI)
db = client.get_default_database('flaskinterview')
user_records = db.user_records


@app.route('/')
def hello():
    record = getRecord("5f627ac9e7179a472eae094e")
    print(record)
    pushRecord(1, "Amit", "16", "OPEN")
    record = getRecord(1)
    print(record)
    return "Hello World!"


def getRecord(user_id):
    record = user_records.find_one({"user_id": user_id})
    return record


def pushRecord(user_id, name, Age, college):
    record = {
        "user_id": user_id,
        "name": name,
        "Age": Age,
        "college": college
    }
    user_records.insert_one(record)


if __name__ == '__main__':
    app.run()
