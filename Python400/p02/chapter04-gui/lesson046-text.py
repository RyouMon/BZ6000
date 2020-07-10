#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Frame, Button, PhotoImage, Text
from tkinter import INSERT, CURRENT, END
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        Button(self, text="Insert Text", command=self.insertText).pack(side="left")
        Button(self, text="Test Tag", command=self.testTag).pack(side="left")
        Button(self, text="Return Text", command=self.returnText).pack(side="left")
        Button(self, text="Add Image", command=self.addImage).pack(side="left")
        Button(self, text="Add Widget", command=self.addWidget).pack(side="left")

        self.text = Text(root, width=300, height=160, bg="gray", fg="white")
        self.text.pack(side="bottom")

    def insertText(self):
        self.text.insert(INSERT, "Kana")
        self.text.insert(END, "❀\n")

    def returnText(self):
        messagebox.showinfo("Text", self.text.get(1.0, END))

    def addImage(self):
        global image
        image = PhotoImage(file="lesson046.png")
        self.text.image_create(END, image=image)

    def addWidget(self):
        btn = Button(self.text, text="press me♥")
        self.text.window_create(CURRENT, window=btn)

    def testTag(self):
        self.text.tag_add("kana", 1.0, 1.4)
        self.text.tag_config("kana", font=("Segoe Script", 30), foreground="pink")
        self.text.tag_add("flower", 1.4, 1.5)
        self.text.tag_config("flower", foreground="red")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+300+300")
    root.title("Text Widget")
    app = Application(root)
    root.mainloop()
