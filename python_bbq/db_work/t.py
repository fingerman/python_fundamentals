import os, sys, sqlite3

connection = sqlite3.connect("firma.db")
cur = connection.cursor()


# sql = '''INSERT INTO salesman VALUES('5002', 'Nail Knite', 'Paris', 0.13)'''

sql = '''UPDATE salesman SET name = 'Pit Alex', city = 'London', comission = 0.11 WHERE salesman_id = 5003; '''
cur.execute(sql)
connection.commit()
