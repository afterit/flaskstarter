from flask import current_app as app

@app.route('/')
def root():
    return "Hello from flask!"
