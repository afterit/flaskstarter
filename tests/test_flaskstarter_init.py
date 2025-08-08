import os
import sys
import types
from unittest.mock import patch

import pytest

# Ensure package can be imported from src layout
sys.path.insert(0, os.path.join(os.getcwd(), "src"))


def _install_templating_stub():
    templating_stub = types.ModuleType("flaskstarter.tools.templating")

    class Dummy:
        def render(self, **kwargs):
            return ""

    def get_template(name):
        return Dummy()

    templating_stub.get_template = get_template
    sys.modules["flaskstarter.tools.templating"] = templating_stub


_install_templating_stub()

from flaskstarter import flaskstart_cli


def _run_init(target_dir):
    with patch("os.getcwd", return_value=target_dir):
        flaskstart_cli.init.callback(".")


@pytest.fixture(scope="module")
def testing_directory():
    path = os.path.join(os.getcwd(), "test_dir")
    os.mkdir(path)
    yield path
    # cleanup
    import shutil
    shutil.rmtree(path)


def test_project_is_created_with_default_name(testing_directory):
    _run_init(testing_directory)
    needed = {"manage.py", "instance", "test_dir"}
    assert set(os.listdir(testing_directory)) == needed
    assert os.path.isfile(
        os.path.join(testing_directory, "test_dir", "blueprints", "__init__.py")
    )
