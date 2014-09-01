import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_environments import Environments
from flask.ext.bootstrap import Bootstrap
from jinja2 import Environment, PackageLoader


# init flask app
app = Flask(__name__)

# init db con
db = SQLAlchemy(app)

# configure flask
env = Environments(app)
env.from_yaml(os.path.join(os.getcwd(), 'flaskapi', 'config', 'config.yml'))

# configure jinja
env = Environment(loader=PackageLoader('flaskapi', 'templates'))
env.filters['jsonify'] = jsonify

# bootstrap
bootstrap = Bootstrap(app)

# TODO: configure per environment logging

# app module imports
import models.asset
import controllers.api
import controllers.errors