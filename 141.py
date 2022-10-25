import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    Name text NOT NULL,
    PlaceOfBirth text NOT NULL);""")

for i in range(0,4):
    name = input('Insert name: ')
    pob = input('Insert pob: ')
    cursor.execute("""INSERT INTO Authors(Name,PlaceOfBirth)
    VALUES(?,?)""",(name,pob))
    db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
    ID integer PRIMARY KEY,
    Title text NOT NULL,
    Author text NOT NULL,
    DatePublished integer NOT NULL);""")

for i in range(1,13):
    newID = i
    newName = input('Enter Title: ')
    newDept = input('Enter Author: ')
    newSalary = input('Enter Date Published: ')
    cursor.execute('''INSERT INTO Books(id,title,author,datepublished)
    VALUES(?,?,?,?)''',(newID,newName,newDept,newSalary))
    db.commit()

db.close()