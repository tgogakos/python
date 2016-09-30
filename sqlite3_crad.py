#!/usr/bin/python

import sqlite3


def insert(db, row):
    db.execute('insert into crud (t1, i1) values (?,?)', (row['t1'], row['i1']))
    db.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from crud where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update crud set i1=? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete(db, t1):
    db.execute('delete from crud where t1 = ?', (t1,))
    db.commit()

def disp_rows(db):
    cursor = db.execute('select * from crud order by t1')
    for row in cursor:
        print('{}:{}'.format(row['t1'], row['i1']))


def main():
    db = sqlite3.connect('crud.db')
    db.row_factory = sqlite3.Row
    print("create table crud")
    db.execute('drop table if exists test')
    db.execute('create table crud (t1 text, i1 float)')

    print('create rows')
    insert(db, dict(t1 = 'one', i1 = 1.0))
    insert(db, dict(t1 = 'two', i1 = 2.0))
    insert(db, dict(t1 = 'three', i1 = 3.0))
    insert(db, dict(t1 = 'four', i1 = 4.0))
    disp_rows(db)
 
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    update(db, dict(t1 = 'one', i1 = 100.1))

    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    delete(db, 'one')
    disp_rows(db)
    
    print("-------")

    delete(db, 'three')
    disp_rows(db)
if __name__ == "__main__":main() 
