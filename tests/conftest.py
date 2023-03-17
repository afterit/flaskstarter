import os
import shutil

import pytest


@pytest.fixture(scope="module")
def testing_directory():
    path = os.path.join(os.getcwd(), "test_dir")
    try:
        os.mkdir(path)
    except FileExistsError:
        pytest.fail("Couldn't create the test_dir to use on tests")
    yield path
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pytest.fail("Couldn't remove the test_dir tree.")
