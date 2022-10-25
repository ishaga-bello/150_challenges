from tkinter import *

def call():
    num = entry.get()
    out = Message(text =0)
    text = 'hello' + ' ' + num
    out['text'] = text
    out.place(x=80, y=90)
    window['bg'] = 'yellow'
    window['fg'] = 'red'

window = Tk()
window.title('work')
window.geometry('250x200')
label = Label(text = 'Enter your name')
label.place(x=10, y=20)
entry = Entry(text = 0)
entry.place(x=135, y=20, width=110)
button = Button(text = 'Start', command = call)
button.place(x=100, y=60)
window.mainloop()