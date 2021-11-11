import json
from app import app, db
from app.models import User, Project, Category, Expense
from dateutil import parser
import datetime

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file) 
        file.close() 
    return jsn

def create_users():     
    user = load_json('user.json')
    if User.query.filter_by(id=1).first() is None:
        for oneUser in user:
            username = oneUser["username"]
            password = oneUser["password"]
            name = oneUser["name"]
            appointment = oneUser["appointment"]

            newUser = User(username=username,password=password,name=name,appointment=appointment)
            db.session.add(newUser)
            db.session.commit()

create_users()  

def create_project():     
    user = load_json('project.json')
    if Project.query.filter_by(id=1).first() is None:
        for oneUser in user:
            user_id = oneUser["user_id"]
            name = oneUser["name"]
            budget = oneUser["budget"]
            description = oneUser["description"]

            newUser = Project(user_id=user_id,name=name,budget=budget,description=description)
            db.session.add(newUser)
            db.session.commit()

create_project()  

def create_category():     
    user = load_json('category.json')
    if Category.query.filter_by(id=1).first() is None:

        for oneUser in user:
            name = oneUser["name"]

            newUser = Category(name=name)
            db.session.add(newUser)
            db.session.commit()

create_category()  

def create_expense():     
    user = load_json('expense.json')
    if Expense.query.filter_by(id=1).first() is None:
        for oneUser in user:
            project_id = oneUser["project_id"]
            category_id = oneUser["category_id"]
            name = oneUser["name"]
            description = oneUser["description"]
            amount = oneUser["amount"]
            created_at = parser.parse(oneUser['created_at']).date()
            created_by = oneUser["created_by"]
            updated_at = parser.parse(oneUser['updated_at']).date()
            updated_by = oneUser["updated_by"]

            newUser = Expense(project_id=project_id,category_id=category_id,name=name,description=description,amount=amount,created_at=created_at,created_by=created_by,updated_at=updated_at,updated_by=updated_by)
            db.session.add(newUser)
            db.session.commit()

    # db.session.close()

create_expense()  