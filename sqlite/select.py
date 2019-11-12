# -*- coding: utf-8 -*-
# __author__ = 'yafengstark'

# 这是中文注释

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print("Opened database successfully")

cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()

# sql = ("update student t set t.name = '%s',"
#      "t.sex = '%s',"
#      "t.age = '%s',"
#      "t.height = '%s',"
#      "t.weight = '%s',"
#      "t.class = '%s',"
#      "t.stuid = '%s',"
#      "t.xxx = '%s'"
#      " where t.stuid= '%s'"
#      " and t.xxx = 'P';" %(A,B,A,B,B,A,A,B,C)
#   )