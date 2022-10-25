# Using the .csv file you created for the last challenge, create a program that will allow
# people to add names and ages to the list and create a button that will display the
# contents of the .csv file by importing it to a list box.

from tkinter import *
import csv
    
def save():
    name = textBox1.get()
    number = textBox2.get()
    info = name + ',' + number + '\n'
    file = open('names.csv', 'a')
    file.write(str(info))
    file.close
    textBox1.delete(0, END)
    textBox2.delete(0, END)

def view():
    file = list(csv.reader(open('names.csv')))
    tmp = []
    x = 0
    for row in file:
        tmp.append(row)
        x += 1
    
    for i in tmp:
        info.insert(0, i)

def reset():
    info.delete(0, END)
    textBox1.focus()

window = Tk()
window.title('Info registration')
window.geometry('300x400')

label = Label(text= 'Enter a name:')
label.place(x=30, y=20)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()


label = Label(text= 'Enter age:')
label.place(x=30, y=60)

textBox2 = Entry(text = '')
textBox2.place(x= 150, y=60, width=120, height=25)
textBox2['justify'] = 'center'
textBox2.focus()

button = Button(text = 'Save', command = save)
button.place(x=50, y=100, width=70, height=25)

button = Button(text = 'View Names', command = view)
button.place(x=150, y=100, width=100, height=25)

button = Button(text = 'Clear', command = reset)
button.place(x=110, y=130, width=70, height=25)

info = Listbox()
info.place(x=50, y=170)


window.mainloop()