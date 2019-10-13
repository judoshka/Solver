from tkinter import *
from tkinter import messagebox


def solve():
    a = Ea.get()
    b = Eb.get()
    c = Ec.get()
    try:
        af = float(a)
        bf = float(b)
        cf = float(c)
        d = bf * bf - 4 * af * cf
        if (d < 0):
            msg = messagebox.showinfo('Roots', 'No roots')
        elif abs(af) < 0.00001:
            msg = messagebox.showinfo('Roots', 'No square equation')
        elif abs(d) < 0.00001:
            x1 = -bf / 2 / af
            msg = messagebox.showinfo('Roots', 'roots are:\n' + str(x1))
        else:
            x1 = (-bf + d ** 0.5) / 2 / af
            x2 = (-bf - d ** 0.5) / 2 / af
            msg = messagebox.showinfo('Roots', 'roots are:\n' + str(x1) + '\n' + str(x2))

    except ValueError:
        msg = messagebox.showinfo('Roots', 'Invalid input')


top = Tk()
top.geometry("300x200")
window = Listbox(top)
window.pack()
Ea = Entry(window, width=3, bd=2)
Ea.pack(side=LEFT)
L2 = Label(window, text=' x^2 + ')
L2.pack(side=LEFT)
Eb = Entry(window, width=3, bd=2)
Eb.pack(side=LEFT)
L1 = Label(window, text=' x +')
L1.pack(side=LEFT)
Ec = Entry(window, width=3, bd=2)
Ec.pack(side=LEFT)
L0 = Label(window, text=' = 0')
L0.pack(side=LEFT)
btn = Button(top, text='Solve', command=solve)
btn.pack()

window.mainloop()


