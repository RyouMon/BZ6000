#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用Tkinter实现简单的画板工具
1 直线工具
2 箭头直线工具
3 矩形工具
4 画笔工具
5 橡皮擦
6 清屏
7 改变画笔颜色
8 快捷键切换画笔颜色
"""

from tkinter import Tk, Frame, Canvas, Button
from tkinter import LEFT, LAST
from tkinter import colorchooser


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.buttons = []
        self.lastDraw = 0
        self.startX = 0
        self.startY = 0
        self.start = False
        self.fg = "#000000"
        self.bg = "#ffffff"
        self.createWidget()

    def createWidget(self):
        # 创建并布置画布
        self.drawPad = Canvas(root, bg=self.bg)
        self.drawPad.pack()
        # 创建并布置按钮
        self.lineBtn = Button(root, text="Line")
        self.buttons.append(self.lineBtn)
        self.arrowlineBtn = Button(root, text="ArrowLine")
        self.buttons.append(self.arrowlineBtn)
        self.rectBtn = Button(root, text="Rect")
        self.buttons.append(self.rectBtn)
        self.penBtn = Button(root, text="Pen")
        self.buttons.append(self.penBtn)
        self.eraserBtn = Button(root, text="Eraser")
        self.buttons.append(self.eraserBtn)
        self.clearBtn = Button(root, text="Clear")
        self.buttons.append(self.clearBtn)
        self.colorBtn = Button(root, text="Color")
        self.buttons.append(self.colorBtn)

        for btn in self.buttons:
            btn.pack(side=LEFT, padx=5)

        # 绑定事件管理器
        self.colorBtn.bind_class("Button", "<Button-1>", self.eventManager)
        self.drawPad.bind("<ButtonRelease-1>", self.finishDraw)
        # 颜色切换快捷键
        self.master.bind("<KeyPress-r>", lambda _e: setattr(self, "fg", "#ff0000"))
        self.master.bind("<KeyPress-g>", lambda _e: setattr(self, "fg", "#00ff00"))
        self.master.bind("<KeyPress-b>", lambda _e: setattr(self, "fg", "#0000ff"))

    def eventManager(self, event):
        if event.widget["text"] == "Line":
            self.drawPad.bind("<B1-Motion>", self.drawLine)
        elif event.widget["text"] == "ArrowLine":
            self.drawPad.bind("<B1-Motion>", self.drawArrowLine)
        elif event.widget["text"] == "Rect":
            self.drawPad.bind("<B1-Motion>", self.drawRect)
        elif event.widget["text"] == "Pen":
            self.drawPad.bind("<B1-Motion>", self.draw)
        elif event.widget["text"] == "Eraser":
            self.drawPad.bind("<B1-Motion>", self.eraser)
        elif event.widget["text"] == "Clear":
            self.clear()
        elif event.widget["text"] == "Color":
            self.changeColor()

    def drawLine(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.startX, self.startY, event.x, event.y, fill=self.fg)

    def drawArrowLine(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.startX, self.startY, event.x, event.y, arrow=LAST, fill=self.fg)

    def startDraw(self, event):
        self.drawPad.delete(self.lastDraw)
        if not self.start:
            self.startX = event.x
            self.startY = event.y
            self.start = True

    def finishDraw(self, event):
        self.start = False
        self.lastDraw = 0

    def drawRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_rectangle(self.startX, self.startY, event.x, event.y, outline=self.fg)

    def draw(self, event):
        self.drawPad.create_line(event.x, event.y, event.x+1, event.y+1, fill=self.fg)

    def eraser(self, event):
        self.drawPad.create_rectangle(event.x+5, event.y+5, event.x-5, event.y-5, fill=self.bg, outline=self.bg)

    def clear(self):
        self.drawPad.delete("all")

    def changeColor(self):
        color = colorchooser.askcolor()
        self.fg = color[1]


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.title("Drawing board")
    root.mainloop()
