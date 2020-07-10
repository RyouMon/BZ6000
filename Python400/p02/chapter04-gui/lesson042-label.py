#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Label, PhotoImage


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        global photo
        photo = PhotoImage(file="lesson042.png")
        self.photo_label = Label(
            self,
            image=photo,
            bd=5,
            relief="raised"
        )
        self.photo_label.pack()

        self.name_label = Label(
            self,
            text="Kana Hanazawa",
            font=("Segoe Script", 30),
            fg="white",
            bg="pink",
            width=23
        )
        self.name_label.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("Label Widget")
    app = Application(root)
    root.mainloop()