#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户登录界面
"""
from tkinter import Tk, Entry, Label, Frame, Button, messagebox, StringVar


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.user = StringVar(self)
        self.password = StringVar(self)

        Label(self, text="User").pack()
        self.user_entry = Entry(self, width=30, textvariable=self.user)
        self.user_entry.pack()

        Label(self, text="Password").pack()
        self.password_entry = Entry(self, width=30, show="*", textvariable=self.password)
        self.password_entry.pack()

        self.btn = Button(self, text="Login", command=self.login)
        self.btn.pack()

    def login(self):
        messagebox.showinfo("Login", "Welcome! {0}.".format(self.user.get()))


if __name__ == '__main__':
    root = Tk()
    root.title("Entry Widget")
    app = Application(root)
    root.mainloop()
