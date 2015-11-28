#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import pygame
from actor import Actor
from config import SELECTION_COLOR
pygame.init()


class Game(object):
    def __init__(self):
        self.size = self.width, self.height = 1024, 768
        self.speed = [2, 2]

        self.screen = pygame.display.set_mode(self.size)

        self.selection = None

        self.fighter = Actor()
        self.fighter.set_surface(self.screen)

        while True:
            self.draw_frame()

    def draw_frame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selection = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                #select
                self.selection = None

        self.fighter.move(self.speed)
        if self.fighter.left() < 0 or self.fighter.right() > self.width:
            self.speed[0] = -self.speed[0]
        if self.fighter.top() < 0 or self.fighter.bottom() > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.fill((255, 255, 255))
        self.fighter.draw()
        if self.selection:
            mouse_position = pygame.mouse.get_pos()
            pygame.draw.rect(
                self.screen,
                SELECTION_COLOR,
                pygame.Rect(
                    self.selection,
                    (mouse_position[0] - self.selection[0], mouse_position[1] - self.selection[1])),
                1)
        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == "__main__":
    Game()
