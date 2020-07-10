#!/usr/bin/env python
# -*-coding:utf-8-*-
from tkinter import Tk, Menu


root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="Save")
filemenu.add_command(label="Open")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Quit", command=root.destroy)

root.config(menu=menubar)
root.title("Menubar")
root.mainloop()