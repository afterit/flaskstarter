from jinja2 import Environment, PackageLoader, select_autoescape, Template

env = Environment(
    loader=PackageLoader('flaskstarter', 'templates'),
    autoescape=select_autoescape('pyt', 'htmlt', 'tomlt')
)

def get_template(name : str) -> Template:
    """Retrieves and return the specified template.

    Args:
        name (str): Template's name

    Returns:
        Template: A Jinja2 Template object.
    """
    return env.get_template(name)