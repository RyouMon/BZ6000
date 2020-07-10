#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Frame, Checkbutton, IntVar


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v1 = IntVar(0)
        self.v2 = IntVar(0)

        Label(self, text="Which voice actor do you like:").pack()
        self.c1 = Checkbutton(
            self, text="花澤香菜", variable=self.v1,
            onvalue=1, offvalue=0
        )
        self.c2 = Checkbutton(
            self, text="豊崎愛生", variable=self.v2,
            onvalue=1, offvalue=0
        )

        self.c1.pack()
        self.c2.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("CheckButton Widget")
    root.geometry("300x100+300+300")
    app = Application(root)
    root.mainloop()

