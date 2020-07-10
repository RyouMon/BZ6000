#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
敌方坦克发射子弹
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
    p1_bullets = []
    enemy_bullets = []

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
            self.blit_p1_bullets()
            self.blit_enemy_bullets()
            if not Main.p1.stop:
                Main.p1.move()
            pygame.display.update()

    def eventManager(self):
        """
        事件管理器，捕获并处理事件
        """
        events = pygame.event.get()
        for event in events:
            # 响应关闭
            if event.type == pygame.QUIT:
                self.end()
            # 响应按键
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  # 向下
                    Main.p1.direction = "D"
                elif event.key == pygame.K_UP:  # 向上
                    Main.p1.direction = "U"
                elif event.key == pygame.K_RIGHT:  # 向右
                    Main.p1.direction = "R"
                elif event.key == pygame.K_LEFT:  # 向左
                    Main.p1.direction = "L"
                elif event.key == pygame.K_SPACE:  # 发射子弹
                    if len(Main.p1_bullets) < 3:
                        Main.p1_bullets.append(Bullet(Main.p1))
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
            # 随机发射子弹
            num = randint(1, 100)
            if num < 2:
                Main.enemy_bullets.append(enemy.shot())

    def blit_p1_bullets(self):
        for bullet in Main.p1_bullets:
            if bullet.visible:
                bullet.display()
                bullet.move()
            else:
                Main.p1_bullets.remove(bullet)

    def blit_enemy_bullets(self):
        for bullet in Main.enemy_bullets:
            if bullet.visible:
                bullet.display()
                bullet.move()
            else:
                Main.enemy_bullets.remove(bullet)

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

    def shot(self):
        return Bullet(self)


class Bullet:
    def __init__(self, tank):
        self.direction = tank.direction
        self.image = pygame.image.load("img/enemymissile.gif")
        self.rect = self.image.get_rect()
        self.speed = 10
        self.visible = True
        if self.direction == "U":
            self.rect.top = tank.rect.top - self.rect.height/2
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
        elif self.direction == "D":
            self.rect.top = tank.rect.top + tank.rect.height - self.rect.height/2
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
        elif self.direction == "L":
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
            self.rect.left = tank.rect.left - self.rect.width/2
        elif self.direction == "R":
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
            self.rect.left = tank.rect.left + tank.rect.width - self.rect.width/2

    def move(self):
        if self.direction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.visible = False
        elif self.direction == "D":
            if self.rect.top + self.rect.height < HEIGHT:
                self.rect.top += self.speed
            else:
                self.visible = False
        elif self.direction == "L":
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.visible = False
        elif self.direction == "R":
            if self.rect.left + self.rect.width < WIDTH:
                self.rect.left += self.speed
            else:
                self.visible = False

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
