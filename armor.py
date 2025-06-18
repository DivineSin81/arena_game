from item import Item


class Armor(Item):
    """Representants armor item with defence and dodge chance bonus."""
    all = []

    def __init__(self, item_name, item_def, item_sub_stat, item_price, quantity, type = "armor"):
        """Initialize armor with given attributes."""
        super().__init__(item_name, item_price, quantity, type)

        self._item_def = item_def
        self._item_sub_stat = item_sub_stat

        Armor.all.append(self)

    @property
    def item_def(self):
        """Get armor's defence bonus."""
        return self._item_def
    
    @item_def.setter
    def item_def(self, value):
        """Set armor's defence bonus, ensuring it stays non-negative."""
        self._item_def = max(0, value)

    @property
    def item_sub_stat(self):
        """Get armor's dodge chance bonus."""
        return self._item_sub_stat
    
    @item_sub_stat.setter
    def item_sub_stat(self, value):
        """Set armor's dodge chance bonus, ensuring it stays non-negative"""
        self._item_sub_stat = max(0, value)

    def __repr__(self):
        """Return a string representation of the armor."""
        index = Armor.all.index(self)
        return f"\n{index}  {self.__class__.__name__}('{self._item_name}', {self._item_def}, {self._item_sub_stat}, {self._item_price}, {self._quantity})"
    

Armor("Night Brinder Armor", 20, 0.1, 40, 1, "armor")
Armor("Void Armor", 100, 0.2, 50, 1, "armor")