import sqlite3 

with sqlite3.connect('Company.db') as db:
    cursor = db.cursor()

# for i in range(2,11):
#     newID = i
#     newName = input('Enter name: ')
#     newDept = input('Enter department: ')
#     newSalary = input('Enter salary: ')
#     cursor.execute('''INSERT INTO employees(id,name,dept,salary)
#     VALUES(?,?,?,?)''',(newID,newName,newDept,newSalary))
#     db.commit()

# cursor.execute("""SELECT employees.id,employees.name,employees.salary,Departments.manager
# FROM employees,Departments""")
# for i in cursor.fetchall():
#     print(i)


cursor.execute("DELETE employees WHERE id=1")
# db.commit()
db.close