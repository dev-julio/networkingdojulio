from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '7d62cac23f612b14b03542ef82f127ed'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from networkingdojulio import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criado")
else:
    print('base de dados ja existente')

from networkingdojulio import routes
