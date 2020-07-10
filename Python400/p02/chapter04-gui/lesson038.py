#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *

# 1 创建根窗口
root = Tk()

# 2 新建组件
btn01 = Button(root)
btn01["text"] = "Hello!"
btn01.pack()


def hello(e):
    print("Hello World!")

# 3 绑定事件方法
btn01.bind("<Button-1>", hello)
# 4 进入主事件循环
root.mainloop()