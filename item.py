class Item:
    """Represents a generic item in the game with attributes like name, price and quantity."""

    def __init__(self, item_name, item_price, quantity, type):
        """Initialize an item with given attributes."""
        self._item_name = item_name
        self._item_price = max(0, item_price)
        self._quantity = max(0, quantity)
        self._type = type

    @property
    def item_name(self):
        """Get the item's name."""
        return self._item_name
    
    @property
    def item_price(self):
        """Get the item's price."""
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        "Set the item's price, ensuring it stays non-negative."
        self._item_price = max(0, value)

    @property
    def quantity(self):
        """Get the item's quantity."""
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        """Set the item's quantity, ensuring it stays non-negative."""
        self._quantity = max(0, value)

    @property
    def type(self):
        """Get the item's type."""
        return self._type