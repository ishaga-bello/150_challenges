# Create a new program that will generate two random whole numbers between 10 and 50. It should ask the
# user to add the numbers together and ype in the answer. If they get the question correct, display a suitable image such as a tick; if they get the
# answer wrong, display another suitable image such as a cross. Theyshould click on a Next button to get
# another question.

from tkinter import *
    
def action():
    sel = selectColour.get()
    window.configure(background = sel)

window = Tk()
window.title('work')
window.geometry('200x200')
window['bg'] = 'grey'

selectColour = StringVar(window)
selectColour.set('Grey')

colourList = OptionMenu(window, selectColour, 'Grey', 'blue', 'Green', 'Red', 'Yellow')
colourList.place(x=50, y=30)

click = Button(text = 'Click me', command = action)
click.place(x =50, y=150, width=60, height=30)

window.mainloop()