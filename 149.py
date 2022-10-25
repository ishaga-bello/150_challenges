from tkinter import *

def view():
    num = box1.get()
    num = int(num)
    for i in range(1,13):
        ans = num * i
        show = str(num) + '*' + str(i) + '=' + str(ans)
        show = str(show)
        table.insert(END, show)
        box1.delete(0, END)


def clear():
    table.delete(0, END)
    box1.focus()
    box1['justify'] = 'center'

window = Tk()
window.title('Time Table')
window.geometry('400x300')

label = Label(text='Enter a number:')
label.place(x=10,y=20)

box1 = Entry(text='')
box1.place(x=120, y=20, width=110, height=25)
box1.focus()
box1['justify'] = 'center'

table = Listbox()
table.place(x=120, y=60, width=110, height=200)

button1 = Button(text = 'View times Table', command=view)
button1.place(x=240, y=20)

button2 = Button(text = 'Clear', command=clear)
button2.place(x=240, y=60, width=140)


window.mainloop()