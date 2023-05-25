from optparse import Option
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('first window')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons
root.geometry('400x400')


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

mainloop()
