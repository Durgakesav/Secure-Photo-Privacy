from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'login'

    with app.app_context():
        db.create_all()
    
    return app