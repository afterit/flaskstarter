import pytest
from flaskstarter.flaskstart_cli import init

@pytest.fixture()
def generate_project_init_params():
    test_input = [
        'testproject',
        'yes',
        'yes',
        'yes',
        'yes'
    ]
    expected_output = 0
    return test_input, expected_output

def test_init_command(generate_project_init_params):
    test_input, expected_output = generate_project_init_params
    assert init(test_input) == expected_output
