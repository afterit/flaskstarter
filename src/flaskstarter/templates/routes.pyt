from flask import current_app as app, render_template

{% if login and db %}from {{name}}.entities import User{% endif %}

@app.route('/')
def root():
    return render_template('index.html')
