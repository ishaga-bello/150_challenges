import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT * FROM Authors""")
for i in cursor.fetchall():
    print(i)

pob = input('Enter a place of birth to search: ')
cursor.execute("""SELECT books.title,books.author,books.datepublished,authors.placeofbirth  FROM authors,books 
WHERE books.author=authors.name AND placeofbirth=?""",[pob])
for i in cursor.fetchall():
    print(i)

db.close()