from tkinter import *

def call():
    name = textBox1.get()
    msg = str('Hello' + name)
    textBox2['bg'] = 'Yellow'
    textBox2['fg'] = 'blue'
    textBox2['text'] = msg
    

window = Tk()
window.title('work')
window.geometry('300x200')

label1 = Label(text= 'Enter your name:')
label1.place(x=30, y=20)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Start', command = call)
button.place(x=80, y=120, width=120, height=25)

textBox2 = Message(text = '')
textBox2.place(x=50, y=100, width=200, height=25)
textBox2['bg'] = 'white'
textBox2['fg'] = 'black'

window.mainloop()