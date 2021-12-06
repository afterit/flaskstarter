import os


def test_fixture_exist(teste):
    """A simple test.

    Args:
        teste (pytest fixture): A test fixture.
    """
    assert teste == "oi"


def test_create_tempdir(testing_directory):
    """[summary]

    Args:
        testing_directory ([type]): [description]
    """
    os.mkdir(os.path.join(testing_directory, "pasta"))
    assert True
