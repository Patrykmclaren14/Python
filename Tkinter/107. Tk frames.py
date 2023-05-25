from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('test')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons

frame = LabelFrame(root, text='This is my frame..', padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b.grid(row=0, column=0)

b2 = Button(frame, text="or here")
b2.grid(row=1, column=1)

root.mainloop()
