import sqlite3 as sql
from datetime import date

today = input("What day did you work YY/MM/DD") 

hours = input("How many hours did you work?")

connection = sql.connect("hours.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS hours (
    day TEXT,
    hours INT
)
""")

cursor.execute("""
INSERT INTO hours 
VALUES(?, ?) 
""", (today, hours))


connection.commit()
connection.close()
