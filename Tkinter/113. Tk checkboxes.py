from msilib.schema import CheckBox
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('first window')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons
root.geometry('400x400')


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text='Check this box, I dare you!',
                variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myButton = Button(root, text="Show selection", command=show).pack()
mainloop()
