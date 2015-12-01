#!/usr/bin/python
# -*- coding: utf-8 -*-


class CombatMaster(object):
    def __init__(self):
        self.fighters = []
        self.battle_wheel = [[], [], [], [], [], [], []]
        self.now = 0

    def add_fighter(self, fighter):
        if fighter not in self.fighters:
            self.fighters.append(fighter)

    def get_fighters(self):
        return self.fighters

    def start_fight(self, attacker, victim, bystanders=None):
        if not bystanders:
            bystanders = []
        self.add_fighter(attacker)
        self.battle_wheel[self.now].append(attacker)
        self.enter_fight(victim)
        for character in bystanders:
            self.enter_fight(character)

    def enter_fight(self, character):
        self.add_fighter(character)
        character_initiative = character.initiative()
        if character_initiative > 0:
            self.battle_wheel[(self.now + max(6 - character_initiative, 0)) % len(self.battle_wheel)]\
                .append(character)
        else:
            self.battle_wheel[(self.now + 6) % len(self.battle_wheel)].append(character)

    def tick(self):
        for character in self.battle_wheel[self.now]:
            if character.is_alive():
                speed = character.act(self.fighters)
                self.battle_wheel[(self.now + speed) % len(self.battle_wheel)].append(character)
        self.battle_wheel[self.now] = []
        for i, character in enumerate(self.fighters):
            if not character.is_alive():
                self.fighters.pop(i)
        self.now = (self.now + 1) % len(self.battle_wheel)
