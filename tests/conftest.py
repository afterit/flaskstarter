import pytest

@pytest.fixture(scope='module')
def teste():
    '''Just to test if fixtures are present and working'''
    return 'oi'