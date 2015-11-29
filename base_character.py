#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint


class BaseCharacter(object):
    def __init__(self):
        self.attributes = {
            "dexterity": 1,
            "strength": 1,
            "stamina": 1,
            "charisma": 1,
            "manipulation": 1,
            "appearance": 1,
            "intelligence": 1,
            "wits": 1,
            "perception": 1
        }
        self.abilities = {}
        self.virtues = {
            "compassion": 1,
            "temperance": 1,
            "conviction": 1,
            "valor": 1
        }
        self.essence = 1
        self.backgrounds = {}
        self.willpower_purchased = 0

    @staticmethod
    def roll(pool):
        successes = 0
        ones = 0
        for _ in range(pool):
            die = randint(1, 10)
            if die >= 7:
                successes += 1
            if die == 1:
                ones += 1
        if successes == 0 and ones > 0:
            return -1
        return successes

    def get_willpower(self):
        max_virtue = "compassion"
        for virtue in self.virtues.keys():
            if self.virtues[virtue] > self.virtues[max_virtue]:
                max_virtue = virtue
        second_highest_virtue = "temperance"
        if max_virtue == "temperance":
            second_highest_virtue = "compassion"
        for virtue in dict(self.virtues).pop(max_virtue):
            if self.virtues[virtue] > self.virtues[second_highest_virtue]:
                second_highest_virtue = virtue
        return self.virtues[second_highest_virtue] + self.virtues[max_virtue] + self.willpower_purchased

    def ability_check(self, attribute, ability):
        return self.roll(self.get_attribute(attribute) + self.get_ability(ability))

    def virtue_check(self, virtue):
        return self.roll(self.get_virtue(virtue))

    def set_attribute(self, attribute, value):
        if attribute not in self.attributes.keys():
            raise KeyError(attribute + " is not a valid attribute name.")
        if value < 1 or value > 5:
            raise ValueError("Attribute values have to be in the range 1 to 5.")

    def get_attribute(self, attribute):
        if attribute not in self.attributes.keys():
            raise KeyError(attribute + " is not a valid attribute name.")
        return self.attributes[attribute]

    def set_ability(self, ability, value):
        if value < 1 or value > 5:
            raise ValueError("Ability values have to be in the range 1 to 5.")
        self.abilities[ability] = value

    def get_ability(self, ability):
        if ability in self.abilities.keys():
            return self.abilities[ability]
        else:
            return 0

    def set_virtue(self, virtue, value):
        if virtue not in self.virtues.keys():
            raise KeyError(virtue + "is not a valid virtue name.")
        if value < 1 or value > 5:
            raise ValueError("Virtue values have to be in the range 1 to 5.")
        self.virtues[virtue] = value

    def get_virtue(self, virtue):
        if virtue not in self.virtues.keys():
            raise KeyError(virtue + "is not a valid virtue name.")
        return self.virtues[virtue]
