import code
import sys, os
import textwrap
from fabric.api import *


@task
def test(name='all'):
    """
    run the test suite
    """
    command = """for file in `ls tests/*.py`; do python $file; done"""
    local(command)


@task
def server():
    local('python app.py')


@task
def shell():
    # interactive shell with flask and sqlalchemy
    import os
    import code, readline, os

    project_top = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    sys.path.insert(0, project_top)
    from flaskapi import app
    import flaskapi
    #import flaskapi
    #from flask_environments import Environments
    #env = Environments(app)
    #env.from_yaml(os.path.join(project_top, 'flaskapi', 'config', 'config.yml'))

    PROJECT_NAME = "flaskapi"

    # pick up the current frame
    # try:
    #    raise None
    #except:
    #    frame = sys.exc_info()[2].tb_frame.f_back

    # evaluate commands in current namespace
    #namespace = frame.f_globals.copy()
    #namespace.update(frame.f_locals)
    #namespace.update(dict( app=app, db=db, env=env ))
    namespace = globals().copy()
    namespace.update(locals())

    banner = """
    {1}~~~~~~
    {0} shell
    {1}~~~~~~
    """.format(PROJECT_NAME, '~' * len(PROJECT_NAME))

    code.interact(banner=banner, local=namespace)
