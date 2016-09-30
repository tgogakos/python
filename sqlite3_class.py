#!/usr/bin/python

import sqlite3

class database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()








def main():
    db = database(filename = 'test2.db', table = 'test')

    print('create table test')
    db.sql_do('drop table if exists test2')
    db.sql_do('create table test (t1 test, i1 float)')

    print('create 
