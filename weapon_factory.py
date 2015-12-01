#!/usr/bin/python
# -*- coding: utf-8 -*-


class WeaponFactory(object):
    @staticmethod
    def get_punch_hand():
        return {
            "name": "hand",
            "ability": "martial arts",
            "speed": 5,
            "accuracy": 1,
            "damage": 0,
            "damage type": "B",
            "defense": 2,
            "rate": 3,
            "range": 0
        }

    @staticmethod
    def get_kick_foot():
        return {
            "name": "foot",
            "ability": "martial arts",
            "speed": 5,
            "accuracy": 0,
            "damage": 3,
            "damage type": "B",
            "defense": -2,
            "rate": 2,
            "range": 0.2
        }

    @staticmethod
    def get_straight_sword():
        return {
            "name": "straight sword",
            "ability": "melee",
            "speed": 4,
            "accuracy": 2,
            "damage": 3,
            "damage type": "L",
            "defense": 1,
            "rate": 2,
            "range": 0.9
        }

    @staticmethod
    def get_spear():
        return {
            "name": "spear",
            "ability": "melee",
            "speed": 5,
            "accuracy": 1,
            "damage": 4,
            "damage type": "L",
            "defense": 2,
            "rate": 2,
            "range": 1.5
        }
