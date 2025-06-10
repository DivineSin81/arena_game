class Item:
    def __init__(self, item_name, item_price, quantity, type):
        assert item_price >= 0, f"Item {item_name} is cheaper than 0!!!"

        self._item_name = item_name
        self._item_price = item_price
        self._quantity = quantity
        self._type = type

    @property
    def item_name(self):
        return self._item_name
    
    @property
    def item_price(self):
        return self.item_price

    @item_price.setter
    def item_price(self, value):
        assert value >= 0, f"Item {self.item_name} price cannot be negative"
        self._item_price = value

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        assert value >= 0, f"Quantity of item {self.item_name} cannot be negative"
        self._quantity = value

    @property
    def type(self):
        return self._type