# create 2 demo users:

pushNewUserRecord(1,'Yuval', 1)

pushNewUserRecord(2,'Yoav', 2)

->Can be also create in the auth branch using register page

# create 4 Messages

today = date.today()

d1 = today.strftime("%d/%m/%Y")

msg1 = 'hello world'

msg2= 'good morning'

pushMessage(1, 2 , msg1, 'msg1',d1 )

pushMessage(2, 1 , msg2, 'msg2',d1 )

pushMessage(1, 2 , msg1, 'msg3',d1 )

pushMessage(1, 2 , msg1, 'msg4',d1 )

# Update - READ MESSAGE

ReadMessage('5f6487c69e6f2c95e3f688da')

# GET - SHOW MESSAGE

getAllRecords(2)

getAllUnreadRecords(2)

# DELETE - DELETE MESSAGE

DeleteMessage('5f6487c69e6f2c95e3f688db')

POST REQUESTS :

(with parameters in body - sender, receiver, message, subject)
http://localhost:5000/sendMessage

http://localhost:5000/messages/2

http://localhost:5000/unreadmessages/2

http://localhost:5000/readMessage/5f648b4d9e6f2c95e3f688dc

http://localhost:5000/delete/5f648b4d9e6f2c95e3f688dc

In auth branch
(with parameters - id , name, password)
http://localhost:5000/register
