# -*- coding: utf-8 -*-
# __author__ = 'yafengstark'

# 这是中文注释
import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")
conn.commit()
conn.close()
# BLOB字段，对应python buffer类型
# c.execute('''CREATE TABLE tiles
#            (qk text PRIMARY KEY     NOT NULL,
#            data         BLOB);''')