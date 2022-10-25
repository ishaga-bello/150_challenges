# Using the .csv file you created for the last challenge, create a program that will allow
# people to add names and ages to the list and create a button that will display the
# contents of the .csv file by importing it to a list box.

from tkinter import *
import csv
    
def action():
    name = textBox1.get()
    name1 = 'Hello' + ' ' + name + '\n'
    msg = str(name1)
    textBox2['text'] = msg
    

window = Tk()
window.title('work')
window.geometry('500x400')
window['bg'] = 'black'

logo = PhotoImage(file  = 'img.GIF')
logoImg = Label(image= logo)
logoImg.place(x=100, y=20, width=200, height=150)

label1 = Label(text= 'Enter your name:')
label1.place(x=80, y=250)
label1['bg'] = 'black'
label1['fg'] = 'white'

textBox1 = Entry(text = '')
textBox1.place(x= 200, y=250, width=220, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Press Me', command = action)
button.place(x=80, y=300, width=120, height=25)

textBox2 = Message(text = '')
textBox2.place(x=205, y=300, width=220, height=25)
textBox2['bg'] = 'white'
textBox2['fg'] = 'black'

window.mainloop()