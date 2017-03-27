# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2017

@author: hustcc
'''
from warpart import SQLAlchemyDB as db
from warpart.database.base import BaseMethod


class Poet(db.Model, BaseMethod):
    '''诗人'''
    __tablename__ = 'poet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))  # 诗人名字


class Poetry(db.Model, BaseMethod):
    '''诗'''
    __tablename__ = 'poetry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))  # 诗题目
    content = db.Column(db.Text)  # 诗内容

    poet_id = db.Column(db.Integer, db.ForeignKey(Poet.id))  # 诗人
    poet = db.relationship(Poet, foreign_keys=poet_id, uselist=False)
