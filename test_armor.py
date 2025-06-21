import unittest
from armor import Armor


class TestArmor(unittest.TestCase):
    """Test cases for Armor class."""

    def setUp(self):
        """Set up a test armor before each test."""
        self.armor = Armor("Test Armor", 20, 0.2, 15, 1)

    def test_item_def_validation(self):
        """Test armor defence validation."""
        self.armor.item_def = -5
        self.assertEqual(self.armor.item_def, 0, "Armor defence should not be negative")
        self.armor.item_def = 10
        self.assertEqual(self.armor.item_def, 10, "Armor defence should be set correctly")

    def test_item_sub_stat_validation(self):
        """Test armor dodge chance validation."""
        self.armor.item_sub_stat = -0.2
        self.assertEqual(self.armor.item_sub_stat, 0, "Armor dodge chance should not be negative")
        self.armor.item_sub_stat = 0.3
        self.assertEqual(self.armor.item_sub_stat, 0.3, "Armor dodge chance should be set correctly")

    def test_init_negative_values(self):
        """Test initialization with negative values."""
        armor = Armor("Test Armor", -2, -0.3, -10, -2)
        self.assertEqual(armor.item_def, 0, "Initial armor defence should not be negative")
        self.assertEqual(armor.item_sub_stat, 0, "Initial armor dodge chance should not be negative")
        self.assertEqual(armor.item_price, 0, "Initial armor price should not be negative")
        self.assertEqual(armor.quantity, 0, "Initial armor quantity should not be negative")

if __name__ == "__main__":
    unittest.main()