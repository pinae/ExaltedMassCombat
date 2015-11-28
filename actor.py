#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from drawable import Drawable
from config import SPRITE_SIZE, SELECTION_COLOR
from pygame import image, Rect
from pygame.math import Vector2
from pygame.transform import rotate, smoothscale
from pygame.draw import circle


class Actor(Drawable):
    def __init__(self):
        super().__init__()
        self.base_image = image.load(os.path.join("images", "fighter.png")).convert_alpha()
        self.direction = 0
        self.selected = False
        self.create_sprite()
        self.position = (0, 0)

    def create_sprite(self):
        rotated = rotate(self.base_image, -(self.direction + 90))
        if self.selected:
            circle(
                rotated,
                SELECTION_COLOR,
                (182, 182),
                138,
                8)
        self.sprite = smoothscale(rotated, (SPRITE_SIZE, SPRITE_SIZE))

    def set_position(self, left, top):
        self.position = (left, top)
        sprite_rect = self.sprite.get_rect()
        self.rect = Rect(
            left - sprite_rect.width // 2,
            top - sprite_rect.height // 2,
            left - sprite_rect.width // 2 + sprite_rect.width,
            top - sprite_rect.height // 2 + sprite_rect.height)

    def position(self):
        return self.position

    def left(self):
        return self.position[0] - SPRITE_SIZE // 2

    def right(self):
        return self.position[0] - SPRITE_SIZE // 2 + SPRITE_SIZE

    def top(self):
        return self.position[1] - SPRITE_SIZE // 2

    def bottom(self):
        return self.position[1] - SPRITE_SIZE // 2 + SPRITE_SIZE

    def move(self, offset):
        self.set_position(self.position[0] + offset[0], self.position[1] + offset[1])
        distance, direction = Vector2(offset[0], offset[1]).as_polar()
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        self.create_sprite()

    def select(self, selection_rect=None):
        if selection_rect is None:
            self.selected = True
        else:
            self.selected = self.rect.colliderect(selection_rect)
        return self.selected

    def deselect(self):
        self.selected = False
