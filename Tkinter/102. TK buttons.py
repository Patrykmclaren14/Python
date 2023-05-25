from faulthandler import disable
from tkinter import *

from numpy import pad

root = Tk()


def myClick():
    myLabel = Label(root, text="Look I click the button")
    myLabel.pack()


myButton = Button(root, text="Clcik me", padx=50, pady=50,
                  command=myClick, fg="white", bg="black")  # state = disable (state of the button) #fg = foreground color, bg = background color
myButton.pack()


root.mainloop()
