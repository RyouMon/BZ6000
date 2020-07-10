#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import copy
from snake.setting import *


class Node(pygame.sprite.Sprite):
    def __init__(self, column, row, direction="U", speed=0):
        super(Node, self).__init__()
        self.image = pygame.image.load("snake/img/node.gif")
        self.rect = self.image.get_rect()
        self.column = column
        self.row = row
        self.direction = direction
        self.speed = speed
        self.update_rect()

    def update_rect(self):
        """更新自己的坐标"""
        self.rect.left = self.column * self.rect.width
        self.rect.top = self.row * self.rect.height

    def move(self):
        """向某个方向移动"""
        if self.direction == "U":
            self.row -= self.speed
        elif self.direction == "D":
            self.row += self.speed
        elif self.direction == "L":
            self.column -= self.speed
        else:  # self.direction == "R"
            self.column += self.speed

    def display(self, surface):
        """把自己绘制到一个Surface对象上"""
        self.update_rect()
        surface.blit(self.image, self.rect)

    def is_against_wall(self):
        """判断是否撞到边界"""
        if self.rect.left < 0:
            return True
        elif self.rect.left + self.rect.width > WIDTH:
            return True
        elif self.rect.top < 0:
            return True
        elif self.rect.top + self.rect.height > HEIGHT:
            return True
        else:
            return False

    def is_against_node(self, node):
        """判断是否与其他节点发生碰撞"""
        if node:
            if self.column == node.column and self.row == node.row:
                return True
            else:
                return False
        else:
            return False


class Snake:
    def __init__(self, head):
        self.nodes = [head]
        self.need_digestion = False

    @property
    def head(self):
        return self.nodes[0]

    def move(self):
        """蛇身跟随蛇头移动"""
        self.nodes.insert(0, copy.copy(self.head))
        self.head.move()
        # 判断是否需要消化食物
        if self.need_digestion:
            self.need_digestion = False
        else:
            self.nodes.pop()

    def eat(self):
        """进食，告诉蛇需要消化食物。"""
        self.need_digestion = True

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, item):
        return self.nodes[item]