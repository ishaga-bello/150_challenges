import sqlite3 

with sqlite3.connect('Company.db') as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Departments(
    Dept text NOT NULL,
    Manager text NOT NULL)''')

for i in range(0,4):
    newDept = input('Enter department: ')
    newName = input('Enter name: ')
    cursor.execute('''INSERT INTO Departments(Dept,Manager)
    VALUES(?,?)''',(newDept,newName))
    db.commit()

db.close