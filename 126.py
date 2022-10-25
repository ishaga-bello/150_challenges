from tkinter import *

def call():
    num = 0
    next = enter.get()
    out = Message(text = 0)
    next = int(next)
    num += next
    out['text'] = num
    out.place(x=125, y=80)

window = Tk()
window.title('work')
window.geometry('250x200')
msg1 = Label(text = 'Enter number')
msg1.place(x=10, y=20)
enter = Entry(text = 0)
enter.place(x=125, y=20, width=120)
button1 = Button(text = 'Add', command = call)
button1.place(x=75, y=50)
window.mainloop()