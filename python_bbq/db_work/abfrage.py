import os, sys, sqlite3

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql = "SELECT * FROM salesman"
cursor.execute(sql)
for data in cursor:
    print(data[0], data[1], data[2], data[3])
