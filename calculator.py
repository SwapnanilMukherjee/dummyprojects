from math import cos, factorial, log, radians, sin, sqrt, tan
from tkinter import *

root = Tk()
root.title('Calculator ')
root.resizable(False, False)

first = float()
second = float()
f = int()
current = str()

label = Label(root, text = current,  background="red", font = 'Consolata', width = 36,
              bg = "red", height = 1, anchor = 'e',)
label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

InputBox = Entry(root, width = 50, borderwidth = 10)
InputBox.grid(row = 1, column = 0, columnspan = 5, padx = 10, pady = 10)


def label_update(new):
    global current
    current = current + str(new)
    label = Label(root, text = current,  background="red", font = 'Consolata', width = 36,  bg = "red", height = 1, anchor = 'e',)
    label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)


def b_click(number):
    current = InputBox.get()
    label_update(number)
    InputBox.delete(0, END)
    InputBox.insert(0, str(current) + str(number))


def add():
    label_update('+')
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 1


def sub():
    label_update('-')
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 2


def product():
    label_update('x')
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 3


def division():
    label_update('÷')
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 4


def mod():
    label_update('%')
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 5


def equal():
    # label_update('=')
    global second
    second = float(InputBox.get())
    global first
    global f

    if f == 0:
        result = float(InputBox.get())

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

    elif f == 6:
        result = first ** second

    if result.is_integer():
        result = int(result)
    f = 0
    InputBox.delete(0, END)
    InputBox.insert(0, result)


# make the necessary changes in the display box regarding sin, cos, log functions

def sinf():
    current = float(InputBox.get())
    result = sin(radians(current))
    if result.is_integer():
        result = int(result)
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def cosf():
    current = float(InputBox.get())
    result = cos(radians(current))
    if result.is_integer():
        result = int(result)
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def tanf():
    if InputBox.get() == '90':
        InputBox.delete(0, END)
        InputBox.insert(0, "Invalid Input")
    else:
        current = float(InputBox.get())
        result = tan(radians(current))
        if result.is_integer():
            result = int(result)
        InputBox.delete(0, END)
        InputBox.insert(0, result)


def logf():
    current = float(InputBox.get())
    result = log(current, 10)
    if result.is_integer():
        result = int(result)
    InputBox.delete(0, END)
    InputBox.insert(0, result)


def sqrtf():
    label_update("√")
    current = float(InputBox.get())
    result = sqrt(current)
    if result.is_integer():
        result = int(result)
    InputBox.delete(0, END)
    InputBox.insert(0, result)


# fix here

def delete():
    current = str(InputBox.get())
    length = len(current)
    result = current[:length - 1]
    InputBox.delete(0, END)
    InputBox.insert(0, str(result))

    # global current
    # current = current[:len(current)-1]
    label = Label(root, text = result, font = 'Consolata', bg = "red", width = 36, height = 1, anchor = 'e')
    label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)


def clear():
    InputBox.delete(0, END)
    global current
    current = str()
    label = Label(root, text = current, font = 'Consolata', bg = "red", width = 36, height = 1, anchor = 'e',
                  style = 'design')
    label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)


def fact():
    label_update("!")
    current = float(InputBox.get())
    fact = factorial(current)
    InputBox.delete(0, END)
    InputBox.insert(0, str(fact))


def exponent():
    label_update("^")
    global first
    first = float(InputBox.get())
    InputBox.delete(0, END)
    global f
    f = 6


# creating buttons

b1 = Button(root, text = '1', font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(1))
b2 = Button(root, text = "2", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(2))
b3 = Button(root, text = "3", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(3))
b4 = Button(root, text = "4", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(4))
b5 = Button(root, text = "5", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(5))
b6 = Button(root, text = "6", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(6))
b7 = Button(root, text = "7", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(7))
b8 = Button(root, text = "8", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(8))
b9 = Button(root, text = "9", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(9))
b0 = Button(root, text = "0", font = 'Consolata 11 ', bg = '#32a865', padx = 30, pady = 10, command = lambda:b_click(0))
b_dot = Button(root, text = ".", font = 'Consolata 17 ', padx = 28, pady = 2, command = lambda:b_click('.'))
b_pie = Button(root, text = "π", font = 'Consolata 15 ', padx = 25, pady = 5, command = lambda:b_click(3.14))
b_bracket_left = Button(root, text = "(", font = 'Consolata 17 ', padx = 27, pady = 2,
                        command = None)  # dummy buttons; not working
b_bracket_right = Button(root, text = ")", font = 'Consolata 17 ', padx = 27, pady = 2,
                         command = None)  # dummy buttons; not working
b_exponent = Button(root, text = "^", font = 'Consolata 17 ', padx = 26, pady = 2, command = exponent)

b_add = Button(root, text = "+", font = 'Consolata 11 ', padx = 30, pady = 10, command = add)
b_sub = Button(root, text = "-", font = 'Consolata 15 ', padx = 30, pady = 5, command = sub)
b_prod = Button(root, text = "x", font = 'Consolata 11 ', padx = 30.5, pady = 10, command = product)
b_div = Button(root, text = "÷", font = 'Consolata 15 ', padx = 28, pady = 5, command = division)
b_equal = Button(root, text = "=", font = 'Consolata 14 ', padx = 30, pady = 30, command = equal)
b_clear = Button(root, text = "C", font = 'Consolata 11 ', padx = 28, pady = 10, command = clear)  # functions created

b_fact = Button(root, text = "!", font = 'Consolata 17 ', padx = 28, pady = 2, command = fact)  # functions created
b_sin = Button(root, text = "sin", font = 'Consolata 11 ', padx = 27, pady = 10, command = sinf)  # functions created
b_cos = Button(root, text = "cos", font = 'Consolata 11 ', padx = 25, pady = 10, command = cosf)  # functions created
b_tan = Button(root, text = "tan", font = 'Consolata 11 ', padx = 27, pady = 10, command = tanf)  # functions created
b_log = Button(root, text = "log", font = 'Consolata 11 ', padx = 24, pady = 10, command = logf)  # functions created
b_sqrt = Button(root, text = "√", font = 'Consolata 11 bold ', padx = 29, pady = 10,
                command = sqrtf)  # functions created
b_del = Button(root, text = "Del", font = 'Consolata 11 ', padx = 26, pady = 10, command = delete)  # functions created
b_modulus = Button(root, text = "%", font = 'Consolata 11 ', padx = 27, pady = 10, command = mod)  # functions created

# arranging buttons in the windows

b_clear.grid(row = 2, column = 0)
b_bracket_left.grid(row = 2, column = 1)
b_bracket_right.grid(row = 2, column = 2)
b_exponent.grid(row = 2, column = 3)
b_del.grid(row = 2, column = 4)

b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b_add.grid(row = 3, column = 3)
b_sin.grid(row = 3, column = 4)

b4.grid(row = 4, column = 0)
b5.grid(row = 4, column = 1)
b6.grid(row = 4, column = 2)
b_sub.grid(row = 4, column = 3)
b_cos.grid(row = 4, column = 4)

b7.grid(row = 5, column = 0)
b8.grid(row = 5, column = 1)
b9.grid(row = 5, column = 2)
b_prod.grid(row = 5, column = 3)
b_tan.grid(row = 5, column = 4)

b_sqrt.grid(row = 6, column = 0)
b0.grid(row = 6, column = 1)
b_dot.grid(row = 6, column = 2)
b_div.grid(row = 6, column = 3)
b_equal.grid(row = 6, column = 4, rowspan = 2)

b_pie.grid(row = 7, column = 0)
b_log.grid(row = 7, column = 1)
b_modulus.grid(row = 7, column = 2)
b_fact.grid(row = 7, column = 3)

root.mainloop()

