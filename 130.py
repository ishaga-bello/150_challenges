# Alter program 129 to add a third button that will save the list to a .csv file. The code
# tmp_list = num_list.get(0,END) can be used to save the contents of a list box as a tuple called tmp_list .

from tkinter import *
import csv

def call():
    num = textBox1.get()
    if num.isdigit():
        nameList.insert(END, num)
        textBox1.delete(0, END)
        textBox1.focus()
    else:
        textBox1.delete(0, END)
        textBox1.focus()
    textBox1.focus()
    
def save():
    file = open('names.csv', 'w')
    names = nameList.get(0, END) 
    x = 0
    for row in names:
        rec = names[x] + '\n'
        file.write(str(rec))
        x += 1
    file.close

def reset():
    nameList.delete(0, END)
    textBox1.focus()

window = Tk()
window.title('Number saver')
window.geometry('300x300')

label1 = Label(text= 'Enter a number:')
label1.place(x=30, y=20)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Add', command = call)
button.place(x=30, y=60, width=70, height=25)

button1 = Button(text = 'Reset', command= reset)
button1.place(x=120, y=60, width=70, height=25)

button2 = Button(text = 'Save', command= save)
button2.place(x=210, y=60, width=70, height=25)

nameList = Listbox()
nameList.place(x=50, y=100)


window.mainloop()