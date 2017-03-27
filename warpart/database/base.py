# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2017

@author: hustcc
'''
from warpart import SQLAlchemyDB as db


# 一些公共的方法，仅仅适合单独操作，对于事务操作，还是需要手工写db.session代码
class BaseMethod(object):
    # 全部配置
    __table_args__ = {
        'mysql_engine': 'MyISAM',
        'mysql_charset': 'utf8'
    }

    # 添加和修改
    def save(self):
        db.session.add(self)
        db.session.commit()

    # 删除
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}  # noqa
