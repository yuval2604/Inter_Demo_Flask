from datetime import date

from flask import Flask, jsonify, request

from .functions import *

app = Flask(__name__)

MONGO_URI = "mongodb://user:Aa123456@ds055980.mlab.com:55980/flaskinterview"
client = pymongo.MongoClient(MONGO_URI, retryWrites=False)
db = client.get_default_database('flaskinterview')

user_records = db.user_records
message_records = db.message_records


# Default page
# If already login redirect to relevant page
@app.route('/')
def main():
    return "ok"


# Create a new message
# INPUT  :  sender , receiver, message, subject
# OUTPUT :
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


# Sends back to the user all the messages recieve by this user
# INPUT  : message_id
# OUTPUT : Mesaages as json
@app.route('/messages/<string:user_id>')
def GetAllMessages(user_id):
    records = get_all_records(user_id)
    return jsonify({'messages': records})


# Sends back to the user all the Unread messages recieve by this user
@app.route('/unreadmessages/<string:user_id>')
def GetAllUnreadMessages(user_id):
    records = getAllUnreadRecords(user_id)
    return jsonify({'messages': records})


# Read a meessage
# INPUT  : message_id
# OUTPUT : mesaage as json
@app.route('/readMessage/<string:message_id>')
def ReadMessage(message_id):
    record = ReadMessageFunc(message_id)

    return jsonify({'messages': record})


# Delete a meessage
# INPUT  : message_id
# OUTPUT
@app.route('/delete/<string:message_id>')
def deleteMessage(message_id):
    DeleteMessageFunc(message_id)
    return "delete page"


if __name__ == '__main__':
    app.run()
