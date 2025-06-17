import game_utils


class Character:
    """Represents a player character with attributes like health, damage and equipment."""
    
    def __init__(self, name, hp, maxhp, dmg, crit_chance, dodge_chance, gold, lvl, exp, maxexp, equiped_weapon=None, equiped_armor=None, inventory=None):
        """Initialize a character with given attributes."""
        self._name = name
        self._hp = max(0, hp)
        self._maxhp = max(0, maxhp)
        self._dmg = max(0, dmg)
        self._crit_chance = max(0, crit_chance)
        self._dodge_chance = max(0, dodge_chance)
        self._gold = max(0, gold)
        self._lvl = max(1, lvl)
        self._exp = max(0, exp)
        self._maxexp = max(0, maxexp)
        self._equiped_weapon = equiped_weapon
        self._equiped_armor = equiped_armor
        self._inventory = inventory if inventory is not None else []
    
    @property
    def name(self):
        """Get the character's name."""
        return self._name
    
    @property
    def hp(self):
        """Get the character's current HP."""
        return self._hp
    
    @hp.setter
    def hp(self, value):
        """Set the character's HP, ensuring it stays within bounds."""
        self._hp = max(0, min(value, self._maxhp))
    
    @property
    def maxhp(self):
        """Get the character's maximum HP."""
        return self._maxhp
    
    @maxhp.setter
    def maxhp(self, value):
        """Set the character's maximum HP, ensuring it stays non-negative."""
        self._maxhp = max(0, value)
        if self._hp > self._maxhp:
            self._hp = self._maxhp
    
    @property
    def dmg(self):
        """Get the character's damage."""
        return self._dmg
    
    @dmg.setter
    def dmg(self, value):
        """Set the character's damage, ensuring it stays non-negative."""
        self._dmg = max(0, value)

    @property
    def crit_chance(self):
        """Get the character's critical chance."""
        return self._crit_chance
    
    @crit_chance.setter
    def crit_chance(self, value):
        """Set the character's critical chance, ensuring it stays non-negative."""
        self._crit_chance = max(0, value)

    @property
    def dodge_chance(self):
        """Get the character's dodge chance."""
        return self._dodge_chance
    
    @dodge_chance.setter
    def dodge_chance(self, value):
        """Set the character's dodge chance, ensuring it stays non-negative."""
        self._dodge_chance = max(0, value)
    
    @property
    def gold(self):
        """Get the character's current gold."""
        return self._gold
    
    @gold.setter
    def gold(self, value):
        """Set the character's gold, ensuring it stays non-negative."""
        self._gold = max(0, value)
    
    @property
    def lvl(self):
        """Get the character's level."""
        return self._lvl
    
    @lvl.setter
    def lvl(self, value):
        """Set the character's level, ensuring it stays at least 1."""
        self._lvl = max(1, value)
    
    @property
    def exp(self):
        """Get the character's current experience points."""
        return self._exp
    
    @exp.setter
    def exp(self, value):
        """Set the character's experience points and handle level-up."""
        self._exp = max(0, value)
        while self._exp >= self._maxexp:
            self.level_up()
    
    @property
    def maxexp(self):
        """Get the character's maximum experience points needed to level-up."""
        return self._maxexp
    
    @maxexp.setter
    def maxexp(self, value):
        """Set the character's maximum experience points, ensuring it stays at least 1."""
        self._maxexp = max(1, value)

    @property
    def equiped_weapon(self):
        """Get the character's currenty equipped weapon."""
        return self._equiped_weapon

    @property
    def equiped_armor(self):
        """Get the character's currenty equipped armor."""
        return self._equiped_armor
    
    @property
    def inventory(self):
        """Get the character's inventory."""
        return self._inventory
    
    def add_to_inventory(self, item):
        """Add an item to the character's inventory."""
        self._inventory.append(item)
        print(f"Added {item.item_name} to inventory")

    def equip_item(self, item):
        """Equip an item, applying its stats."""
        if item.type == "weapon":
            if self._equiped_weapon:
                self._dmg -= self._equiped_weapon.item_dmg
                self._crit_chance -= self._equiped_weapon.item_crit_chance
            self._equiped_weapon = item
            self._dmg += item.item_dmg
            self._crit_chance += item.item_crit_chance
            print(f"Equipped {item.item_name}. Damage: {self._dmg}, Crit chance: {self.crit_chance * 100}%")
        elif item.type == "armor":
            if self._equiped_armor:
                self._maxhp -= self._equiped_armor.item_def
                self._dodge_chance -= self._equiped_armor.item_sub_stat
            self._equiped_armor = item
            self._maxhp += item.item_def
            self._dodge_chance += item.item_sub_stat
            print(f"Equipped {item.item_name}. Max HP: {self._maxhp}, Dodge/Block chance: {self.dodge_chance * 100}%.")

    def level_up(self):
        """Level up the character, increasing stats."""
        self._lvl += 1
        self._exp -= self._maxexp
        self._maxexp = int(self._maxexp * 1.5)
        self._maxhp += 50
        self._hp = self._maxhp
        self._dmg += 20
        print(f"Level Up! You are now level {self._lvl}. Max HP: {self._maxhp}, DMG: {self._dmg}")

    def __str__(self):
        """Return a string representation of the character's stats."""
        return ("===========\n"
                f"class {self._name}\n"
                f"hp {self._hp}\n"
                f"maxhp {self._maxhp}\n"
                f"dmg {self._dmg}\n"
                f"crit chance {self._crit_chance * 100}%\n"
                f"{'Block chance' if self.name == 'Warrior' else 'Dodge chance'} {self._dodge_chance * 100}%\n"
                f"gold {self._gold}\n"
                f"lvl {self._lvl}\n"
                f"exp {self._exp}\n"
                f"maxexp {self._maxexp}\n"
                f"equiped weapon {self._equiped_weapon.item_name if self._equiped_weapon else None}\n"
                f"equiped armor {self._equiped_armor.item_name if self._equiped_armor else None}\n"
                "===========")
    
    @staticmethod
    def select_class():
        """Prompt the user to select a character class."""
        print("Hello!\nChoose your class:\n[1] Warrior\n[2] Archer")
        select_class = game_utils.get_valid_input("Choose your class: ", [1, 2])
        if select_class == 1:
            return Character("Warrior", 250, 250, 100, 0.10, 0.10, 0, 1, 0, 100)
        elif select_class == 2:
            return Character("Archer", 150, 150, 200, 0.15, 0.15, 60, 1, 0, 100)