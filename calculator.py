import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")

equation = ""
expression = tk.StringVar()

entry = ttk.Entry(window, textvariable=expression)
entry.grid(row=1, column=1, columnspan=4, sticky="EW")


def press(num):
    global equation
    equation = entry.get()
    equation += str(num)
    expression.set(equation)


def delete_press():
    global equation
    equation = entry.get()
    equation = equation[:-1]
    expression.set(equation)


def clear_press():
    global equation
    equation = ""
    expression.set(equation)


def equal_press():
    global equation
    result = eval(equation)
    equation = str(result)
    expression.set(result)


# Creating Buttons

clear = ttk.Button(window, text="CE", width=7, command=lambda: clear_press())
clear.grid(row=2, column=1, columnspan=3, sticky="EW")

delete = ttk.Button(window, text="C", width=7, command=lambda: delete_press())
delete.grid(row=2, column=4)

one = ttk.Button(window, text=1, width=7, command=lambda: press(1))
one.grid(row=3, column=1)

two = ttk.Button(window, text=2, width=7, command=lambda: press(2))
two.grid(row=3, column=2)

three = ttk.Button(window, text=3, width=7, command=lambda: press(3))
three.grid(row=3, column=3)

decimal = ttk.Button(window, text=".", width=7, command=lambda: press("."))
decimal.grid(row=3, column=4)

four = ttk.Button(window, text=4, width=7, command=lambda: press(4))
four.grid(row=4, column=1)

five = ttk.Button(window, text=5, width=7, command=lambda: press(5))
five.grid(row=4, column=2)

six = ttk.Button(window, text=6, width=7, command=lambda: press(6))
six.grid(row=4, column=3)

divide = ttk.Button(window, text="/", width=7, command=lambda: press("/"))
divide.grid(row=4, column=4)

seven = ttk.Button(window, text=7, width=7, command=lambda: press(7))
seven.grid(row=5, column=1)

eight = ttk.Button(window, text=8, width=7, command=lambda: press(8))
eight.grid(row=5, column=2)

nine = ttk.Button(window, text=9, width=7, command=lambda: press(9))
nine.grid(row=5, column=3)

multiply = ttk.Button(window, text="X", width=7, command=lambda: press("*"))
multiply.grid(row=5, column=4)

zero = ttk.Button(window, text=0, width=7, command=lambda: press(0))
zero.grid(row=6, column=1)

plus = ttk.Button(window, text="+", width=7, command=lambda: press("+"))
plus.grid(row=6, column=2)

minus = ttk.Button(window, text="-", width=7, command=lambda: press("-"))
minus.grid(row=6, column=3)

equal = ttk.Button(window, text="=", width=7, command=lambda: equal_press())
equal.grid(row=6, column=4)

window.mainloop()
