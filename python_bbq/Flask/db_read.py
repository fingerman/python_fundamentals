import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': '',
            'database': 'vsearchlogdb',
            }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
#_SQL = '''describe log'''
_SQL = '''select * from log'''
#_SQL = """DELETE FROM log WHERE id = 5 """
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

conn.commit()
cursor.close()
conn.close()

