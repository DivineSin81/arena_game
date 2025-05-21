from item import Item

class Weapon(Item):
    all = []

    def __init__(self, item_name, item_dmg, item_price, quantity, type = "weapon"):
        super().__init__(item_name, item_price, quantity, type)

        self.item_dmg = item_dmg

        Weapon.all.append(self)

    def __repr__(self):
        index = Weapon.all.index(self)
        return f"\n{index}  {self.__class__.__name__}('{self.item_name}', {self.item_dmg}, {self.item_price}, {self.quantity})"


wepon1 = Weapon("Night Bringer Bow", 100, 20, 1, "weapon")
wepon2 = Weapon("Night Bringer Edge", 100, 20, 1, "weapon")