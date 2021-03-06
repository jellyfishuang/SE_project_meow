from models.pg_model import pg_model
from models.sqlite import sqlite_model
import os


class model():
    dao = sqlite_model()
    # dao = pg_model()
    """
    Board(name=name, description=description,
    bucket_list=bucket_list, manager=manager).create()
    datetime format: '2007-01-01 10:00:00'
    """

    def create(self):
        return model.dao.create(type(self).__name__, self.__dict__)
    """
    Q(name=name)
    Q.add(description=description, Q.OR)
    Q.add(bucket_list=bucket_list, Q.AND)
    Board.filter(Q)
    """
    @classmethod
    def filter(cls, q):
        return model.dao.filter(cls.__name__, q)
    """
    Board.filter(name=name, description=description,
    bucket_list=bucket_list, manager=manager)
    """
    @classmethod
    def filter(cls, **kwargs):
        return model.dao.filter(cls.__name__, **kwargs)


class Q():
    AND = 0
    OR = 1

    def __init__(self, **kwargs):
        self.querystring = ""
        self.parameter = ()
        if len(kwargs) == 1:
            for arg in kwargs:
                self.querystring = arg + " = ?"
                self.parameter = (str(kwargs[arg]),)

    def add(self, q, op):
        if op == 0:
            op_str = "AND"
        elif op == 1:
            op_str = "OR"
        self.querystring += " " + op_str + " "
        self.querystring += q.querystring
        self.parameter += (q.parameter)