import sqlite3 as sql
from datetime import date

today = date.today()

hours = input("How many hours did you work?")

connection = sql.connect("hours.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Hours (
    day TEXT,
    hours TEXT
)
""")

cursor.execute("""
INSERT INTO Hours VALUES
('{today}', '{hours}')
""")

cursor.execute("""
SELECT * FROM hours
""")

rows = cursor.fetchall()
print(rows)


connection.commit()

connection.close()
