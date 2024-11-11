from flask import render_template, request
from .models import User

def register_routes(app, db):
    @app.route('/')
    def index():
        return render_template('core/index.html', script='scripts/index.js', styles='css/index.css')


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('core/register.html', styles='css/register.css')
        elif request.method == 'POST':
            pass


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('core/login.html', styles='css/login.css')
        elif request.method == 'POST':
            pass