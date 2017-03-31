# -*- coding: utf-8 -*-
'''
Created on Mar 28, 2017

@author: hustcc
'''
import datetime


def max_id():
    start = datetime.datetime(2017, 3, 28, 0, 0, 0, 0)
    now = datetime.datetime.now()
    # datetime timedelta
    dtd = (now - start).total_seconds()
    # 每隔 30 分钟一首
    return dtd // 1800


def poetry_datetime(poetry_id):
    start = datetime.datetime(2017, 3, 28, 0, 0, 0, 0)
    return start + datetime.timedelta(seconds=poetry_id * 1800)


if __name__ == '__main__':
    print(max_id())
    print(poetry_datetime(169))
