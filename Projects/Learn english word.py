from tkinter import *

root = Tk()
root.title('English word application')
root.geometry("500x500")
english_word = ['cat', 'dog', 'table', 'chair', 'book', 'pen']
polish_word = ["kot", "pies", "stół", "krzesło", "książka", "długopis"]


def Check():
    if text.get() == mylabel1.cget('text'):
        mylabel1.grid(column=1)
    if text.get() == mylabel2.cget('text'):
        mylabel2.grid(column=1)
    if text.get() == mylabel3.cget('text'):
        mylabel3.grid(column=1)
    if text.get() == mylabel4.cget('text'):
        mylabel4.grid(column=1)
    if text.get() == mylabel5.cget('text'):
        mylabel5.grid(column=1)
    if text.get() == mylabel6.cget('text'):
        mylabel6.grid(column=1)


mylabel1 = Label(root, text=english_word[0])
mylabel2 = Label(root, text=english_word[1])
mylabel3 = Label(root, text=english_word[2])
mylabel4 = Label(root, text=english_word[3])
mylabel5 = Label(root, text=english_word[4])
mylabel6 = Label(root, text=english_word[5])


text = Entry(root)
text.grid(column=2, row=0)

good = Label(root, text='dobrze')

myButton = Button(root, text='Check', command=Check)
myButton.grid(column=3, row=0)

mainloop()
