# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2017

@author: hustcc
'''
from warpart import app
# from gevent.wsgi import WSGIServer
# from gevent import monkey
# monkey.patch_all()  # patch


def runserver(port=10028, debug=False):
    app.run('0.0.0.0', port, debug=debug, threaded=False)
    # http_server = WSGIServer(('0.0.0.0', port), app)
    # http_server.serve_forever()


if __name__ == '__main__':
    runserver(debug=True)
