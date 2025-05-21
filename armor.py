from item import Item

class Armor(Item):
    all = []

    def __init__(self, item_name, item_def, item_price, quantity, type = "armor"):
        super().__init__(item_name, item_price, quantity, type)

        self.item_def = item_def

        Armor.all.append(self)

    def __repr__(self):
        index = Armor.all.index(self)
        return f"\n{index}  {self.__class__.__name__}('{self.item_name}', {self.item_def}, {self.item_price}, {self.quantity})"
    

armor1 = Armor("Night Brinder Armor", 20, 40, 1, "armor")
armor2 = Armor("Void Armor", 100, 50, 1, "armor")