# Create a new program that will generate two random whole numbers between 10 and 50. It should ask the
# user to add the numbers together and ype in the answer. If they get the question correct, display a suitable image such as a tick; if they get the
# answer wrong, display another suitable image such as a cross. Theyshould click on a Next button to get
# another question.

from tkinter import *
    
def action():
    name = textBox1.get()
    name1 = 'Hello' + ' ' + name + '\n'
    msg = str(name1)
    # textBox2['text'] = msg
    button = Button(text = 'Check', command = action)
    button.place(x=200, y=150, width=120, height=25)
    # logo = PhotoImage(file  = 'img.GIF')
    # logoImg = Label(image= logo)
    # logoImg.place(x=100, y=20, width=200, height=150)

window = Tk()
window.title('work')
window.geometry('500x400')
window['bg'] = 'grey'


label1 = Label(text= 'Number 1:')
label1.place(x=50, y=51)
label1['bg'] = 'grey'
label1['fg'] = 'black'

textBox1 = Message(text = '')
textBox1.place(x= 120, y=50, width=100, height=25)

label1 = Label(text= 'Number 2:')
label1.place(x=280, y=51)
label1['bg'] = 'grey'
label1['fg'] = 'black'

textBox1 = Message(text = '')
textBox1.place(x= 350, y=50, width=100, height=25)

textBox1 = Entry(text = '')
textBox1.place(x= 150, y=100, width=200, height=25)
textBox1['justify'] = 'center'
textBox1.focus()

button = Button(text = 'Check', command = action)
button.place(x=200, y=150, width=120, height=25)

window.mainloop()