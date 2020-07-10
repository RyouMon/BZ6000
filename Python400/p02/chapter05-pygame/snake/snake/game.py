#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame
import time
import random
from snake.snake import Snake, Node
from snake.setting import *


class Game:
    def __init__(self):
        """初始化游戏"""
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Snake")
        self._init_player()
        self.is_game_stop = True
        self.font = pygame.font.SysFont("heiti", 30, True)
        self.over_text = self.font.render("GameOver, Press 'r' restart.", True, FONT_COLOR)

    def _init_player(self):
        self.snake = Snake(Node(*PLAY_INIT_COORDINATE))
        self.food = None

    def start(self):
        """游戏主循环"""
        while True:
            time.sleep(0.06)
            self.window.fill(pygame.Color(*BG_COLOR))
            text = self.font.render(
                "Score: {0}".format(len(self.snake)-1), True, FONT_COLOR
            )
            self.window.blit(text, (20, 20))
            self.event_manage()  # 处理各种事件
            self.blit_food()
            self.eat_food()
            self.move_snake()  # 蛇进行移动
            self.blit_snake()  # 把蛇画到屏幕上
            self.is_game_over()  # 判断游戏是否结束
            pygame.display.update()  # 更新屏幕

    def event_manage(self):
        """管理发生的事件"""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                # 控制移动方向，玩家只能转向90度
                if event.key == pygame.K_DOWN:
                    if self.snake.head.direction != "U":
                        self.snake.head.direction = "D"
                elif event.key == pygame.K_UP:
                    if self.snake.head.direction != "D":
                        self.snake.head.direction = "U"
                elif event.key == pygame.K_LEFT:
                    if self.snake.head.direction != "R":
                        self.snake.head.direction = "L"
                elif event.key == pygame.K_RIGHT:
                    if self.snake.head.direction != "L":
                        self.snake.head.direction = "R"
                # 玩家按下r键重生
                elif event.key == pygame.K_r:
                    if game.is_game_stop:
                        self._init_player()
                # 玩家按下空格键开始游戏
                elif event.key == pygame.K_SPACE:
                    if self.is_game_stop:
                        self.snake.head.speed = 1
                        self.food = self.gen_food()
                        self.is_game_stop = False
            elif event.type == pygame.QUIT:
                self.end()

    def move_snake(self):
        """蛇进行移动"""
        self.snake.move()

    def gen_food(self):
        """随机生成食物，但食物不能出现在蛇的身体里。"""
        is_collide = False
        while True:
            coordinate = self.rnd_coordinate()
            for node in self.snake.nodes:
                if node.column == coordinate[0] and node.row == coordinate[1]:
                    is_collide = True
                    break
            if not is_collide:
                break
        return Node(*coordinate)

    def blit_snake(self):
        """绘制蛇"""
        for node in self.snake.nodes:
            node.display(self.window)

    def blit_food(self):
        """绘制食物"""
        if self.food:
            self.food.display(self.window)

    def eat_food(self):
        """蛇看看有没有可以吃的东西"""
        if self.snake.head.is_against_node(self.food):
            self.snake.eat()
            self.food = self.gen_food()

    def create_node(self, last):
        """创建并返回一个新的节点"""
        return Node(*self.rnd_coordinate(), last=last)

    def rnd_coordinate(self):
        """随机生成一个坐标"""
        rnd_column = random.randint(0, WIDTH/15-1)
        rnd_row = random.randint(0, HEIGHT/15-1)
        return rnd_column, rnd_row

    def is_game_over(self):
        """判断游戏是否结束"""
        is_over = False
        if self.snake.head.is_against_wall():
            is_over = True
        else:
            for i in range(1, len(self.snake)):
                if self.snake.head.is_against_node(self.snake[i]):
                    is_over = True
                    break
        if is_over:
            for node in self.snake.nodes:
                node.speed = 0
            self.is_game_stop = True
            self.window.blit(self.over_text, (HEIGHT/2, WIDTH/2))

    def end(self):
        """结束游戏"""
        pygame.quit()


game = Game()