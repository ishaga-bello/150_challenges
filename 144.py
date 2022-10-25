import sqlite3

file = open('BookInfo.txt', 'w')

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT Name FROM Authors""")
for i in cursor.fetchall():
    print(i)

num = input('Enter an author name to search: ')
cursor.execute("""SELECT * FROM books 
WHERE author=? 
ORDER BY id""",[num])
for i in cursor.fetchall():
    rec = str(i[0]) + '-' + i[1] + '-' + i[2] + '-' + str(i[3]) + '\n'
    file.write(rec)

file.close
db.close()