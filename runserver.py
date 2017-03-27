# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2017

@author: hustcc
'''
from warpart import app
# from gevent.wsgi import WSGIServer
# from gevent import monkey
# monkey.patch_all()  # patch


def runserver(port=10028):
    app.run('0.0.0.0', port, debug=False, threaded=False)
    # http_server = WSGIServer(('0.0.0.0', port), app)
    # http_server.serve_forever()


if __name__ == '__main__':
    runserver()
