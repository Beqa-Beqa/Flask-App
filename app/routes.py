from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Post

def register_routes(app, db):
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            posts = Post.query.all()
            own_posts = Post.query.filter_by(owner_id=current_user.uid).all()
            print(own_posts)
            return render_template('authenticated/index.html', styles='css/index.css', posts=posts)
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
            
            if user: 
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Invalid credentials'
        
    
    @app.route('/logout', methods=['POST'])
    def logout():
        logout_user()
        return redirect(url_for('login'))
    
    
    @app.route('/create-post', methods=['POST'])
    def create_post():
        title = request.form.get('title')
        content = request.form.get('content')
        
        new_post = Post(title=title, content=content, owner_id=current_user.uid)
        
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('index'))