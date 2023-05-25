from cProfile import label
from fileinput import filename
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('first window')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons

root.filename = filedialog.askopenfile(
    initialdir=r"C:\Users\michalmas77757\Desktop\wszystko\pliki python\kurs python", title='select your files', filetypes=(('jpg files', "*.jpg"), ("all files", "*.*")))
myLabel = Label(root, text=root.filename).pack()
myImage = ImageTk.PhotoImage(Image.open(root.filename))


root.mainloop()
