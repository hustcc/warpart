# -*- coding: utf-8 -*-
'''
Created on 2015年6月16日

@author: hustcc
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 版本号
__version__ = '0.0.1'


# flask
app = Flask(__name__)


# flask-sqlalchemy
dbi = 'mysql+pymysql://root:root@127.0.0.1/warpart'
app.config['SQLALCHEMY_DATABASE_URI'] = dbi
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLAlchemyDB = SQLAlchemy(app)


from warpart.util import jinja  # noqa
from warpart.database import model  # noqa
from warpart import views  # noqa
