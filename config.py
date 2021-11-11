import os
#basedir = os.path.abspath(os.path.dirname(__insert file here__))

class Config(object):
    SECRET_KEY = os.environ.get('KEY') or 'admin'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(__insertbasedirhere_, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False