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
                day TEXT,
                hours INT
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
        Custom.geometry("300x150")
        todayLabel = Label(Custom, text="What date did you work YY/MM/DD")
        todayEntry = Entry(Custom)
        todayLabel.pack()
        todayEntry.pack()

        hoursLabel = Label(Custom, text="How many hours did you work?")
        hours = Entry(Custom)
        hoursLabel.pack()
        hours.pack()


        def CustonInput():
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
            """, (todayEntry.get(), hours.get()))

            connection.commit()
            connection.close()
        Confirm = Button(Custom, text="Confirm", command=CustonInput)
        Confirm.pack()


    elif type.get() == "Viewer":
        Viewer=tk.Tk()
        Viewer.title("Viewer")
        Viewer.geometry("960x540")
        connection = sql.connect("hours.db")

        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM hours
        ORDER BY day ASC;
        """)

        rows = cursor.fetchall()

        connection.commit()
        connection.close()

        WarningLabel = Label(Viewer, text="Disclaimer: I recommend using a database viewer like DB Browser")
        WarningLabel.pack()
        ViewerLabel = Label(Viewer, text=rows, wraplength=960)
        ViewerLabel.pack()

        def refresh():
            Viewer.destroy()

            ViewerR = tk.Tk()
            ViewerR.title("Viewer")
            ViewerR.geometry("960x540")
            connection = sql.connect("hours.db")

            cursor = connection.cursor()

            cursor.execute("""
                    SELECT * FROM hours
                    ORDER BY day ASC;
                    """)

            rows = cursor.fetchall()

            connection.commit()
            connection.close()

            ViewerLabel = Label(ViewerR, text=rows)
            ViewerLabel.pack()

            ViewerButton = Button(ViewerR, text="refresh", command=refresh)
            ViewerButton.pack()




        ViewerButton = Button(Viewer, text="refresh",command=refresh)
        ViewerButton.pack()


    elif type.get() == "Delete":

        Delete = tk.Tk()
        Delete.title("Delete")
        Delete.geometry("400x100")
        dateLabel = Label(Delete, text= "What date was the shift? YY/MM/DD")
        dateEntry = Entry(Delete)
        dateLabel.pack()
        dateEntry.pack()

        def SqlStuffDelete():
            connection = sql.connect("hours.db")
            cursor = connection.cursor()

            cursor.execute("""DELETE FROM hours
                                WHERE day = ?""", (dateEntry.get(),))

            connection.commit()
            connection.close()


        dateButton = Button(Delete,text="Confirm", command=SqlStuffDelete)
        dateButton.pack()




type = StringVar()
type.set("Logger")

InitialOption = OptionMenu(window, type, "Logger", "Custom", "Viewer", "Delete")
InitialOption.grid(row=0, column=0)

InitialOptionButton = Button(window, text="Confirm Choice", command=Selection)
InitialOptionButton.grid(row=0, column=1)



window.mainloop()
