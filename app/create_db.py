import json
from app import app, db
from app.models import User

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file) 
        file.close() 
    return jsn

def create_users():     
    user = load_json('user.json')

    for oneUser in user:
        id = oneUser["id"]
        username = oneUser["username"]
        password = oneUser["password"]
        name = oneUser["name"]
        appointment = oneUser["appointment"]

        newUser = User(id=id, username=username,password=password,name=name,appointment=appointment)
        db.session.add(newUser)
        db.session.commit()

create_users()  