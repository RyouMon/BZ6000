#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Button, PhotoImage


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        global image
        image = PhotoImage(file="lesson044.png")

        self.btn01 = Button(self, text="Quit", command=self.master.destroy)
        self.btn02 = Button(self, image=image, command=self.master.destroy)

        self.btn01.pack()
        self.btn02.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x200+300+300")
    root.title("Button Widget")
    app = Application(root)
    root.mainloop()
