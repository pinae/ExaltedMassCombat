#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from config import SPRITE_SIZE
from pygame import image
from pygame.transform import smoothscale
from pygame.math import Vector2


class Drawable(object):
    def __init__(self):
        self.sprite = None
        self.set_image(os.path.join("images", "none.png"))
        self.rect = self.sprite.get_rect()
        self.surface = None

    def set_image(self, filename):
        self.sprite = smoothscale(image.load(filename).convert_alpha(), (SPRITE_SIZE, SPRITE_SIZE))

    def set_surface(self, surface):
        self.surface = surface

    def set_position(self, new_position):
        self.rect.left = new_position.x
        self.rect.top = new_position.y

    def position(self):
        return Vector2(self.rect.left, self.rect.top)

    def left(self):
        return self.rect.left

    def right(self):
        return self.rect.right

    def top(self):
        return self.rect.top

    def bottom(self):
        return self.rect.bottom

    def move(self, offset):
        self.rect = self.rect.move(offset)

    def draw(self):
        if self.surface:
            self.surface.blit(self.sprite, self.rect)
