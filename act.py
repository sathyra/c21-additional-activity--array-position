import numpy as np
from tkinter import *
root=Tk()
root.geometry("600x400")

t = [("1","2","3","4","5"),("Position: 0","Position: 1","Position: 2","Position: 3","Position: 4"),("Position: -5","Position: -4","Position: -3","Position: -2","Position: -1")]

for x in range(3):
        for y in range(5):
                w = Text(root, width=12, height=2, bg='light blue', padx=10, pady=10, relief=RAISED)
                w.grid(row=x,column=y)
                w.insert(END, t[x][y])

    #top.state("zoomed")
root.mainloop()