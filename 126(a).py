from tkinter import *

def call():
    num = textBox1.get()
    num = int(num)
    answer = textBox2['text']
    answer =int(answer)
    total = num + answer
    textBox2['text'] = total
    
def reset():
    total = 0
    textBox2['text'] = 0
    textBox1.delete(0, END)
    textBox1.focus()

window = Tk()
window.title('work')
window.geometry('300x200')

label1 = Label(text= 'Enter a number:')
label1.place(x=30, y=20)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=20, width=120, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Add', command = call)
button.place(x=30, y=60, width=120, height=25)

button1 = Button(text = 'Reset', command= reset)
button1.place(x=150, y=60, width=120, height=25)

label1 = Label(text= 'Answer =')
label1.place(x=50, y=100)

textBox2 = Message(text = 0)
textBox2.place(x=150, y=100, width=100, height=25)
textBox2['bg'] = 'white'
textBox2['fg'] = 'black'

window.mainloop()