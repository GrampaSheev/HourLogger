import sqlite3 as sql
from datetime import date

today = date.today()

connection = sql.connect("hours.db")

cursor = connection.cursor()


cursor.execute("""
  CREATE Table Hours
""")

connection.commit()

connection.close()
