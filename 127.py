from tkinter import *

def call():
    name = textBox1.get()
    nameList.insert(END, name)
    textBox1.delete(0,END)
    textBox1.focus()
    
def reset():
    nameList.delete(0, END)
    textBox1.focus()

window = Tk()
window.title('Name Adder')
window.geometry('300x300')

label1 = Label(text= 'Enter a name:')
label1.place(x=30, y=20)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Add', command = call)
button.place(x=30, y=60, width=120, height=25)

button1 = Button(text = 'Reset', command= reset)
button1.place(x=150, y=60, width=120, height=25)

nameList = Listbox()
nameList.place(x=50, y=100)


window.mainloop()