#!/usr/bin/python
# -*- coding: utf-8 -*-

from base_character import BaseCharacter
from random import shuffle, randint


class CharacterFactory(object):
    def __init__(self):
        self.character_number = 0
        self.used_character_names = []

    def create_random_mortal(self, name=None):
        self.character_number += 1
        if not name:
            name = "Unnamed character " + str(self.character_number)
        if name in self.used_character_names:
            raise KeyError(name + " is already used for another character. Use another name.")
        else:
            self.used_character_names.append(name)
        char = BaseCharacter(name)
        attributes = [["strength", "dexterity", "stamina"],
                      ["manipulation", "charisma", "appearance"],
                      ["intelligence", "wits", "perception"]]
        shuffle(attributes)
        for i, bonus in enumerate([4, 3, 3]):
            for _ in range(bonus):
                bonused_attribute = attributes[i][randint(0, len(attributes[i]) - 1)]
                char.set_attribute(bonused_attribute, char.get_attribute(bonused_attribute) + 1)
                if char.get_attribute(bonused_attribute) >= 5:
                    del attributes[i][bonused_attribute]
        abilities = [
            "archery", "martial arts", "melee", "thrown", "war",
            "athletics", "awareness", "dodge", "larceny", "stealth",
            "integrity", "performance", "presence", "resistance", "survival",
            "bureaucracy", "linguistics", "ride", "sail", "socialize",
            "craft (air)", "craft (wood)", "craft (fire)", "craft (earth)",
            "investigation", "lore", "medicine", "occult"]
        for _ in range(18):
            bonused_ability = abilities[randint(0, len(abilities) - 1)]
            char.set_ability(bonused_ability, char.get_ability(bonused_ability) + 1)
            if char.get_ability(bonused_ability) >= 5:
                del abilities[bonused_ability]
        # This poor guy has not spent any of his 21 bonus points.
        return char

    def create_random_heroic_mortal(self, name=None):
        self.character_number += 1
        char = BaseCharacter(name)
        attributes = [["strength", "dexterity", "stamina"],
                      ["manipulation", "charisma", "appearance"],
                      ["intelligence", "wits", "perception"]]
        shuffle(attributes)
        for i, bonus in enumerate([6, 4, 3]):
            for _ in range(bonus):
                bonused_attribute = attributes[i][randint(0, len(attributes[i]) - 1)]
                char.set_attribute(bonused_attribute, char.get_attribute(bonused_attribute) + 1)
                if char.get_attribute(bonused_attribute) >= 5:
                    del attributes[i][bonused_attribute]
        abilities = [
            "archery", "martial arts", "melee", "thrown", "war",
            "athletics", "awareness", "dodge", "larceny", "stealth",
            "integrity", "performance", "presence", "resistance", "survival",
            "bureaucracy", "linguistics", "ride", "sail", "socialize",
            "craft (air)", "craft (wood)", "craft (fire)", "craft (earth)",
            "investigation", "lore", "medicine", "occult"]
        for _ in range(25):
            bonused_ability = abilities[randint(0, len(abilities) - 1)]
            char.set_ability(bonused_ability, char.get_ability(bonused_ability) + 1)
            if char.get_ability(bonused_ability) >= 5:
                del abilities[bonused_ability]
        # This poor guy has not spent any of his 21 bonus points.
        return char

    def get_number_of_created_characters(self):
        return self.character_number
