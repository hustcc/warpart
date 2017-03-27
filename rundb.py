# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2017

@author: hustcc
'''
from warpart import SQLAlchemyDB as db
from sqlalchemy import text
import sys


reload(sys)
sys.setdefaultencoding('utf8')


def build_db():
    '''
    build db：重新生成数据库
    '''
    # 创建数据库结构
    db.drop_all()
    db.create_all()
    # 导入唐诗
    sql = ''
    for line in open("doc/tang.sql"):
        sql += line
        if sql.strip().endswith(';'):
            db.session.execute(text(sql))
            sql = ''
    db.session.commit()


if __name__ == '__main__':
    build_db()
