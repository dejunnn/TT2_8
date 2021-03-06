from flask_restful import Resource
from app import db
from app import login
from datetime import datetime
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# class UserModel(Resource)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))#, unique=True)
    password= db.Column(db.String(64), nullable = False)
    #password_hash = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    appointment = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return (self.password == password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(128))
    budget = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Project {}>'.format(self.name)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(128))
    amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.String(64))
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String(64))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Expense {}>'.format(self.name)



db.create_all()