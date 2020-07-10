#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
完善子弹类
"""
import pygame
import time
from random import choice, randint

SIZE = WIDTH, HEIGHT = 600, 600
BG = pygame.Color(255, 255, 255)


class Main:
    window = None
    p1 = None
    enemy_tanks = []
    enemy_num = 6

    def __init__(self):
        pygame.init()

    def start(self):
        # 初始化窗口
        Main.window = pygame.display.set_mode(SIZE)
        font = pygame.font.SysFont("kaiti", 20)
        text = font.render("敌方坦克剩余数量：{0}".format(Main.enemy_num), True, (0, 0, 0))
        Main.p1 = MyTank(300, 300)
        self.create_enemies()

        # 进入主循环
        while True:
            time.sleep(0.02)
            Main.window.fill(BG)
            Main.window.blit(text, (20, 20))
            self.eventManager()
            Main.p1.display()
            self.blit_enemies()
            if not Main.p1.stop:
                Main.p1.move()
            pygame.display.update()

    def eventManager(self):
        events = pygame.event.get()
        for event in events:
            # 响应关闭
            if event.type == pygame.QUIT:
                self.end()
            # 响应按键
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Main.p1.direction = "D"
                elif event.key == pygame.K_UP:
                    Main.p1.direction = "U"
                elif event.key == pygame.K_RIGHT:
                    Main.p1.direction = "R"
                elif event.key == pygame.K_LEFT:
                    Main.p1.direction = "L"
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
                if event.key == pygame.K_DOWN or \
                        event.key == pygame.K_UP or \
                        event.key == pygame.K_LEFT or \
                        event.key == pygame.K_RIGHT:
                    Main.p1.stop = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or \
                        event.key == pygame.K_UP or \
                        event.key == pygame.K_LEFT or \
                        event.key == pygame.K_RIGHT:
                    Main.p1.stop = True

    def create_enemies(self):
        for i in range(Main.enemy_num):
            top = randint(100, 200)
            left = randint(100, 500)
            speed = randint(1, 4)
            Main.enemy_tanks.append(EnemyTank(top, left, speed))

    def blit_enemies(self):
        for enemy in Main.enemy_tanks:
            enemy.display()
            enemy.move()

    def end(self):
        print("Game Over")
        quit()


class Tank:
    def __init__(self, speed):
        self.direction = "U"
        self.speed = speed
        self.stop = True

    def shot(self):
        pass

    def move(self):
        if self.direction == "L":
            if self.rect.left > 0:  # 限制坦克不会超过边界
                self.rect.left -= self.speed
        elif self.direction == "R":
            if self.rect.left + self.rect.width < WIDTH:
                self.rect.left += self.speed
        elif self.direction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == "D":
            if self.rect.top + self.rect.height < HEIGHT:
                self.rect.top += self.speed

    def display(self):
        self.image = self.images[self.direction]
        Main.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self, top, left, speed=10):
        super(MyTank, self).__init__(speed)
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


class EnemyTank(Tank):
    def __init__(self, top, left, speed):
        super(EnemyTank, self).__init__(speed)
        self.images = {
            "U": pygame.image.load("img/enemy1U.gif"),
            "D": pygame.image.load("img/enemy1D.gif"),
            "L": pygame.image.load("img/enemy1L.gif"),
            "R": pygame.image.load("img/enemy1R.gif"),
        }
        self.direction = choice(["U", "D", "L", "R"])
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.step = 100

    def move(self):
        self.step -= 1
        if self.step < 0:
            self.direction = choice(["U", "D", "L", "R"])
            self.step = 100
        super(EnemyTank, self).move()


class Bullet:
    def __init__(self, tank):
        self.image = pygame.image.load("img/enemymissile.gif")
        self.rect = self.image.get_rect()
        if tank.dirction == "U":
            self.rect.top = tank.rect.top
            self.rect.left = tank.rect.left + tank.rect.width/2
        elif tank.dirction == "D":
            self.rect.top = tank.rect.top + tank.rect.height
            self.rect.left = tank.rect.left + tank.rect.width/2
        elif tank.dirction == "L":
            self.rect.top = tank.rect.top + tank.rect.height/2
            self.rect.left = tank.rect.left
        elif tank.dirction == "R":
            self.rect.top = tank.rect.top + tank.rect.height/2
            self.rect.left = tank.rect.left + tank.rect.width

    def move(self):
        pass

    def display(self):
        Main.window.blit(self.image, self.rect)


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
