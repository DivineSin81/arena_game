from item import Item

class Weapon(Item):
    all = []

    def __init__(self, item_name, item_dmg, item_price, quantity, type = "weapon"):
        super().__init__(item_name, item_price, quantity, type)

        self._item_dmg = item_dmg

        Weapon.all.append(self)

    @property
    def item_dmg(self):
        return self._item_dmg
    
    @item_dmg.setter
    def item_dmg(self, value):
        self._item_dmg = max(0, value)

    def __repr__(self):
        index = Weapon.all.index(self)
        return f"\n{index}  {self.__class__.__name__}('{self.item_name}', {self.item_dmg}, {self.item_price}, {self.quantity})"


weapon1 = Weapon("Night Bringer Bow", 100, 20, 1, "weapon")
weapon2 = Weapon("Night Bringer Edge", 100, 20, 1, "weapon")