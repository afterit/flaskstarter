from flask import Blueprint

{% if not templates: %}
bp = Blueprint('{{name}}', __name__, url_prefix='/{{name}}')
{% else: %}
bp = Blueprint('{{name}}', __name__, url_prefix='/{{name}}', template_folder='templates')
{% endif %}

@bp.route('/')
def root():
    return 'Hello from {{name}}'


def init_app(app):
    app.register_blueprint(bp)