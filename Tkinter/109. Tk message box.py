from email import message
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('test')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons


# show - info, warning, error, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my popup", "Hello world")
    if response == 1:
        Label(root, text="You click yes").pack()
    if response == 0:
        Label(root, text="You click no").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()
