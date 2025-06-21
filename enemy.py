import random
from copy import deepcopy


class Enemy:
    """Represents an enemy in the game with attributes like health, damage and fight system"""
    all_enemies = []

    def __init__(self, name, hp, dmg, crit_chance, dodge_chance, exp, gold):
        """Initialize an enemy with given attributes."""
        self._name = name
        self._hp = max(0, hp)
        self._dmg = max(0, dmg)
        self._crit_chance = max(0, crit_chance)
        self._dodge_chance = max(0, dodge_chance)
        self._exp = max(0, exp)
        self._gold = max(0, gold)

        Enemy.all_enemies.append(self)

    @property
    def name(self):
        """Get the enemy's name."""
        return self._name
    
    @property
    def hp(self):
        """Get the enemy's current HP."""
        return self._hp
    
    @hp.setter
    def hp(self, value):
        """Set the enemy's HP, ensuring it stays non-negative."""
        self._hp = max(0, value)

    @property
    def dmg(self):
        """Get the enemy's damage."""
        return self._dmg
    
    @dmg.setter
    def dmg(self, value):
        """Set the enemy's dmg, ensuring it stays non-negative."""
        self._dmg = max(0, value)
    
    @property
    def crit_chance(self):
        """Get the enemy's critical chance."""
        return self._crit_chance
    
    @crit_chance.setter
    def crit_chance(self, value):
        """Set the enemy's crit_chance, ensuring it stays non-negative."""
        self._crit_chance = max(0, value)
    
    @property
    def dodge_chance(self):
        """Get the enemy's dodge chance."""
        return self._dodge_chance
    
    @dodge_chance.setter
    def dodge_chance(self, value):
        """Set the enemy's dodge_chance, ensuring it stays non-negative."""
        self._dodge_chance = max(0, value)
    
    @property
    def exp(self):
        """Get the experience points awarded for defeating the enemy."""
        return self._exp
    
    @property
    def gold(self):
        """Get the gold awarded for defeating the enemy."""
        return self._gold
    
    @property
    def is_alive(self):
        """Check if enemy is still alive."""
        return self._hp > 0
    
    @staticmethod
    def _perform_attack(attacker, target, attacker_name, target_name):
        """Perform an attack, handling dodge and critical damage"""
        if random.random() <= target.dodge_chance:
            print(f"{target_name} dodged {attacker_name} attack")
            return
        
        if random.random() < attacker.crit_chance:
            damage = int(attacker.dmg * 1.5)
            print(f"{attacker_name} lands a critical hit for {damage} damage on {target_name}!")
        else:
            damage = attacker.dmg
            print(f"{attacker_name} deals {damage} damage to {target_name}.")
        
        target.hp -= damage
        print(f"{target_name}'s HP: {target.hp}")

    @classmethod
    def fight(cls, character):
        """Simulate a fight between the character and a random enemy."""
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