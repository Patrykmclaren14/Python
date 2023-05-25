import os
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

import comm
from pyparsing import col

window = Tk()
window.title('Text program')
img = PhotoImage(file='sun.png')
window.tk.call('wm', 'iconphoto', window._w, img)
window.geometry('500x500')


def change_color():
    color = colorchooser.askcolor(title="pick a calor")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt", file=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, 'r')
        text_area.insert(1.0, file.read())
    except Exception:
        print("could't read file")


def save_file():
    file = filedialog.asksaveasfile(initialfile='untitled.txt', defaultextension='.txt', filetypes=[
                                    ('All Files', '*.*'), ('Text Documents', '.txt')])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')

            file.write(text_area.get(1.0, END))
        except Exception:
            print("Couldn't your file")
        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program",
             "This is a program written by Patryk Wierzbowski gowno fc")


def quit():
    window.destroy()


font_name = StringVar(window)
font_name.set('aerial')

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
# gdy zmieniamy rozmiary okna wartosc w programie nie jest ukryta tylko sie zweza
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text='color', command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(),
                      command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100,
                   textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


mainloop()
