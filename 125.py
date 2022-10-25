from tkinter import *
import random

def call():
    out = Message(text =0)
    text = random.randint(1,6)
    out['text'] = text
    out.place(x=120, y=120)
    window['bg'] = 'yellow'
    out['fg'] = 'red'

window = Tk()
window.title('work')
window.geometry('250x200')
button = Button(text = 'Roll', command = call)
button.place(x=100, y=60)
window.mainloop()