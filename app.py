from flask import Flask, request, jsonify, session, render_template, url_for, request, redirect
import pymongo
from pymongo import MongoClient
from flask.json import JSONEncoder
from bson import ObjectId
from datetime import date
import bcrypt

app = Flask(__name__)

MONGO_URI = "mongodb://user:Aa123456@ds055980.mlab.com:55980/flaskinterview"
client = pymongo.MongoClient(MONGO_URI, retryWrites=False)
db = client.get_default_database('flaskinterview')

user_records = db.user_records
message_records = db.message_records


@app.route('/')
def main():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return "Welcome to my FLASK website"


@app.route("/sendMessage", methods=['POST'])
def sendMessage():
    req_data = request.form.to_dict()
    sender = req_data["sender"]
    receiver = req_data["receiver"]
    message = req_data["message"]
    subject = req_data["subject"]
    today = date.today()
    c_d = today.strftime("%d/%m/%Y")
    pushMessage(sender, receiver, message, subject, c_d)
    return "sendMessage Page"


@app.route('/messages/<string:user_id>')
def GetAllMessages(user_id):
    records = getAllRecords(user_id)
    return jsonify({'messages': records})


@app.route('/unreadmessages/<string:user_id>')
def GetAllUnreadMessages(user_id):
    records = getAllUnreadRecords(user_id)
    return jsonify({'messages': records})


@app.route('/readMessage/<string:message_id>')
def ReadMessage(message_id):
    record = ReadMessage(message_id)
    return jsonify({'messages': record})


@app.route('/delete/<string:message_id>')
def deleteMessage(message_id):
    DeleteMessage(message_id)
    return "delete page"


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        existing_user = user_records.find_one(
            {"id": request.form['id']}, {'_id': 0})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            user_records.insert(
                {'id': request.form['id'], 'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return 'register complete'

        return 'That username already exists!'

    return 'register page'


@app.route('/login', methods=['POST'])
def login():

    login_user = user_records.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('main'))

    return 'Invalid username or password'


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
    records = message_records.find({'receiver': int(user_id)}, {'_id': 0})
    return convertCursorToObject(records)


"""
INPUT : user_id
OUTPUT: All unread messages of a specific user
"""


def getAllUnreadRecords(user_id):
    records = message_records.find({
        'receiver': int(user_id),
        'Seen': 'false'
    }, {'_id': 0})
    return convertCursorToObject(records)


# UPDATE METHOD

"""
INPUT : message_id
OUTPUT:
"""


def ReadMessage(message_id):
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


def DeleteMessage(message_id):
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


def convertCursorToObject(cursor):
    x = []
    for i in cursor:
        x.append(i)
    return x


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run()
