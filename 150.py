import sqlite3
from tkinter import *

def addArtist():
    aID = box1.get()
    Name = box2.get()
    Add = box3.get()
    town = box4.get()
    count = box5.get()
    post = box6.get()
    cursor.execute("""INSERT INTO ArtistContact(artistid,name,address,)""")

with sqlite3.connect('Art Gallery.db') as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS ArtistContact(
    ArtistID integer PRIMARY KEY,
    Name text NOT NULL,
    Address text NOT NULL,
    Town text NOT NULL,
    County text NOT NULL,
    Postcode text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS PieceOfArt(
    PieceID integer PRIMARY KEY,
    ArtistID integer NOT NULL,
    Title text NOT NULL, 
    Medium text NOT NULL,
    Price integer NOT NULL);""")

window = Tk()
window.title('Art Gallery Management System')
window.geometry('600x500')

label = Label(text = 'Artist Contact Details')
label.place(x=20, y=10)

lb1 = Label(text = 'ArtistID')
lb1.place(x=25 , y=40)

box1= Entry(text = '')
box1.place(x=25 , y=60, width= 75)

lb1 = Label(text = 'Name')
lb1.place(x=125 , y=40)

box2= Entry(text = '')
box2.place(x=125 , y=60, width= 75)

lb1 = Label(text = 'Address')
lb1.place(x=225 , y=40)

box3= Entry(text = '')
box3.place(x=225 , y=60, width= 75)

lb1 = Label(text = 'Town')
lb1.place(x=325 , y=40)

box4= Entry(text = '')
box4.place(x=325 , y=60, width= 75)

lb1 = Label(text = 'County')
lb1.place(x=425 , y=40)

box5= Entry(text = '')
box5.place(x=425 , y=60, width= 75)

lb1 = Label(text = 'Postcode')
lb1.place(x=525 , y=40)

box6= Entry(text = '')
box6.place(x=525 , y=60, width= 75)

b1 = Button(text='Add')
b1.place(x=125, y=90)

b2 = Button(text='Clear')
b2.place(x=325, y=90)

label = Label(text = 'Piece of Art')
label.place(x=20, y=120)

lb1 = Label(text = 'pieceID')
lb1.place(x=40 , y=140)

box7= Entry(text = '')
box7.place(x=40 , y=160, width= 80)

lb1 = Label(text = 'ArtistID')
lb1.place(x=140 , y=140)

box8= Entry(text = '')
box8.place(x=140 , y=160, width= 80)

lb1 = Label(text = 'Title')
lb1.place(x=240 , y=140)

box9= Entry(text = '')
box9.place(x=240 , y=160, width= 80)

lb1 = Label(text = 'Medium')
lb1.place(x=340 , y=140)

box10= Entry(text = '')
box10.place(x=340 , y=160, width= 80)

lb1 = Label(text = 'Price')
lb1.place(x=440 , y=140)

box11= Entry(text = '')
box11.place(x=440 , y=160, width= 80)

b1 = Button(text='Add')
b1.place(x=125, y=190)

b2 = Button(text='Clear')
b2.place(x=325, y=190)

label = Label(text='Enter Id of sold piece of art: ')
label.place(x=60, y=230)

box12 = Entry(text ='')
box12.place(x=260, y=230)

b1 = Button(text = 'Sold')
b1.place(x=450, y=230)

lb1 = Label(text = 'Artist')
lb1.place(x=20 , y=280)

box11= Entry(text = '')
box11.place(x=80 , y=280, width= 100)

lb1 = Label(text = 'Medium')
lb1.place(x=200 , y=280)

box11= Entry(text = '')
box11.place(x=280 , y=280, width= 100)

lb1 = Label(text = 'Price')
lb1.place(x=400 , y=280)

box11= Entry(text = '')
box11.place(x=450 , y=280, width= 100)

b1 = Button(text='Search')
b1.place(x=125, y=310)

b2 = Button(text='Clear')
b2.place(x=325, y=310)

table = Listbox()
table.place(x=100, y=350, width=400)

window.mainloop()