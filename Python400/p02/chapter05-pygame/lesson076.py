#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
坦克转向和移动
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
        Main.p1 = MyTank(300, 300)
        # 进入主循环
        while True:
            Main.window.fill(BG)
            Main.window.blit(text, (20, 20))
            self.eventManager()
            Main.p1.display()
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
                    Main.p1.direction = "D"
                    Main.p1.move()
                elif event.key == pygame.K_UP:
                    Main.p1.direction = "U"
                    Main.p1.move()
                elif event.key == pygame.K_RIGHT:
                    Main.p1.direction = "R"
                    Main.p1.move()
                elif event.key == pygame.K_LEFT:
                    Main.p1.direction = "L"
                    Main.p1.move()

    def end(self):
        print("Game Over")
        quit()


class Tank:
    def __init__(self):
        self.direction = "U"
        self.speed = 10


    def shot(self):
        pass

    def move(self):
        if self.direction == "L":
            self.rect.left -= self.speed
        elif self.direction == "R":
            self.rect.left += self.speed
        elif self.direction == "U":
            self.rect.top -= self.speed
        elif self.direction == "D":
            self.rect.top += self.speed

    def display(self):
        self.image = self.images[self.direction]
        Main.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self, top, left):
        super(MyTank, self).__init__()
        self.images = {
            "U": pygame.image.load("img/p1tankU.gif"),
            "D": pygame.image.load("img/p1tankD.gif"),
            "L": pygame.image.load("img/p1tankL.gif"),
            "R": pygame.image.load("img/p1tankR.gif"),
        }
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.top = top
        self.rect.left = left


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