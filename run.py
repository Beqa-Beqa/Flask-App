from app import create_app

# If this file is run, then run the flask application
# We need run.py to avoid circular imports ( if it occurs, app will crash )
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)