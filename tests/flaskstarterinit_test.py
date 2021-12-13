'''Flaskstarter init tests.
'''
import os
import requests
import signal
import subprocess as shell
import time

def test_project_is_created_with_default_name(testing_directory):
    '''Tests if a project is created on a given location.

    This test runs the init command with default naming for
    main package. It asserts if the content is equal to the
    expected for a fresh project source.
    '''
    cmd = f'cd {testing_directory}; flaskstarter init .'
    shell.run(cmd, shell=True, check=True)
    needed = ['manage.py', 'instance', 'test_dir', 'requirements.txt']
    content = os.listdir(testing_directory)
    assert content == needed


def test_flaskstarter_projet_runs(testing_directory):
    '''Tests if fresh project is runnable. 
    '''
    cmd = f'cd {testing_directory}; python manage.py runserver'
    app = shell.Popen(cmd, stdout=shell.PIPE, shell=True, preexec_fn=os.setsid)
    time.sleep(2)
    get_root = 'http://127.0.0.1:5000/'
    response = requests.get(get_root)

    os.killpg(os.getpgid(app.pid), signal.SIGTERM)

    assert response.status_code == 200
