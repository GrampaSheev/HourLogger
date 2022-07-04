import sqlite3 as sql
import tkinter as tk
from tkinter import *
from datetime import date

window = tk.Tk()
window.title("Selection")
window.geometry("300x300")

def Selection():
    if type.get() == "Logger":
        today = date.today()
        Logger=tk.Tk()
        Logger.title("Logger")
        Logger.geometry("360x40")
        HowManyLabel = Label(Logger, text= "How many hours did you work?")
        HowManyLabel.grid(row=0, column=2)
        HowManyEntry = Entry(Logger)
        HowManyEntry.grid(row=0,column=3)

        def SqlStuff():

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
            """, (today, HowManyEntry.get()))

            connection.commit()
            connection.close()
            Logger.destroy()
        SQLStuffButton = Button(Logger, text="Confirm", command=SqlStuff)
        SQLStuffButton.grid(row=0,column=4)
    elif type.get() == "Custom":
        Custom=tk.Tk()
        Custom.title("Custom")
        Custom.geometry("960x540")

    elif type.get() == "Viewer":
        Viewer=tk.Tk()
        Viewer.title("Viewer")
        Viewer.geometry("960x540")

type = StringVar()
type.set("Logger")

InitialOption = OptionMenu(window, type, "Logger", "Custom", "Viewer")
InitialOption.grid(row=0, column=0)

InitialOptionButton = Button(window, text="Confirm Choice", command=Selection)
InitialOptionButton.grid(row=0, column=1)



window.mainloop()
