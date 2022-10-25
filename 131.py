# Create a program that will allow the user to create a new .csv file. It should
# ask them to enter the name and age of a person and then allow them to add
# this to the end of the file they have just created.

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

window = Tk()
window.title('Info registration')
window.geometry('300x200')

label = Label(text= 'Enter a name:')
label.place(x=30, y=20)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()


label = Label(text= 'Enter number:')
label.place(x=30, y=60)

textBox2 = Entry(text = '')
textBox2.place(x= 150, y=60, width=120, height=25)
textBox2['justify'] = 'center'
textBox2.focus()

button = Button(text = 'Save', command = save)
button.place(x=100, y=100, width=70, height=25)


window.mainloop()