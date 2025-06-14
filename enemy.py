import random
from copy import deepcopy


class Enemy:
    all_enemies = []

    def __init__(self, name, hp, dmg, crit_chance, dodge_chance, exp, gold):
        self._name = name
        self._hp = hp
        self._dmg = dmg
        self._crit_chance = crit_chance
        self._dodge_chance = dodge_chance
        self._exp = exp
        self._gold = gold

        Enemy.all_enemies.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    @property
    def dmg(self):
        return self._dmg
    
    @property
    def crit_chance(self):
        return self._crit_chance
    
    @property
    def dodge_chance(self):
        return self._dodge_chance
    
    @property
    def exp(self):
        return self._exp
    
    @property
    def gold(self):
        return self._gold
    
    @property
    def is_alive(self):
        return self._hp > 0
    
    @staticmethod
    def _perform_attack(attacker, target, attacker_name, target_name):
        if random.random() <= target.dodge_chance:
            print(f"{target_name} dodged {attacker_name} attack")
            return
        
        if random.random() < attacker.crit_chance:
            damage = attacker.dmg * 1.5
            print(f"{attacker_name} lands a critical hit for {damage} damage on {target_name}!")
        else:
            damage = attacker.dmg
            print(f"{attacker_name} deals {damage} damage to {target_name}.")
        
        target.hp -= damage
        print(f"{target_name}'s HP: {target.hp}")

    @classmethod
    def fight(cls, character):
        enemy = deepcopy(random.choice(cls.all_enemies))
        print(f"You encounter a {enemy.name}! Your HP: {character.hp}, Enemy HP: {enemy.hp}")

        while enemy.is_alive and character.hp > 0:
            cls._perform_attack(character, enemy, "You", enemy.name)

            if enemy.is_alive:
                cls._perform_attack(enemy, character, enemy.name, "You")

        if not enemy.is_alive:
            print(f"You defeated the {enemy.name}")
            character.gold += enemy.gold
            character.exp += enemy.exp
            print(f"You gained {enemy.gold} gold and {enemy.exp} experience!")


Enemy("Goblin", 100, 20, 0.10, 0.15, 20, 20)
Enemy("Orc", 200, 50, 0.15, 0.15, 50, 50)
Enemy("Bandit", 300, 75, 0.20, 0.15, 75, 75)