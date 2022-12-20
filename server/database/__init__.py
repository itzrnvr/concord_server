import json
from typing import List
from uuid import uuid4

from ..models.message import Message, EditMessage
from ..models.user import User

db: List[User] = [
    User(id=uuid4(), username="admin", password="12345")
]

messagesDb: List[Message] = []


class Database:

    def findUser(self, username):
        dat = [False, None]
        for i, user in enumerate(db):
            if user.username == username:
                dat = [True, db[i]]
                break

        return dat

    def login(self, user):
        response = {0: "None"}
        dbUser = self.findUser(user.username)
        if dbUser[0]:
            if dbUser[1].password == user.password:
                response = dbUser[1]

        return response

    def register(self, user):
        response = {}
        dbUser = self.findUser(user.username)
        if not dbUser[0]:
            newUser = User(pfp=user.pfp, username=user.username, password=user.password)
            db.append(newUser)
            response = newUser

        return response

    def deleteUser(self, id):
        for user in db:
            if user.id == id:
                db.remove(user)
                return

    def getAllUsers(self):
        users = []
        for user in db:
            users.append({"id": str(user.id),
                          "pfp": user.pfp,
                          "username": user.username})
        return json.dumps(users)

    def addChat(self, pfp, username, message):
        messagesDb.append(Message(pfp=pfp, username=str(username), message=message))

    def editMessage(self, editMes: EditMessage):
        for i, mes in enumerate(messagesDb):
            if mes.id == editMes.id:
                mes.message = editMes.message
                messagesDb[i] = mes
                return {"id": mes.id, "username": mes.username, "message": mes.message}

    def deleteMessage(self, messageID):
        for message in messagesDb:
            if message.id == messageID:
                messagesDb.remove(message)

    def getAllChats(self):
        messages = []
        for message in messagesDb:
            messages.append({"mId": str(message.id),
                             "pfp": message.pfp,
                             "username": message.username,
                             "message": message.message})
        return json.dumps(messages)
