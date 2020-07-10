#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
玩家和敌人发生碰撞
"""
import pygame
import time
from random import choice, randint

SIZE = WIDTH, HEIGHT = 600, 600
BG = pygame.Color(0, 0, 0)


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        super(BaseItem, self).__init__()


class Main:
    window = None
    p1 = None
    enemy_tanks = []
    enemy_num = 6
    p1_bullets = []
    enemy_bullets = []
    explore_list = []
    wall_list = []

    def __init__(self):
        pygame.init()
        Main.window = pygame.display.set_mode(SIZE)
        self.font = pygame.font.SysFont("kaiti", 20)
        Main.p1 = P1Tank(WIDTH/2, HEIGHT/2)
        self.create_enemies()
        self.create_walls()

    def start(self):
        """游戏主循环"""
        while True:
            time.sleep(0.02)
            Main.window.fill(BG)
            text = self.font.render("敌方坦克剩余数量：{0}".format(len(Main.enemy_tanks)), True, (255, 255, 255))
            Main.window.blit(text, (20, 20))
            self.eventManager()
            self.blit_p1()
            self.blit_enemies()
            self.blit_p1_bullets()
            self.blit_enemy_bullets()
            self.blit_explore()
            self.blit_walls()
            pygame.display.update()

    def eventManager(self):
        """管理事件"""
        events = pygame.event.get()
        for event in events:
            # 响应关闭
            if event.type == pygame.QUIT:
                self.end()
            # 响应按键
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Main.p1.reborn()
                if event.key == pygame.K_DOWN:  # 向下
                    Main.p1.direction = "D"
                elif event.key == pygame.K_UP:  # 向上
                    Main.p1.direction = "U"
                elif event.key == pygame.K_RIGHT:  # 向右
                    Main.p1.direction = "R"
                elif event.key == pygame.K_LEFT:  # 向左
                    Main.p1.direction = "L"
                elif event.key == pygame.K_SPACE:  # 发射子弹
                    Main.p1.shot()
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

    def create_walls(self):
        """创建墙壁"""
        for i in range(6):
            wall = Wall(i*120, HEIGHT/2)
            Main.wall_list.append(wall)

    def create_enemies(self):
        """创建敌方坦克"""
        for i in range(Main.enemy_num):
            top = randint(100, 200)
            left = randint(100, 500)
            speed = randint(1, 4)
            Main.enemy_tanks.append(EnemyTank(left, top, speed))

    def blit_p1(self):
        """绘制玩家P1"""
        if Main.p1:
            if Main.p1.visible:
                if not Main.p1.stop:
                    Main.p1.move()
                    for wall in Main.wall_list:
                        Main.p1.hit(wall)
                    for enemy in Main.enemy_tanks:
                        Main.p1.hit(enemy)
                Main.p1.display()
                for bullet in Main.enemy_bullets:
                    bullet.hit_tank(Main.p1)

    def blit_enemies(self):
        """绘制敌方坦克"""
        for enemy in Main.enemy_tanks:
            if enemy.visible:
                for wall in Main.wall_list:
                    enemy.hit(wall)
                enemy.hit(Main.p1)
                enemy.display()
                enemy.move()
                enemy.shot()
            else:
                Main.enemy_tanks.remove(enemy)

    def blit_p1_bullets(self):
        """绘制玩家P1的子弹"""
        for bullet in Main.p1_bullets:
            for enemy in Main.enemy_tanks:
                bullet.hit_tank(enemy)
            for wall in Main.wall_list:
                bullet.hit_wall(wall)
            if bullet.visible:
                bullet.display()
                bullet.move()
            else:
                Main.p1_bullets.remove(bullet)

    def blit_enemy_bullets(self):
        """绘制敌方坦克的子弹"""
        for bullet in Main.enemy_bullets:
            for wall in Main.wall_list:
                bullet.hit_wall(wall)
            if bullet.visible:
                bullet.display()
                bullet.move()
            else:
                Main.enemy_bullets.remove(bullet)

    def blit_explore(self):
        """绘制爆炸效果"""
        for explore in Main.explore_list:
            if explore.visible:
                explore.play()
            else:
                Main.explore_list.remove(explore)

    def blit_walls(self):
        """绘制墙壁"""
        for wall in Main.wall_list:
            if wall.visible:
                wall.display()
            else:
                Main.wall_list.remove(wall)

    def end(self):
        print("Game Over")
        quit()


class Tank(BaseItem):
    def __init__(self, left, top, speed):
        super(Tank, self).__init__()
        self.direction = "U"
        self.speed = speed
        self.stop = True
        self.visible = True
        self.last_left = left
        self.last_top = top

    def shot(self):
        pass

    def move(self):
        if self.visible:
            self.last_top = self.rect.top
            self.last_left = self.rect.left
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
        if self.visible:
            self.image = self.images[self.direction]
            Main.window.blit(self.image, self.rect)

    def reborn(self):
        pass

    def stay_on(self):
        self.rect.left = self.last_left
        self.rect.top = self.last_top

    def hit(self, obj):
        if pygame.sprite.collide_rect(self, obj):
            self.stay_on()


class P1Tank(Tank):
    def __init__(self, left, top, speed=10):
        super(P1Tank, self).__init__(left, top, speed)
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

    def shot(self):
        if self.visible and len(Main.p1_bullets) < 3:
            Main.p1_bullets.append(Bullet(self))

    def reborn(self):
        if not self.visible:
            self.rect.top = HEIGHT/2
            self.rect.left = WIDTH/2
            self.visible = True


class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        super(EnemyTank, self).__init__(left, top, speed)
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
        num = randint(1, 100)
        if num < 2:
            Main.enemy_bullets.append(Bullet(self))


class Bullet(BaseItem):
    def __init__(self, tank):
        super(Bullet, self).__init__()
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

    def hit_tank(self, tank):
        if pygame.sprite.collide_rect(self, tank):
            self.visible = False
            tank.visible = False
            Main.explore_list.append(Explore(tank))

    def hit_wall(self, wall):
        if pygame.sprite.collide_rect(self, wall):
            self.visible = False
            wall.hp -= 1


class Wall(BaseItem):
    def __init__(self, left, top):
        super(Wall, self).__init__()
        self.image = pygame.image.load("img/steels.gif")
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.hp = 3
        self.visible = True

    def display(self):
        if self.hp:
            Main.window.blit(self.image, self.rect)
        else:
            self.visible = False

class Explore():
    def __init__(self, tank):
        self.rect = tank.rect
        self.images = [
            pygame.image.load("img/blast0.gif"),
            pygame.image.load("img/blast1.gif"),
            pygame.image.load("img/blast2.gif"),
            pygame.image.load("img/blast3.gif"),
            pygame.image.load("img/blast4.gif"),
        ]
        self.step = 0
        self.visible = True

    def play(self):
        if self.step < 4:
            Main.window.blit(self.images[self.step], self.rect)
            self.step += 1
        else:
            self.visible = False


class Music():
    def __init__(self):
        pass

    def play(self):
        pass


if __name__ == '__main__':
    Main().start()
