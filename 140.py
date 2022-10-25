import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def view():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def insert():
    newId = input("Enter ID: ")
    name = input('Enter name: ')
    sur = input('Enter surname: ')
    tel = input('Enter Telephone: ')
    cursor.execute("""INSERT INTO Names(id,FirstName,Surname,PhoneNumber)
    VALUES(?,?,?,?)""",(newId,name,sur,tel))
    db.commit()

def search():
    search= input('ENter Surname to search: ')
    cursor.execute("SELECT * FROM Names WHERE surname=?",[search])
    for x in cursor.fetchall():
        print(x)

def remove():
    rem = input('Enter id to delete: ')
    cursor.execute("DELETE FROM Names WHERE id=?", [rem])

def main():
    select = 0
    while select != 5:
        print('Main Menu')
        print()
        print('1) View phone book')
        print('2) Add to phone book')
        print('3) Search for surname')
        print('4) Delete person from phone book')
        print('5) Quit')
        print()
        select = int(input('Enter your selection: '))
        if select == 1 :
            view()
        elif select == 2:
            insert()
        elif select == 3:
            search()
        elif select == 4:
            remove()
        else:
            select = int(input('Select between 1 and 5: '))

main()

db.close()