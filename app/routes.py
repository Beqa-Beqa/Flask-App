from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from .models import User

def register_routes(app, db):
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return current_user.username
        else:
            people = User.query.all()
            return render_template('core/index.html', script='scripts/index.js', styles='css/index.css', people=people)


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('core/register.html', styles='css/register.css')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            age = request.form.get('age')
            
            new_user = User(username=username, password=password, age=age)
            
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('index'))


    @app.route('/login',  methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('core/login.html', styles='css/login.css')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = User.query.filter_by(username=username, password=password).one_or_none()
            print(user)
            
            if user: login_user(user)
                
            return f'Success login {current_user.username}'
        
    
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        logout_user()
        return 'Success logout'