# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2017

@author: hustcc
'''
from warpart import app
import sys


reload(sys)
sys.setdefaultencoding('utf8')


def poetry_content(content):
    content = content or ''
    content = content.split('。')
    content = ["%s。" % c for c in content if c.strip()]
    return content


app.jinja_env.filters.update({'poetry_content': poetry_content})
