# 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. Using these figures, make a program
# that will allow the user to convert between miles and kilometres.

from tkinter import *

def toKm():
    mile = textBox1.get()
    textBox1.delete(0,END)
    textBox1.focus()
    mile = float(mile)
    km = mile * 0.6214
    km = '%.2f' %km
    textBox2['text'] = km
    
def toMile():
    km = textBox1.get()
    textBox1.delete(0,END)
    textBox1.focus()
    km = float(km)
    mile = km * 1.6093
    mile = '%.2f' %mile
    textBox2['text'] = mile
    textBox1.focus()

def reset():
    textBox2['text'] = 0
    textBox1.delete(0, END)
    textBox1.focus()

window = Tk()
window.title('converter')
window.geometry('300x200')

label1 = Label(text= 'Enter a number:')
label1.place(x=30, y=20)

textBox1 = Entry(text = 0)
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Convert to KM', command = toKm)
button.place(x=30, y=60, width=120, height=25)

button1 = Button(text = 'Convert to Mile', command= toMile)
button1.place(x=150, y=60, width=120, height=25)

button2 = Button(text = 'Reset', command= reset)
button2.place(x=80, y=100, width=120, height=25)

label2 = Label(text= 'value:')
label2.place(x=80, y=140)

textBox2 = Message(text = 0)
textBox2['relief'] = 'solid'
textBox2.place(x=150, y=140, width=125, height=25)

window.mainloop()