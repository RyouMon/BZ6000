#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
记事本
实现以下功能
1 打开文件
2 新建文件
3 保存文件
4 改变背景颜色
5 增加快捷键
"""
from tkinter import Tk, Frame, Menu, Text
from tkinter import filedialog, colorchooser
from tkinter import END


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.filename = ""
        self.createWidget()

    def createWidget(self):
        self.menu = Menu(self.master)
        self.fileMenu = Menu(self.menu, tearoff=False)
        self.fileMenu.add_command(label="Open file", command=self.openFile)
        self.fileMenu.add_command(label="New file", command=self.newFile)
        self.fileMenu.add_command(label="Save", command=self.save)
        self.fileMenu.add_command(label="Save as", command=self.saveAs)

        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.menu)

        self.postMenu = Menu(self.master, tearoff=False)
        self.postMenu.add_command(label="Change background", command=self.changeBG)
        self.master.bind(
            "<Button-3>",
            lambda event: self.postMenu.post(event.x_root, event.y_root)
        )

        self.textPad = Text(root)
        self.textPad.pack()

    def newFile(self):
        self.textPad.delete(1.0, END)
        self.filename = ""

    def save(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(
                filetypes=[("文本文件", ".txt"), ],
                defaultextension=".txt"
            )
        with open(self.filename, "w") as f:
            f.write(self.textPad.get(1.0, END))

    def saveAs(self):
        with filedialog.asksaveasfile(
                "w", filetypes=[("文本文件", ".txt"), ],
                defaultextension=".txt"
        ) as f:
            f.write(self.textPad.get(1.0, END))

    def openFile(self):
        self.filename = filedialog.askopenfilename(
            filetypes=[("文本文件", ".txt"), ],
            defaultextension=".txt"
        )
        with open(self.filename, "r") as f:
            self.textPad.delete(1.0, END)
            self.textPad.insert(1.0, f.read())

    def changeBG(self):
        self.bg = colorchooser.askcolor()
        self.textPad.config(bg=self.bg[1])


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.title("Notebook")
    root.mainloop()
