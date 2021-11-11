from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required

def index():
    posts = [
        {
            'author': {'username': 'Test 2'},
            'body': 'Welcomeee!'
        },
        {
            'author': {'username': 'Test 1'},
            'body': 'Hellooo'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# temporary hard coding of the data till importing from db
projects_headings = ("ID", "User_ID", "Name", "Description", "Budget")
projects_data = (
    ("1", "4", "RTF", "Realtime Face Recognition", "120000"),
    ("2", "5", "IOT", "Internet of Things", "2044000"),
    ("3", "6", "VAR", "Video Action Review", "7034000"),
)
expenses_headings = ("ID", "Project_ID", "Category_ID", "Name", "Description", 
                    "Amount", "Created_At", "Created_By", "Updated_At", "Updated_By")
expenses_data = (
                ("1", "2", "2", "RTF", "Realtime Face Recognition", "9000", "2021-11-04T16:00:00.000Z",
                 "Jacky", "2021-11-06T16:00:00.000Z", "Jacky"),
                 ("1", "2", "2", "RTF", "Realtime Face Recognition", "9000", "2021-11-04T16:00:00.000Z",
                 "Jacky", "2021-11-06T16:00:00.000Z", "Jacky"),
                 ("1", "2", "2", "RTF", "Realtime Face Recognition", "9000", "2021-11-04T16:00:00.000Z",
                 "Jacky", "2021-11-06T16:00:00.000Z", "Jacky")


)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', projects_headings=projects_headings, projects_data=
                            projects_data, expenses_headings = expenses_headings, expenses_data = expenses_data)
