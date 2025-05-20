from item import Item
import csv


class Weapon(Item):
    all = []

    def __init__(self, item_name, item_dmg, item_price, quantity, type):
        super().__init__(item_name, item_price, quantity, type)

        self.item_dmg = item_dmg

        Weapon.all.append(self)

    def __repr__(self):
        return f"\n{self.__class__.__name__}('{self.item_name}', {self.item_dmg}, {self.item_price}, {self.quantity})"

    @classmethod
    def from_csv(cls):
        with open('weapons.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(item_name = item.get('item_name'),
                     item_dmg = item.get('item_dmg'),
                     item_price = item.get('item_price'),
                     quantity = item.get('quantity'),
                     type = item.get('type'),)

    def test(self):
        print(Weapon.all)

#wepon1 = Weapon("Night Bringer Edge", 100, 20, 1)