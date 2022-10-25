import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT * FROM Books""")
for i in cursor.fetchall():
    print(i)

pob = input('Enter a year to search: ')
cursor.execute("""SELECT books.title,books.author,books.datepublished  FROM books 
WHERE datepublished>? 
ORDER BY datepublished""",[pob])
for i in cursor.fetchall():
    print(i)

db.close()