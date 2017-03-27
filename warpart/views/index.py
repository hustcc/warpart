# -*- coding: utf-8 -*-
'''
Created on 2016-10-20

@author: hustcc
'''

from warpart import app
from warpart.database.model import Poetry
import flask
import random


# index
@app.route('/', methods=['GET'])
def index():
    # get random id
    total_poetry = Poetry.query.count()
    r = random.uniform(1, total_poetry)

    r = Poetry.query.filter(Poetry.id < r).order_by(Poetry.id.desc()).first()
    r = r and r.id or 1
    return poetry_page(r)


# poetry_id
@app.route('/<poetry_id>.html', methods=['GET'])
def poetry_page(poetry_id):
    # poetry_id should be number
    if not str(poetry_id).isdigit():
        return 'intercepted.'

    poetry = Poetry.query.get(poetry_id)
    if not poetry:
        return 'intercepted.'
    poet = poetry.poet
    # stat
    total_poetry = Poetry.query.count()
    total_poet = Poetry.query.count()
    # prev, next
    prev = Poetry.query.filter(Poetry.id < poetry.id) \
                 .order_by(Poetry.id.desc()).first()
    prev = prev and prev.id or None

    next = Poetry.query.filter(Poetry.id > poetry.id) \
                 .order_by(Poetry.id.asc()).first()
    next = next and next.id or None

    return flask.render_template('index.html',
                                 poet=poet,
                                 poetry=poetry,
                                 total_poet=total_poet,
                                 total_poetry=total_poetry,
                                 prev=prev,
                                 next=next)
