{% extends 'ext.pyt' %}

{% block imports %}
from flask_login import LoginManager
from {{project}}.models import User
{% endblock %}

{% block globalobjects %}
login_manager = LoginManager()
{% endblock %}

{% block inits %}
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
{% endblock %}
