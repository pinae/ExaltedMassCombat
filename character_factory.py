#!/usr/bin/python
# -*- coding: utf-8 -*-

from base_character import BaseCharacter
from random import shuffle, randint


class CharacterFactory(object):
    @staticmethod
    def create_random_mortal(name=None):
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
                    attributes[i].pop(bonused_attribute)
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
                abilities.pop(bonused_ability)
        # This poor guy has not spent any of his 21 bonus points.
        return char

    @staticmethod
    def create_random_heroic_mortal():
        char = BaseCharacter()
        attributes = [["strength", "dexterity", "stamina"],
                      ["manipulation", "charisma", "appearance"],
                      ["intelligence", "wits", "perception"]]
        shuffle(attributes)
        for i, bonus in enumerate([6, 4, 3]):
            for _ in range(bonus):
                bonused_attribute = attributes[i][randint(0, len(attributes[i]) - 1)]
                char.set_attribute(bonused_attribute, char.get_attribute(bonused_attribute) + 1)
                if char.get_attribute(bonused_attribute) >= 5:
                    attributes[i].pop(bonused_attribute)
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
                abilities.pop(bonused_ability)
        # This poor guy has not spent any of his 21 bonus points.
        return char
