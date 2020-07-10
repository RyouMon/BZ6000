#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super(Application, self).__init__(master, **kwargs)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn01 = tk.Button(self)
        self.btn01["text"] = "Hello World\n(click me)"
        self.btn01["command"] = self.say_hi
        self.btn01.pack(side="top")

        self.btn02 = tk.Button(
            self,
            text="QUIT",
            fg="red",
            command=self.master.destroy
        )
        self.btn02.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("200x100+300+300")
    app = Application(master=root)
    root.mainloop()
