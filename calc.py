from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys


class Calc(Tk):
    def add_number(self, symbol):
        self.entry.insert(END, symbol)

    def calc(self):
        self.second_arg = self.entry.get()
        equation = ''.join((self.first_arg, self.action, self.second_arg))
        value = eval(equation)
        print(value)
        self.entry.delete(0, END)
        self.entry.insert(END, str(value))
        self.first_arg = str(value)
        self.second_arg = 0

    def add_action(self, action):
        self.action = action
        self.first_arg = self.entry.get()
        self.entry.delete(0, END)

    def clear(self):
        self.entry.delete(0, END)
        self.first_arg = 0
        self.second_arg = 0

    def init_numbers(self):
        numbers = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            ".", "0"
        ]
        c = 0
        r = 1
        for number in numbers:
            ttk.Button(self, text=number, command=lambda: self.add_number(number), width=10).grid(row=r, column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.entry = Entry(self, text='', bd=0, width=33)
        self.entry.grid(row=0, column=0, columnspan=3)
        self.action = '+'
        self.first_arg = 0
        self.second_arg = 0
        self.zero = Button(text='0', width=10, command=lambda: self.add_number('0'))
        self.one = Button(text='1', width=10, command=lambda: self.add_number('1'))
        self.two = Button(text='2', width=10, command=lambda: self.add_number('2'))
        self.three = Button(text='3', width=10, command=lambda: self.add_number('3'))
        self.four = Button(text='4', width=10, command=lambda: self.add_number('4'))
        self.five = Button(text='5', width=10, command=lambda: self.add_number('5'))
        self.six = Button(text='6', width=10, command=lambda: self.add_number('6'))
        self.seven = Button(text='7', width=10, command=lambda: self.add_number('7'))
        self.eight = Button(text='8', width=10, command=lambda: self.add_number('8'))
        self.nine = Button(text='9', width=10, command=lambda: self.add_number('9'))
        self.point = Button(text='.', width=10, command=lambda: self.add_number('.'))
        self.zero.grid(column=1, row=4, sticky='WESN')
        self.one.grid(column=0, row=3, sticky='WESN')
        self.two.grid(column=1, row=3, sticky='WESN')
        self.three.grid(column=2, row=3, sticky='WESN')
        self.four.grid(column=0, row=2, sticky='WESN')
        self.five.grid(column=1, row=2, sticky='WESN')
        self.six.grid(column=2, row=2, sticky='WESN')
        self.seven.grid(column=0, row=1, sticky='WESN')
        self.eight.grid(column=1, row=1, sticky='WESN')
        self.nine.grid(column=2, row=1, sticky='WESN')
        self.point.grid(column=0, row=4, sticky='WESN')

        self.plus = Button(text='+', width=10, command=lambda: self.add_action('+'))
        self.minus = Button(text='-', width=10, command=lambda: self.add_action('-'))
        self.divide = Button(text='/', width=10, command=lambda: self.add_action('/'))
        self.multiply = Button(text='*', width=10, command=lambda: self.add_action('*'))
        self.plus.grid(column=3, row=1, sticky='WESN')
        self.minus.grid(column=3, row=2, sticky='WESN')
        self.divide.grid(column=3, row=3, sticky='WESN')
        self.multiply.grid(column=3, row=4, sticky='WESN')

        self.cls = Button(text='C', width=10, command=self.clear)
        self.cls.grid(column=2, row=4, sticky='WESN')

        self.equal = Button(text='=', width=10, command=self.calc)
        self.equal.grid(column=3, row=0, sticky='WESN')

        # self.init_numbers()


def main():
    calc = Calc()
    calc.mainloop()


if __name__ == '__main__':
    main()



'''


def calc(key):
    global memory
    if key == "=":
        # исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
        # исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    # очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


root = Tk()
root.title("Calculator")

btn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", ]


r = 1
c = 0
for i in btn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)
'''
# root.mainloop()
