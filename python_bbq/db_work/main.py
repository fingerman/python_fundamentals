import os, sys, sqlite3

# if os.path.exists("firma.db"):
#     print("Datei bereits vorhanden")
#     sys.exit(0)

# Mit DB kommunizieren, wenn nich vorhanden, dann eine DB erzeugen
connection = sqlite3.connect("firma.db")
# Cursor-Objekt erzeugen
cursor = connection.cursor()

# Tabelle erzeugen
# sql = "CREATE TABLE personen(" \
#       "name TEXT, " \
#       "vorname TEXT, " \
#       "personalnummer INTEGER PRIMARY KEY, " \
#       "gehalt REAL, " \
#       "geburtstag TEXT)"
#
# cursor.execute(sql)
# connection.commit()

# Datensatz erzeugen
# sql = "INSERT INTO personen VALUES('Maier', " \
#       "'Hans', 6714, 3500, '15.03.1962')"
# cursor.execute(sql)
# connection.commit()

# Datensatz(2) erzeugen
# sql = "INSERT INTO personen VALUES('Schmitz', " \
#       "'Peter', 81343, 3750, '12.04.1958')"
# cursor.execute(sql)
# connection.commit()

# Datensatz erzeugen
# sql = "INSERT INTO personen VALUES('Mertens', " \
#       "'Julia', 2297, 3621.5, '30.12.1959')"
# cursor.execute(sql)
# connection.commit()
#
# sql = "INSERT INTO personen VALUES('Mertens', " \
#       "'Behruz', 22971, 5000, '30.12.1989')"
# cursor.execute(sql)
# connection.commit()
# # Verbindung beenden
connection.close()