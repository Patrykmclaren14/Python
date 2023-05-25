from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('first window')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons


def opening():
    global img
    top = Toplevel()
    top.tk.call('wm', 'iconphoto', top._w, img)
    top.title('second window')

    label = Label(top, text="Hello world").pack()
    myImg = ImageTk.PhotoImage(Image.open('icon.png'))
    label = Label(top, image=myImg).pack()
    button2 = Button(top, text="Quit from the second window",
                     command=top.destroy).pack()


button = Button(root, text="Open second window", command=opening).pack()


mainloop()
