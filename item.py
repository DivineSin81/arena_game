import csv

from cycler import V

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        #Validations
        assert price >= 0, f"Item {name} price {price} not >= 0"
        assert quantity >= 0, f"Item {name} quantity {quantity} not >= 0"

        #Self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def setname(self, value):
        if len(value) > 10:
            raise Exception("Too long")
        else:
            self.__name = value

    def __calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"\n{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
