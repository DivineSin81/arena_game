from io import StringIO
import unittest
from character import Character
from armor import Armor
from shop import select_shop, shop_menu
from weapon import Weapon
from unittest.mock import patch


class TestShop(unittest.TestCase):
    """Test cases for all shop functions."""

    def setUp(self):
        """Set up test objects before each test."""
        self.character = Character("Test Character", 100, 100, 50, 0.2, 0.2, 100, 1, 0, 100)
        self.armor = Armor("Test Armor", 10, 0.05, 50, 2)
        self.weapon = Weapon("Test Weapon", 15, 0.05, 75, 1)
        self.original_armor_all = Armor.all
        self.original_weapon_all = Weapon.all
        Armor.all = [self.armor]
        Weapon.all = [self.weapon]

    def tearDown(self):
        """Clean up after each test."""
        Armor.all = self.original_armor_all
        Weapon.all = self.original_weapon_all

    def test_select_shop_armor(self):
        """Test select_shop when choosing Armor Shop."""
        with patch('game_utils.get_valid_input', return_value=1), patch('shop.shop_menu') as mock_shop_menu, patch('sys.stdout', new=StringIO()) as fake_out:
            select_shop(self.character)
        output = fake_out.getvalue()
        self.assertIn("Do you want to better protect yourself or deal more dmg?", output)
        mock_shop_menu.assert_called_once_with(self.character, "armor", Armor.all)

    def test_select_shop_weapon(self):
        """Test select_shop when choosing Weapon Shop."""
        with patch('game_utils.get_valid_input', return_value=2), patch('shop.shop_menu') as mock_shop_menu, patch('sys.stdout', new=StringIO()) as fake_out:
            select_shop(self.character)
        output = fake_out.getvalue()
        self.assertIn("Do you want to better protect yourself or deal more dmg?", output)
        mock_shop_menu.assert_called_once_with(self.character, "weapon", Weapon.all)

    def test_select_shop_exit(self):
        """Test select_shop when choosing Exit."""
        with patch('game_utils.get_valid_input', return_value=0), patch('shop.shop_menu') as mock_shop_menu, patch('sys.stdout', new=StringIO()) as fake_out:
            select_shop(self.character)
        output = fake_out.getvalue()
        self.assertIn("Do you want to better protect yourself or deal more dmg?", output)
        mock_shop_menu.assert_not_called()

    def test_select_shop_invalid_selection(self):
        """Test select_shop with invalid selection."""
        with patch('game_utils.get_valid_input', side_effect=ValueError), patch('shop.shop_menu') as mock_shop_menu, patch('sys.stdout', new=StringIO()) as fake_out:
            select_shop(self.character)
        output = fake_out.getvalue()
        self.assertIn("Invalid Selection.", output, "Shoul print invalid selection message")

    def test_shop_menu_no_items(self):
        """Test shop_menu when no items are available."""
        Armor.all = []
        with patch('sys.stdout', new=StringIO()) as fake_out:
            shop_menu(self.character, "armor", Armor.all)
        output = fake_out.getvalue()
        self.assertIn("No armors available right now.", output, "Should print no items message")
        self.assertEqual(self.character.gold, 100, "Gold should not change")

    def test_shop_menu_armor_purchase(self):
        """Test shop_menu when purchasing an armor."""
        with patch('game_utils.get_valid_input', return_value=0), patch('sys.stdout', new=StringIO()) as fakeout:
            shop_menu(self.character, "armor", Armor.all)
        output = fakeout.getvalue()
        self.assertIn("Welcome to the Armor Shop!", output)
        self.assertIn("[0] Test Armor - DEF: 10, Dodge/Block chance: 5.0%, Price: 50", output)
        self.assertIn("You bought Test Armor! Your max HP increased to 110", output)
        self.assertEqual(self.character.gold, 50, "Gold should decrease to 50")
        self.assertEqual(self.character.maxhp, 110, "Max HP should increase by armor's item_def")
        self.assertEqual(self.character.dodge_chance, 0.25, "Dodge chance should increase by item_sub_stat")
        self.assertEqual(self.armor.quantity, 1, "Armor quantity should decrease to 1")
        self.assertIn(self.armor, self.character._inventory, "Armor should be in inventory")
        self.assertEqual(self.character._equiped_armor, self.armor, "Armor should be equipped")

    def test_shop_menu_weapon_purchase(self):
        """Test shop_menu when purchasing an weapon."""
        with patch('game_utils.get_valid_input', return_value=0), patch('sys.stdout', new=StringIO()) as fakeout:
            shop_menu(self.character, "weapon", Weapon.all)
        output = fakeout.getvalue()
        self.assertIn("Welcome to the Weapon Shop!", output)
        self.assertIn("[0] Test Weapon - DMG: 15, Crit chance: 5.0%, Price: 75", output)
        self.assertIn("You bought Test Weapon! Your dmg increased to 65", output)
        self.assertEqual(self.character.gold, 25, "Gold should decrease to 25")
        self.assertEqual(self.character.dmg, 65, "Max HP should increase by weapon's item_dmg")
        self.assertEqual(self.character.crit_chance, 0.25, "Dodge chance should increase by item_crit_chance")
        self.assertEqual(self.weapon.quantity, 0, "Armor quantity should decrease to 0")
        self.assertIn(self.weapon, self.character._inventory, "Weapon should be in inventory")
        self.assertEqual(self.character._equiped_weapon, self.weapon, "Weapon should be equipped")

    def test_shop_menu_insufficient_gold(self):
        """Test shop_menu when character has insufficient gold."""
        self.character.gold = 10
        with patch('game_utils.get_valid_input', return_value=0), patch('sys.stdout', new=StringIO()) as fakeout:
            shop_menu(self.character, "armor", Armor.all)
        output = fakeout.getvalue()
        self.assertIn("Not enough gold!", output, "Should print insufficient gold message")
        self.assertEqual(self.character.gold, 10, "Gold should not change")
        self.assertEqual(self.armor.quantity, 2, "Armor quantity should not change")
        self.assertNotIn(self.armor, self.character._inventory, "Armor should not be in inventory")

    def test_shop_menu_cancel_purchase(self):
        """Test shop_menu when purchase is cancelled."""
        with patch('game_utils.get_valid_input', return_value=-1), patch('sys.stdout', new=StringIO()) as fakeout:
            shop_menu(self.character, "weapon", Weapon.all)
        output = fakeout.getvalue()
        self.assertIn("You left the shop.", output, "Should print cancel message")
        self.assertEqual(self.character.gold, 100, "Gold should not change")
        self.assertEqual(self.weapon.quantity, 1, "Weapon quantity should not chance")
        self.assertNotIn(self.weapon, self.character._inventory, "Weapon should not be in inventory")

if __name__ == "__main__":
    unittest.main()