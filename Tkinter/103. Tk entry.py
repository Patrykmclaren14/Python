from tkinter import *

root = Tk()

e = Entry(width=40, )
e.pack()


def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


myButton = Button(root, text="Clcik me", padx=50, pady=50,
                  command=myClick, fg="white", bg="black")  # state = disable (state of the button) #fg = foreground color, bg = background color
myButton.pack()


root.mainloop()
