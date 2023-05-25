from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('first window')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons
root.geometry('400x400')


def slide():
    myLabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))


vertical = Scale(root, from_=0, to=200)
vertical.pack()


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


def slide():
    myLabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x400')


myButton = Button(root, text="Click me", command=slide).pack()

mainloop()
