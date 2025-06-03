from flask import render_template


def root():
    return render_template('index.html')
