from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('TicTacToe')
root.resizable(False, False)
root.anchor('w')

photo1 = PhotoImage(file = r"C:\Users\swapn\PycharmProjects\Code Playground\python\TICTACTOE\cross.png")
photo2 = PhotoImage(file = r"C:\Users\swapn\PycharmProjects\Code Playground\python\TICTACTOE\circle.png")
f = 0
c = 0
b = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

l2 = Label(root, text = '', font = "Montserrat 12", height = 2, anchor = 'w', justify = 'left')
l2.grid(row = 4, column = 0, columnspan = 3)


def button_click(b_name, row_n, column_n, b_no):
    global c
    c += 1
    global f
    if f == 0:
        b_name = Label(root, bg = 'white', image = photo1)
        b_name.grid(row = row_n, column = column_n)
        global b
        b[b_no] = f
        f = 1

    elif f == 1:
        b_name = Label(root, bg = 'white', image = photo2)
        b_name.grid(row = row_n, column = column_n)
        b[b_no] = f
        f = 0

    if b[1] == b[2] == b[3]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[1] == b[4] == b[7]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[1] == b[4] == b[7]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[2] == b[5] == b[8]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[4] == b[5] == b[6]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[3] == b[6] == b[9]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[7] == b[8] == b[9]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[1] == b[4] == b[7]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[1] == b[5] == b[9]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif b[3] == b[5] == b[7]:
        messagebox.showinfo('Finished', "Game Over")
        time.sleep(0.5)
        root.quit()

    elif c == 9 :
        messagebox.showinfo('Finished', "Match Draw")
        time.sleep(0.5)
        root.quit()


B1 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B1, 1, 0, 1))
B2 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B2, 1, 1, 2))
B3 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B3, 1, 2, 3))
B4 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B4, 2, 0, 4))
B5 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B5, 2, 1, 5))
B6 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B6, 2, 2, 6))
B7 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B7, 3, 0, 7))
B8 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B8, 3, 1, 8))
B9 = Button(root, bg = 'white', padx = 60, pady = 50, command = lambda: button_click(B9, 3, 2, 9))

l1 = Label(root, text = 'Game starts with cross', font = "Montserrat 12", height = 2, anchor = 'w', justify = 'left')
l1.grid(row = 0, column = 0, columnspan = 3)

B1.grid(row = 1, column = 0)
B2.grid(row = 1, column = 1)
B3.grid(row = 1, column = 2)

B4.grid(row = 2, column = 0)
B5.grid(row = 2, column = 1)
B6.grid(row = 2, column = 2)

B7.grid(row = 3, column = 0)
B8.grid(row = 3, column = 1)
B9.grid(row = 3, column = 2)

root.mainloop()
