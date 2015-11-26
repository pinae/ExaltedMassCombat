#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import pygame
pygame.init()


class Game(object):
    def __init__(self):
        self.size = self.width, self.height = 1024, 768
        self.speed = [2, 2]

        self.screen = pygame.display.set_mode(self.size)

        self.fighter = pygame.image.load(os.path.join("images", "fighter32.png")).convert_alpha()
        self.fighter_rect = self.fighter.get_rect()

        while True:
            self.draw_frame()

    def draw_frame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.fighter_rect = self.fighter_rect.move(self.speed)
        if self.fighter_rect.left < 0 or self.fighter_rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.fighter_rect.top < 0 or self.fighter_rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.fighter, self.fighter_rect)
        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == "__main__":
    Game()
