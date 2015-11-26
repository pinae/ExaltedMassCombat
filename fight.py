#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import pygame
from actor import Actor
pygame.init()


class Game(object):
    def __init__(self):
        self.size = self.width, self.height = 1024, 768
        self.speed = [2, 2]

        self.screen = pygame.display.set_mode(self.size)

        self.fighter = Actor()
        self.fighter.set_surface(self.screen)

        while True:
            self.draw_frame()

    def draw_frame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.fighter.move(self.speed)
        if self.fighter.left() < 0 or self.fighter.right() > self.width:
            self.speed[0] = -self.speed[0]
        if self.fighter.top() < 0 or self.fighter.bottom() > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.fill((255, 255, 255))
        self.fighter.draw()
        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == "__main__":
    Game()
