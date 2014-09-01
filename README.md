flask-crud
==========
example flask crud api

install

environment
install pyenv, virtualenv, pyenv-virtualenv
install packages necessary to build python from source
install db packages: mysql-client, mysql-server mysql-common libmysql-dev

project setup
pyenv virtualenv 2.7.8 venv-2.7.8-flask-crud
pip install -r requirements.txt
mysql -uroot -p -e 'CREATE DATABASE `flask_asset` CHARACTER SET utf8 COLLATE utf8_general_ci'
alembic upgrade head
