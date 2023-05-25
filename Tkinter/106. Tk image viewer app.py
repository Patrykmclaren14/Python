from email.mime import image
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('test')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons

photo1 = ImageTk.PhotoImage(Image.open('photo1.jpg'))
photo2 = ImageTk.PhotoImage(Image.open('photo2.jpg'))
photo3 = ImageTk.PhotoImage(Image.open('photo3.jpg'))
photo4 = ImageTk.PhotoImage(Image.open('photo4.jfif'))
photo5 = ImageTk.PhotoImage(Image.open('photo5.jpg'))

imageList = [photo1, photo2, photo3, photo4, photo5]

status = Label(root, text="image 1 of " +
               str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)


myLabel = Label(image=photo1)
myLabel.grid(row=0, column=0, columnspan=3,)


def back(imageNumber):
    global myLabel
    global ButtonForward
    global ButtonBack

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber-1])
    ButtonForward = Button(
        root, text=">>", command=lambda: forward(imageNumber+1))
    ButtonBack = Button(root, text="<<", command=lambda: back(imageNumber-1))
    if imageNumber == 1:
        ButtonBack = Button(root, text="<<", state=DISABLED)
    myLabel.grid(row=0, column=0, columnspan=3)
    ButtonBack.grid(row=1, column=0)
    ButtonForward.grid(row=1, column=2)
    status = Label(root, text="image " + str(imageNumber) + " of " +
                   str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def forward(imageNumber):
    global myLabel
    global ButtonForward
    global ButtonBack

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber-1])
    ButtonForward = Button(
        root, text=">>", command=lambda: forward(imageNumber+1))
    ButtonBack = Button(root, text="<<", command=lambda: back(imageNumber-1))
    if imageNumber == 5:
        ButtonForward = Button(root, text=">>", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    ButtonBack.grid(row=1, column=0)
    ButtonForward.grid(row=1, column=2)
    status = Label(root, text="image " + str(imageNumber) + " of " +
                   str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


ButtonQuit = Button(root, text="Exit program", command=root.quit)
ButtonBack = Button(root, text="<<", command=back, state=DISABLED)
ButtonForward = Button(root, text=">>", command=lambda: forward(2))

ButtonQuit.grid(row=1, column=1)
ButtonBack.grid(row=1, column=0)
ButtonForward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
