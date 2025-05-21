class Item:
    def __init__(self, item_name, item_price, quantity, type):
        assert item_price >= 0, f"Item {item_name} is cheaper than 0!!!"

        self.item_name = item_name
        self.item_price = item_price
        self.quantity = quantity
        self.type = type

    def shop(self, item):
        if item.type == "weapon":
            if self.gold >= item.item_price:
                self.dmg += item.item_dmg
                self.gold -= item.item_price
                print(f"You bought {item.item_name}")
            else:
                print("Sorry, you don't have enought money")
        elif type == "armor":
            pass