#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

        self.actors = []
        hugo = Actor()
        hugo.set_surface(self.screen)
        self.actors.append(hugo)
        self.selected_actors = []

        while True:
            self.draw_frame()

    def draw_frame(self):
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selection = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                selection_rect = pygame.Rect(
                    min(self.selection[0], mouse_position[0]),
                    min(self.selection[1], mouse_position[1]),
                    max(self.selection[0], mouse_position[0]) - min(self.selection[0], mouse_position[0]),
                    max(self.selection[1], mouse_position[1]) - min(self.selection[1], mouse_position[1]))
                self.selected_actors = []
                for actor in self.actors:
                    if actor.select(selection_rect):
                        self.selected_actors.append(actor)
                self.selection = None

        self.actors[0].move(self.speed)
        if self.actors[0].left() < 0 or self.actors[0].right() > self.width:
            self.speed[0] = -self.speed[0]
        if self.actors[0].top() < 0 or self.actors[0].bottom() > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.fill((255, 255, 255))
        for actor in self.actors:
            actor.draw()
        if self.selection:
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
