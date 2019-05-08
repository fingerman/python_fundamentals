import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': '',
            'database': 'vsearchlogdb',
            }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """insert into log
          (phrase, letters, ip, browser_string, results)
          values
          ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL)
conn.commit()
cursor.close()
conn.close()


