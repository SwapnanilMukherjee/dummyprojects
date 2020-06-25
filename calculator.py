from math import cos, log, radians, sin, sqrt, tan
from tkinter import *

root = Tk()
root.title('Simple Calculator ')

first = float()
second = float()
f = int()

InputBox = Entry(root, width = 40, borderwidth = 5)
InputBox.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)


def b_click(number):
    current = InputBox.get()
    InputBox.delete(0, END)
    InputBox.insert(0, str(current) + str(number))


def add():
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 1


def sub():
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 2


def product():
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 3


def division():
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 4


def mod():
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 5


def equal():
    global second
    second = float(InputBox.get())
    global first

    if f == 1:
        result = first + second

    elif f == 2:
        result = first - second

    elif f == 3:
        result = first * second

    elif f == 4:
        result = first / second

    elif f == 5:
        result = first % second
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def sinf():
    current = float(InputBox.get())
    result = sin(radians(current))
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def cosf():
    current = float(InputBox.get())
    result = cos(radians(current))
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def tanf():
    if InputBox.get() == '90':
        InputBox.delete(0, END)
        InputBox.insert(0, "Invalid Input")
    else:
        current = float(InputBox.get())
        result = tan(radians(current))
        InputBox.delete(0, END)
        InputBox.insert(0, result)


def logf():
    current = float(InputBox.get())
    result = log(current, 10)
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def sqrtf():
    current = float(InputBox.get())
    result = sqrt(current)
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def delete():
    current = str(InputBox.get())
    length = len(current)
    result = current[:length - 1]
    InputBox.delete(0, END)
    InputBox.insert(0, str(result))


def clear():
    InputBox.delete(0, END)


# creating buttons

b1 = Button(root, text = "1", padx = 30, pady = 10, command = lambda : b_click(1))
b2 = Button(root, text = "2", padx = 30, pady = 10, command = lambda : b_click(2))
b3 = Button(root, text = "3", padx = 30, pady = 10, command = lambda : b_click(3))
b4 = Button(root, text = "4", padx = 30, pady = 10, command = lambda : b_click(4))
b5 = Button(root, text = "5", padx = 30, pady = 10, command = lambda : b_click(5))
b6 = Button(root, text = "6", padx = 30, pady = 10, command = lambda : b_click(6))
b7 = Button(root, text = "7", padx = 30, pady = 10, command = lambda : b_click(7))
b8 = Button(root, text = "8", padx = 30, pady = 10, command = lambda : b_click(8))
b9 = Button(root, text = "9", padx = 30, pady = 10, command = lambda : b_click(9))
b0 = Button(root, text = "0", padx = 30, pady = 10, command = lambda : b_click(0))
b_point = Button(root, text = ".", padx = 31.4, pady = 10, command = lambda:b_click('.'))

b_add = Button(root, text = "+", padx = 29, pady = 10, command = add)
b_sub = Button(root, text = "-", padx = 30.4, pady = 10, command = sub)
b_prod = Button(root, text = "*", padx = 31, pady = 10, command = product)
b_div = Button(root, text = "/", padx = 30, pady = 10, command = division)
b_equal = Button(root, text = "=", padx = 29, pady = 10, command = equal)
b_clear = Button(root, text = "C", padx = 29, pady = 10, command = clear)  # functions created

b_sin = Button(root, text = "sin", padx = 29.5, pady = 10, command = sinf)  # functions created
b_cos = Button(root, text = "cos", padx = 28.5, pady = 10, command = cosf)  # functions created
b_tan = Button(root, text = "tan", padx = 29, pady = 10, command = tanf)  # functions created
b_log = Button(root, text = "log", padx = 28.5, pady = 10, command = logf)  # functions created
b_sqrt = Button(root, text = "S.Root", padx = 20, pady = 10, command = sqrtf)  # functions created
b_del = Button(root, text = "Del", padx = 29, pady = 10, command = delete)  # functions created
b_modulus = Button(root, text = "%", padx = 28, pady = 10,
                   command = lambda:mod(float(InputBox.get())))  # functions created

# arranging buttons in the windows

b_clear.grid(row = 2, column = 0)
b_point.grid(row = 2, column = 1)
b_modulus.grid(row = 2, column = 2)
b_del.grid(row = 2, column = 3)

b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b_sin.grid(row = 3, column = 3)

b4.grid(row = 4, column = 0)
b5.grid(row = 4, column = 1)
b6.grid(row = 4, column = 2)
b_cos.grid(row = 4, column = 3)

b7.grid(row = 5, column = 0)
b8.grid(row = 5, column = 1)
b9.grid(row = 5, column = 2)
b_tan.grid(row = 5, column = 3)

b_add.grid(row = 6, column = 0)
b0.grid(row = 6, column = 1)
b_sub.grid(row = 6, column = 2)
b_log.grid(row = 6, column = 3)

b_prod.grid(row = 7, column = 0)
b_equal.grid(row = 7, column = 1)
b_div.grid(row = 7, column = 2)
b_sqrt.grid(row = 7, column = 3)

root.mainloop()
