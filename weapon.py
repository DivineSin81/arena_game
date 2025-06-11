from item import Item


class Weapon(Item):
    all = []

    def __init__(self, item_name, item_dmg, item_crit_chance, item_price, quantity, type = "weapon"):
        super().__init__(item_name, item_price, quantity, type)

        self._item_dmg = item_dmg
        self._item_crit_chace = item_crit_chance

        Weapon.all.append(self)

    @property
    def item_dmg(self):
        return self._item_dmg
    
    @item_dmg.setter
    def item_dmg(self, value):
        self._item_dmg = max(0, value)

    @property
    def item_crit_chance(self):
        return self._item_crit_chace
    
    @item_crit_chance.setter
    def item_crit_chance(self, value):
        self._item_crit_chace = max(0, value)

    def __repr__(self):
        index = Weapon.all.index(self)
        return f"\n{index}  {self.__class__.__name__}('{self._item_name}', {self._item_dmg}, {self._item_crit_chace}, {self._item_price}, {self._quantity})"


Weapon("Night Bringer Bow", 100, 0.2, 60, 1, "weapon")
Weapon("Night Bringer Edge", 100, 0.1, 20, 1, "weapon")