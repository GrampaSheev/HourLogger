import sqlite3 as sql

connection = sql.connect("hours.db")

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM hours
""")

rows = cursor.fetchall()

connection.commit()
connection.close()
print(rows)
