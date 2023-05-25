from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('test')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons


Modes = [
    ("Pepperoni", "Pepperoni"),
    ("Capriociosa", "Capriociosa"),
    ("Pinapple", "Pinapple"),
    ("Onion", "Onion"),
    ("Diabolo", "Diabolo")
]

pizza = StringVar()
pizza.set("Peperoni")

for text, mode in Modes:
    Radiobutton(root, text=text, variable=pizza,  value=mode,
                ).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r,  value=1,
#            command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r,  value=2,
#            command=lambda: clicked(r.get())).pack()


myButton = Button(root, text="Click me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
