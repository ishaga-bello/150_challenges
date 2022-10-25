from tkinter import *
import sqlite3


def add():
    name = box1.get()
    grade = box2.get()
    cursor.execute("""INSERT INTO Score(Name,Grade)
    VALUES(?,?)""",(name,grade))
    db.commit()

def clear():
    box1.delete(0, END)
    box2.delete(0, END)
    box1.focus()

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Score(
    Name text NOT NULL,
    Grade integer NOT NULL);""")

window = Tk()
window.title('TestScores')
window.geometry('400x200')

label = Label(text= 'Enter student\'s name:')
label.place(x=30,y=30)

box1 = Entry(text='')
box1.place(x=200, y=30)
box1.focus()
box1['justify'] = 'center'

label = Label(text= 'Enter student\'s grade:')
label.place(x=30,y=80)

box2 = Entry(text='')
box2.place(x=200, y=80)
box2.focus()
box2['justify'] = 'center'

b1 = Button(text= 'Add', command=add)
b1.place(x=120, y=120, width=75)

b2 = Button(text= 'Clear', command=clear)
b2.place(x=230, y=120, width=75)

window.mainloop()
db.close()