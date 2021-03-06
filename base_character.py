#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import floor
from weapon_factory import WeaponFactory
from actor import Actor
from config import SPRITE_SIZE
from random import randint
from pygame.math import Vector2


class BaseCharacter(Actor):
    def __init__(self, name):
        self.name = name
        super(BaseCharacter, self).__init__()
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
        self.weapon = WeaponFactory.get_punch_hand()
        self.health_levels = [0, -1, -1, -2, -2, -4, -1000]
        self.wounds = {
            "bashing": 0,
            "lethal": 0
        }
        self.fraction = None

    def __str__(self):
        return "Character {}".format(self.name)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def roll(pool, damage=False):
        successes = 0
        ones = 0
        for _ in range(pool):
            die = randint(1, 10)
            if die >= 7:
                successes += 1
            if not damage and die == 10:
                successes += 1
            if die == 1:
                ones += 1
        if successes == 0 and ones > 0:
            return -1
        return successes

    def get_name(self):
        return self.name

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
        return self.roll(
            min(self.get_attribute(attribute) + self.get_ability(ability),
                max(self.get_attribute(attribute) + self.get_ability(ability) + self.get_wound_penalty(), self.essence))
        )

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

    def set_fraction(self, fraction):
        self.fraction = fraction

    def get_fraction(self):
        return self.fraction

    def attack(self, dv):
        successes = self.ability_check("dexterity", self.weapon["ability"])
        if successes < 0:
            # Botch: Hitting myself without DV.
            self.soak(self.get_attribute("strength") + self.weapon["damage"], self.weapon["damage type"])
        if successes < dv:
            return 0, 'B'
        return self.get_attribute("strength") + self.weapon["damage"] + successes - dv, self.weapon["damage type"]

    def soak(self, damage, damage_type):
        wounds = self.roll(damage, damage=True)
        if damage_type not in ["B", "L"]:
            raise ValueError(damage_type + " is not a valid damage type. Valid are B and L.")
        if damage_type == "B":
            if self.wounds["bashing"] + wounds > len(self.health_levels):
                bashing_overflow = self.wounds["bashing"] + wounds - len(self.health_levels)
                self.wounds["bashing"] = len(self.health_levels)
                self.wounds["lethal"] += bashing_overflow
            else:
                self.wounds["bashing"] += wounds
        if damage_type == "L":
            self.wounds["lethal"] += wounds
            self.wounds["bashing"] = max(self.wounds["bashing"], self.wounds["lethal"])

    def is_alive(self):
        return self.wounds["lethal"] < len(self.health_levels) and self.wounds["bashing"] < len(self.health_levels)

    def get_wound_penalty(self):
        return self.health_levels[max(self.wounds["bashing"], self.wounds["lethal"])]

    def get_dodge_dv(self):
        return int(floor((self.get_attribute("dexterity") +
                          self.get_ability("dodge")) / 2)) + self.get_wound_penalty()

    def get_parry_dv(self):
        return int(floor((self.get_attribute("dexterity") +
                          self.get_ability(self.weapon["ability"]) +
                          self.weapon["defense"]) / 2)) + self.get_wound_penalty()

    def get_best_dv(self):
        return max(self.get_dodge_dv(), self.get_parry_dv())

    def initiative(self):
        return self.ability_check("perception", "awareness")

    def get_movement_distance(self):
        return self.attributes["dexterity"] - self.get_wound_penalty()

    def act(self, fighters):
        nearest_enemy = None
        nearest_enemy_distance = 1000000
        for fighter in fighters:
            if fighter.get_name() != self.get_name() and (
                    not fighter.get_fraction() or
                    not self.get_fraction() or
                    fighter.get_fraction() != self.get_fraction()):
                dx = (self.get_position()[0] - fighter.get_position()[0]) / SPRITE_SIZE
                dy = (self.get_position()[1] - fighter.get_position()[1]) / SPRITE_SIZE
                if dx * dx + dy * dy < nearest_enemy_distance:
                    nearest_enemy = fighter
                    nearest_enemy_distance = dx * dx + dy * dy
        max_attack_range = (0.5 + self.weapon["range"] + self.get_movement_distance())
        if nearest_enemy_distance <= max_attack_range * max_attack_range:  # The nearest enemy is in range.
            attack_range = (0.5 + self.weapon["range"])
            if nearest_enemy_distance > attack_range * attack_range:
                positional_offset = nearest_enemy.get_position() - self.get_position()
                positional_offset.scale_to_length(
                    (positional_offset.length() / SPRITE_SIZE - attack_range) * SPRITE_SIZE)
                self.move(positional_offset)
            damage, damage_type = self.attack(nearest_enemy.get_best_dv())
            print("{}: Attacking {} with {} damage of type {}.".format(
                self.name, nearest_enemy.get_name(), damage, damage_type))
            nearest_enemy.soak(damage, damage_type)
            return self.weapon['speed']
        elif self.get_target_position() is not None:
            positional_offset = self.get_target_position() - self.get_position()
            positional_offset.scale_to_length(
                min(positional_offset.length(), self.get_movement_distance() * SPRITE_SIZE))
            print("{}: Moving to position {}.".format(self.name, positional_offset))
            self.move(positional_offset)
            if (self.get_target_position() - self.get_position()).length() < 0.1:
                self.set_target_position(None)
            return 1
        else:  # We wait because we have no orders.
            print("{}: Waiting because I have no orders.".format(self.name))
            return 1
