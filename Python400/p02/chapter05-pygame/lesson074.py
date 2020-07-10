#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
在屏幕上显示字体
"""
import pygame


SIZE = WIDTH, HEIGHT = 600, 600
BG = pygame.Color(255, 255, 255)


class Main:
    window = None

    def __init__(self):
        pygame.init()

    def start(self):
        # 初始化窗口
        Main.window = pygame.display.set_mode(SIZE)
        font = pygame.font.SysFont("kaiti", 20)
        text = font.render("敌方坦克剩余数量：{0}".format(6), True, (0, 0, 0))
        # 进入主循环
        while True:
            Main.window.fill(BG)
            Main.window.blit(text, (20, 20))
            self.eventManager()
            pygame.display.update()

    def eventManager(self):
        events = pygame.event.get()
        for event in events:
            # 响应关闭
            if event.type == pygame.QUIT:
                self.end()
            # 响应按键
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print("down")
                elif event.key == pygame.K_UP:
                    print("up")
                elif event.key == pygame.K_RIGHT:
                    print("right")
                elif event.key == pygame.K_LEFT:
                    print("left")

    def end(self):
        print("Game Over")
        quit()


class Tank():
    def __init__(self):
        pass

    def shot(self):
        pass

    def move(self):
        pass

    def display(self):
        pass


class MyTank(Tank):
    def __init__(self):
        pass


class EnenmyTank(Tank):
    def __init__(self):
        pass


class Bullet:
    def __init__(self):
        pass

    def move(self):
        pass


class Wall():
    def __init__(self):
        pass

    def display(self):
        pass


class Explore():
    def __init__(self):
        pass

    def display(self):
        pass


class Music():
    def __init__(self):
        pass

    def play(self):
        pass


if __name__ == '__main__':

    Main().start()