import unittest
from weapon import Weapon


class TestWeapon(unittest.TestCase):
    """Test cases for a Weapon class."""

    def setUp(self):
        """Set up a test weapon before each test."""
        self.weapon = Weapon("Test weapon", 10, 0.2, 25, 1)

    def test_item_damage_validation(self):
        """Test weapon damage validation."""
        self.weapon.item_dmg = -5
        self.assertEqual(self.weapon.item_dmg, 0, "Weapon damage should not be negative")
        self.weapon.item_dmg = 10
        self.assertEqual(self.weapon.item_dmg, 10, "Weapon damage should be set correctly")

    def test_item_crit_chance_validation(self):
        """Test weapon critical chance validation."""
        self.weapon.item_crit_chance = -0.2
        self.assertEqual(self.weapon.item_crit_chance, 0, "Weapon critical chance should not be negative")
        self.weapon.item_crit_chance = 0.5
        self.assertEqual(self.weapon.item_crit_chance, 0.5, "Weapon critical chance should be set correctly")

    def test_init_negative_values(self):
        """Test initialization with negative values."""
        weapon = Weapon("Test weapon", -2, -0.3, -5, -2)
        self.assertEqual(weapon.item_dmg, 0, "Initial weapon damage should not be negative")
        self.assertEqual(weapon.item_crit_chance, 0, "Initial weapon critical chance should not be negative")
        self.assertEqual(weapon.item_price, 0, "Initial weapon price should not be negative")
        self.assertEqual(weapon.quantity, 0, "Initial weapon quantity should not be negative")

if __name__ == "__main__":
    unittest.main()