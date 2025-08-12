from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x500")

def info() :
    messagebox.showinfo("info",'error')

b1 = Button(win , text="info", command= info)
b1.pack()

win.mainloop()