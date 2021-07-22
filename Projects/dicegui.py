import random

from tkinter import *

root=Tk()
root.geometry("700x450")

label=Label(root,text='',font=("times",200))

def roll():
    number=['\u2680','\u2861','\u2862','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()

button=Button(root,text="Roll Dice",command="roll")
button.place(x=325,y=10)

root.mainloop()