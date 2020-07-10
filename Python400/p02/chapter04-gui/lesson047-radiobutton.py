#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Frame, Radiobutton, StringVar


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.gender = StringVar(self)
        self.gender.set("M")

        Label(self, text="Choose your gender:").pack()
        Radiobutton(self, text="Woman", value="W", variable=self.gender).pack()
        Radiobutton(self, text="Man", value="M", variable=self.gender).pack()


if __name__ == '__main__':
    root = Tk()
    root.title("RadioButton Widget")
    root.geometry("300x100+300+300")
    app = Application(root)
    root.mainloop()
