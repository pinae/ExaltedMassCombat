#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from drawable import Drawable
from config import SPRITE_SIZE


class Actor(Drawable):
    def __init__(self):
        super().__init__()
        self.set_image(os.path.join("images", str(SPRITE_SIZE), "fighter.png"))
