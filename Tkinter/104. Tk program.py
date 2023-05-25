from tkinter import *
from math import sqrt

root = Tk()
root.title('calculator')

e = Entry(root, width=55, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

e.insert(0, "")


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    firstNumber = e.get()
    global f_num
    global math
    math = 'addiction'
    f_num = int(firstNumber)
    e.delete(0, END)


def button_sub():
    firstNumber = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(firstNumber)
    e.delete(0, END)


def button_multiplication():
    firstNumber = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(firstNumber)
    e.delete(0, END)


def button_division():
    firstNumber = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(firstNumber)
    e.delete(0, END)


def button_exp():
    firstNumber = e.get()
    global f_num
    global math
    math = 'exponentiation'
    f_num = int(firstNumber)
    e.delete(0, END)


def button_square():
    firstNumber = e.get()
    global f_num
    global math
    math = 'square root'
    f_num = int(firstNumber)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addiction':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))
    if math == 'exponentiation':
        e.insert(0, f_num ** int(second_number))
    if math == 'square root':
        e.insert(0, sqrt(f_num))


def button_clear():
    e.delete(0, END)


button1 = Button(root, text='1', padx=40, pady=20,
                 command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=20,
                 command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=20,
                 command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=20,
                 command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=20,
                 command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=20,
                 command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=20,
                 command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=20,
                 command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=20,
                 command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=20,
                 command=lambda: button_click(0))
buttonAdd = Button(root, text='+', padx=40, pady=20,
                   command=button_add)
buttonEqual = Button(root, text='=', padx=88, pady=20,
                     command=button_equal)
buttonClear = Button(root, text='Clear', padx=79, pady=20,
                     command=button_clear)
buttonSub = Button(root, text='-', padx=40, pady=20,
                   command=button_sub)
buttonMulti = Button(root, text='x', padx=40, pady=20,
                     command=button_multiplication)
buttonDiv = Button(root, text='/', padx=40, pady=20,
                   command=button_division)
buttonExp = Button(root, text='^', padx=40, pady=20,
                   command=button_exp)
buttonSquare = Button(root, text='√', padx=40, pady=20,
                      command=button_square)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=4, column=1, columnspan=2)
buttonClear.grid(row=5, column=1, columnspan=2)

buttonSub.grid(row=1, column=3)
buttonMulti.grid(row=2, column=3)
buttonDiv.grid(row=3, column=3)
buttonExp.grid(row=4, column=3)
buttonSquare.grid(row=5, column=3)


root.mainloop()
