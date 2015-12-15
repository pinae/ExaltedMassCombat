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
        self.position = Vector2(0, 0)
        self.target_position = None

    def create_sprite(self):
        base = self.base_image.copy()
        if self.selected:
            circle(
                base,
                SELECTION_COLOR,
                (128, 128),
                128,
                8)
        rotated = rotate(base, -(self.direction + 90))
        self.sprite = smoothscale(rotated, (round(rotated.get_width() * SPRITE_SIZE / self.base_image.get_width()),
                                            round(rotated.get_height() * SPRITE_SIZE / self.base_image.get_width())))

    def set_position(self, new_position):
        self.position = new_position
        sprite_rect = self.sprite.get_rect()
        self.rect = Rect(
            new_position.x - sprite_rect.width // 2,
            new_position.y - sprite_rect.height // 2,
            new_position.x - sprite_rect.width // 2 + sprite_rect.width,
            new_position.y - sprite_rect.height // 2 + sprite_rect.height)

    def set_target_position(self, target_vector=None):
        self.target_position = target_vector

    def get_target_position(self):
        return self.target_position

    def get_position(self):
        return self.position

    def left(self):
        return self.position.x - SPRITE_SIZE // 2

    def right(self):
        return self.position.x - SPRITE_SIZE // 2 + SPRITE_SIZE

    def top(self):
        return self.position.y - SPRITE_SIZE // 2

    def bottom(self):
        return self.position.y - SPRITE_SIZE // 2 + SPRITE_SIZE

    def move(self, offset):
        distance, direction = offset.as_polar()
        self.set_direction(direction)
        self.set_position(self.get_position() + offset)

    def set_direction(self, direction):
        self.direction = direction
        self.create_sprite()

    def select(self, selection_rect=None):
        if selection_rect is None:
            self.selected = True
        else:
            self.selected = self.rect.colliderect(selection_rect)
        self.create_sprite()
        return self.selected

    def deselect(self):
        self.selected = False
