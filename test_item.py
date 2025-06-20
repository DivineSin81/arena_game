import unittest
from item import Item


class TestItem(unittest.TestCase):
    """Test cases for the Item class."""

    def setUp(self):
        """Set up a test item before each test."""
        self.item = Item("Test Item", 50, 1, "Test")

    def test_item_price_validation(self):
        """Test item price validation."""
        self.item.item_price = -10
        self.assertEqual(self.item.item_price, 0, "Item price should not be negative")
        self.item.item_price = 100
        self.assertEqual(self.item.item_price, 100, "Item price should be set correctly")

    def test_quantity_validation(self):
        """Test item quantity validation."""
        self.item.quantity = -5
        self.assertEqual(self.item.quantity, 0, "Item price should not be negative")
        self.item.quantity = 5
        self.assertEqual(self.item.quantity, 5, "Item price should be set correctly")

    def test_init_negative_values(self):
        """Test initialization with negative values."""
        item = Item("Test Item", -20, -3, "Test")
        self.assertEqual(item.item_price, 0, "Initial item price should not be negative")
        self.assertEqual(item.item_price, 0, "Initial item quantity should not be negative")

if __name__ == "__main__":
    unittest.main()