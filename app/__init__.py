
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os
load_dotenv()



app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["API_KEY"] = os.getenv("API_key")


class Base(DeclarativeBase):
    pass



db = SQLAlchemy(model_class=Base)

db.init_app(app)


login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "NEED LOGIN"
login_manager.init_app(app)

from .models import User
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id: int):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    # print(user)
    return user

from app.routes import *
