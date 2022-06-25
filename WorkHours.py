import sqlite3 as sql
from datetime import date

today = date.today()

hours = input("How many hours did you work?")

connection = sql.connect("hours.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS hours (
    day DATE,
    hours TEXT
)
""")

cursor.execute("""
INSERT INTO hours 
VALUES(?, ?) 
""", (today, hours))

cursor.execute("""
SELECT * FROM hours
ORDER BY day DESC;
""")

rows = cursor.fetchall()

connection.commit()
connection.close()
print(rows)