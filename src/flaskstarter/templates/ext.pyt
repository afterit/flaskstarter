from typing import NoReturn
from flask import Flask

{% block imports %}
# Place here the extension's dependencies
{% endblock %}

{% block globalobjects %}
# Place here your extension globals
{% endblock %}

def init_app(app : Flask) -> NoReturn:
    {% block inits %}
    '''Init your global objects which do need to connect to flask object.'''
    {% endblock %}
