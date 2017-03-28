# -*- coding: utf-8 -*-
'''
Created on 2016-10-20

@author: hustcc
'''

from warpart import app
from warpart.database.model import Poetry, Poet
from warpart.util import date_util
import flask


# index
@app.route('/', methods=['GET'])
def index():
    max_id = date_util.max_id()
    return poetry_page(max_id)


# poetry_id
@app.route('/<poetry_id>.html', methods=['GET'])
def poetry_page(poetry_id):
    max_id = date_util.max_id()
    # poetry_id should be number
    if not str(poetry_id).isdigit():
        return 'intercepted.'

    try:
        poetry_id = int(poetry_id)
    except:
        return 'intercepted.'

    if poetry_id > max_id:
        return 'intercepted.'

    poetry = Poetry.query.get(poetry_id)
    if not poetry:
        return 'intercepted.'

    poet = poetry.poet
    # stat
    total_poetry = Poetry.query.filter(Poetry.id <= max_id).count()
    total_poet = Poet.query.count()
    # prev, next
    prev = Poetry.query.filter(Poetry.id < poetry.id, Poetry.id <= max_id) \
                 .order_by(Poetry.id.desc()).first()
    prev = prev and prev.id or None

    next = Poetry.query.filter(Poetry.id > poetry.id, Poetry.id <= max_id) \
                 .order_by(Poetry.id.asc()).first()
    next = next and next.id or None

    return flask.render_template('index.html',
                                 poet=poet,
                                 poetry=poetry,
                                 total_poet=total_poet,
                                 total_poetry=total_poetry,
                                 prev=prev,
                                 next=next)


@app.route('/sitemap.xml', methods=['GET'])
@app.route('/sitemap.html', methods=['GET'])
def sitemap():
    max_id = date_util.max_id()
    poetries = Poetry.query.filter(Poetry.id <= max_id) \
                     .order_by(Poetry.id.desc()).all()
    sitemap_xml = flask.render_template('sitemap.xml', poetries=poetries)
    response = app.make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
