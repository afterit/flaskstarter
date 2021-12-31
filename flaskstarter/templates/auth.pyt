{% extends 'ext.pyt' %}
{% block imports %}
from flask_login import LoginManager
{% endblock %}
{% block globalobjects %}
loginmanager = LoginManager()
{% endblock %}
{% block inits %}
    loginmanager.init_app(app)
{% endblock %}