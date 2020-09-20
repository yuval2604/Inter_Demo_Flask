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

EX:
sender: 2
receiver: 3
message : "hello world'
subject : "Hi , This is my message"

OR
https://interviewheroku.herokuapp.com/sendMessage

http://localhost:5000/messages/2
OR
https://interviewheroku.herokuapp.com/messages/2

http://localhost:5000/unreadmessages/2
OR
https://interviewheroku.herokuapp.com/unreadmessages/2

http://localhost:5000/readMessage/5f67a2d6416d6b4b5ca758b3
OR
https://interviewheroku.herokuapp.com/readMessage/5f67a2d6416d6b4b5ca758b3

http://localhost:5000/delete/5f67a2d6416d6b4b5ca758b3
OR
https://interviewheroku.herokuapp.com/delete/5f67a2d6416d6b4b5ca758b3

In auth branch
(with parameters - id , name, password)
http://localhost:5000/register
