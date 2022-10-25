import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
    id integer PRIMARY KEY,
    FirstName text NOT NULL,
    Surname text NOT NULL,
    PhoneNumber integer);"""
)

for i in range(1,6):
    newId = i
    name = input('ENter name: ')
    sur = input('Enter surname: ')
    tel = input('ENter Telephone: ')
    cursor.execute("""INSERT INTO Names(id,FirstName,Surname,PhoneNumber)
    VALUES(?,?,?,?)""",(newId,name,sur,tel))
    db.commit()