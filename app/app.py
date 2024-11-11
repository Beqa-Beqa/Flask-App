from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app_db.db'
    app.secret_key = 'MY SECRET KEY'
    
    db.init_app(app)
    
    login_manager = LoginManager(app)
    # login_manager.init_app(app)
    
    from .models import User
    
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    from .routes import register_routes
    register_routes(app, db)
    
    migrate = Migrate(app, db)
    
    with app.app_context():
        db.create_all()
    
    return app