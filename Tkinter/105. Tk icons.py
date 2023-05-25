from email.mime import image
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('test')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons

photo = ImageTk.PhotoImage(Image.open('icon.png'))
myLabel = Label(image=photo)
myLabel.pack()

# button that exit program
Button_quit = Button(root, text="Exit program", command=root.quit)
Button_quit.pack()

root.mainloop()
