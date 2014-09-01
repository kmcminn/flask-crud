# flask-crud
an example flask crud api

## Installation

### environment
1. install pyenv, virtualenv, pyenv-virtualenv
2. install packages necessary to build python from source
3. install db packages: mysql-client, mysql-server mysql-common libmysql-dev
 
### project setup
1. pyenv virtualenv 2.7.8 venv-2.7.8-flask-crud
2. pip install -r requirements.txt
3. mysql -uroot -p -e 'CREATE DATABASE `flask_asset` CHARACTER SET utf8 COLLATE utf8_general_ci'
4. alembic upgrade head
5. test with fab tasks
