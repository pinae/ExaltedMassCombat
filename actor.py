#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from drawable import Drawable
from config import SPRITE_SIZE
from pygame import image
from pygame.math import Vector2
from pygame.transform import rotate, smoothscale


class Actor(Drawable):
    def __init__(self):
        super().__init__()
        self.base_image = image.load(os.path.join("images", "fighter.png")).convert_alpha()
        self.direction = 0
        self.sprite = smoothscale(self.base_image, (SPRITE_SIZE, SPRITE_SIZE))

    def move(self, offset):
        super().move(offset)
        distance, direction = Vector2(offset[0], offset[1]).as_polar()
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        self.sprite = smoothscale(rotate(self.base_image, -(self.direction + 90)), (SPRITE_SIZE, SPRITE_SIZE))
