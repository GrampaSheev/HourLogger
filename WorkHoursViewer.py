import sqlite3 as sql

connection = sql.connect("hours.db")

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM hours
ORDER BY day DESC;
""")

rows = cursor.fetchall()

print(rows) 

connection.commit()
connection.close()

