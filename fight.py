#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pygame
from datetime import datetime
from character_factory import CharacterFactory
from config import SELECTION_COLOR, TICK_DURATION
from pygame.math import Vector2
from combatMaster import CombatMaster
pygame.init()


class Game(object):
    def __init__(self):
        self.size = self.width, self.height = 1024, 768
        self.speed = [Vector2(2, 2),
                      Vector2(3, 1),
                      Vector2(3, 0),
                      Vector2(3, -1),
                      Vector2(2, -2),
                      Vector2(1, -3),
                      Vector2(0, -3),
                      Vector2(-1, -3),
                      Vector2(-2, -2),
                      Vector2(-3, -1),
                      Vector2(-3, 0),
                      Vector2(-3, 1),
                      Vector2(-2, 2),
                      Vector2(-1, 3),
                      Vector2(0, 3),
                      Vector2(1, 3)]
        self.speed_index = 0

        self.screen = pygame.display.set_mode(self.size)

        self.selection = None

        self.actors = []
        character_factory = CharacterFactory()
        hugo = character_factory.create_random_mortal("Hugo")
        hugo.set_surface(self.screen)
        hugo.set_position(Vector2(100, 100))
        self.actors.append(hugo)
        bob = character_factory.create_random_mortal("Bob")
        bob.set_surface(self.screen)
        bob.set_position(Vector2(700, 300))
        self.actors.append(bob)

        self.cm = CombatMaster()
        self.cm.start_fight(hugo, bob)
        self.last_tick = datetime.now()

        self.selected_actors = []

        while True:
            self.draw_frame()

    def handle_events(self, mouse_position):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.selection = event.pos
                if event.button == 2:
                    print(event)
                if event.button == 3 and len(self.selected_actors) > 0:
                    for actor in self.selected_actors:
                        actor.set_target_position((mouse_position[0], mouse_position[1]))
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    selection_rect = pygame.Rect(
                        min(self.selection[0], mouse_position[0]),
                        min(self.selection[1], mouse_position[1]),
                        max(self.selection[0], mouse_position[0]) - min(self.selection[0], mouse_position[0]),
                        max(self.selection[1], mouse_position[1]) - min(self.selection[1], mouse_position[1]))
                    previously_selected_actors = self.selected_actors
                    self.selected_actors = []
                    for actor in self.actors:
                        if actor.select(selection_rect):
                            self.selected_actors.append(actor)
                    self.selection = None
                    if len(self.selected_actors) == 0 and len(previously_selected_actors) > 0:
                        for actor in previously_selected_actors:
                            actor.set_target_position(Vector2(mouse_position))
                            actor.select()
                        self.selected_actors = previously_selected_actors

    def progress_time(self):
        now = datetime.now()
        if (now - self.last_tick) >= TICK_DURATION:
            self.last_tick = self.last_tick + TICK_DURATION
            self.cm.tick()

    def draw_frame(self):
        mouse_position = pygame.mouse.get_pos()
        self.handle_events(mouse_position)
        self.progress_time()

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
