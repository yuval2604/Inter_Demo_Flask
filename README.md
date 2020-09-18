# Inter_Demo_Flask

My Flask website

The task is to write a simple rest API backend system that responsible of
handling messages between users.
a message contains :

1. sender (owner)
2. receiver
3. message
4. subject
5. creation date

   The rest API should contains :

- Write message
- Get all messages for a specific user
- Get all unread messages for a specific user
- Read message (return one message)
- Delete message (as owner or as receiver)

Deploy a new MongoDB(mlab) project

Build 2 collections :

user_records:

id - string
name - string
password - string

message_records:

0. \_id - Assigned Degaulty by mongo db

1. sender (owner) - user_id -string
2. receiver - user_id - string
3. message - string
4. subject - string
5. creation date - date

Future developmennt/ Default values assign :

MongoDB assigned a defalut hash value to represnt the object

# a flag represent if the message seen/read or not

6. Seen - bool

note :

user id cann't be an integer cause can start with 0
therefore define as string
