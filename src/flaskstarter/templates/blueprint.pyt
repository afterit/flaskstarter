from flask import Blueprint

bp = Blueprint('{{name}}', __name__, url_prefix='/{{name}}')

@bp.route('/')
def root():
    return "Hello from {{name}}"