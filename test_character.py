import unittest
from character import Character
from weapon import Weapon
from armor import Armor


class TestCharacter(unittest.TestCase):
    """Test cases for the Character class."""

    def setUp(self):
        """Set up a test character and items before each test."""
        self.character = Character("Test Character", 100, 100, 50, 0.1, 0.1, 100, 1, 0, 100, None, None, [])
        self.weapon = Weapon("Test Weapon", 100, 0.2, 50, 1)
        self.armor = Armor("Test Armor", 50, 0.2, 50, 1)

    def test_hp_validation(self):
        """Test HP validation. Not negative and not over maxhp."""
        self.character.hp = -10
        self.assertEqual(self.character.hp, 0, "HP should not be negative")
        self.character.hp = 150
        self.assertEqual(self.character.hp, 100, "HP should not be exceed maxhp")
    
    def test_maxhp_validation(self):
        """Test maximum hp validation. Not negative."""
        self.character.maxhp = -20
        self.assertEqual(self.character.maxhp, 0, "Max HP should not be negative")

    def test_dmg_validation(self):
        """Test damage validation. Not negative."""
        self.character.dmg = -5
        self.assertEqual(self.character.dmg, 0, "Damage should not be negative")

    def test_crit_chance_validation(self):
        """Test critical chance validation. Not negative."""
        self.character.crit_chance = -2
        self.assertEqual(self.character.crit_chance, 0, "Critical chance should not be negative")

    def test_dodge_chance_validation(self):
        """Test dodge chance validation. Not negative."""
        self.character.dodge_chance = -2
        self.assertEqual(self.character.dodge_chance, 0, "Dodge chance should not be negative")

    def test_gold_validation(self):
        """Test gold validation. Not negative."""
        self.character.gold = -10
        self.assertEqual(self.character.gold, 0, "Gold should not be negative")

    def test_lvl_validation(self):
        """Test level validation. Not negative and not 0."""
        self.character.lvl = 0
        self.assertEqual(self.character.lvl, 1, "LvL should not be equal 0")
        self.character.lvl = -2
        self.assertEqual(self.character.lvl, 1, "Lvl should not be negative")

    def test_exp_validation(self):
        """Test experience points validation. Not negative."""
        self.character.exp = -5
        self.assertEqual(self.character.exp, 0, "Exp should not be negative")

    def test_maxexp_validation(self):
        """Test maximum experience points validation. Not negative and not 0."""
        self.character.maxexp = -8
        self.assertEqual(self.character.maxexp, 1, "Max exp should not be negative")
        self.character.maxexp = 0
        self.assertEqual(self.character.maxexp, 1, "Max exp should not be equal 0")

    def test_add_to_inventory(self):
        """Test adding an item to inventory."""
        self.character.add_to_inventory(self.weapon)
        self.assertIn(self.weapon, self.character.inventory, "Weapon should be in inventory")
        self.assertEqual(len(self.character.inventory), 1, "Inventory should contain 1 item")

    def test_equip_weapon(self):
        """Test equipping a wepon."""
        self.character.equip_item(self.weapon)
        self.assertEqual(self.character.equiped_weapon, self.weapon, "Weapon should be equiped")
        self.assertEqual(self.character.dmg, 150, "Character damage should be increased by weapon's item_dmg")
        #self.assertEqual(self.character.crit_chance, 0.3, "Character critical chance should be increased by weapon's item crit chance")

    def test_equip_armor(self):
        """Test equipping armor."""
        self.character.equip_item(self.armor)
        self.assertEqual(self.character.equiped_armor, self.armor, "Armor should be equiped")
        self.assertEqual(self.character.maxhp, 150, "Character max HP should be increased by armor's item_def")
        #self.assertEqual(self.character.dodge_chance, 0.3, "character dodge chance should be increased by armor's item_sub_stat")
    
    def test_level_up(self):
        """Test level-up functionality."""
        self.character.exp = 100
        self.assertEqual(self.character.lvl, 2, "Level should increase after reaching maxexp")
        self.assertEqual(self.character.exp, 0, "After Level-up exp should be equal 0")
        self.assertEqual(self.character.maxexp, 150, "Max exp should be multiplay by 1.5")
        self.assertEqual(self.character.maxhp, 150, "Max HP should increase after level-up")
        self.assertEqual(self.character.hp, self.character.maxhp, "Hp should be equal to maxhp after level-up")
        self.assertEqual(self.character.dmg, 70, "Damage should increase after level-up")

    def test_over_level_up(self):
        """Test level-up with excess experience."""
        self.character.exp = 150
        self.assertEqual(self.character.lvl, 2, "Level should increase after reaching maxexp")
        self.assertEqual(self.character.exp, 50, "After Level-up exp should be equal of exp over max_exp of previous lvl")
        self.assertEqual(self.character.maxexp, 150, "Max exp should be multiplay by 1.5")
        self.assertEqual(self.character.maxhp, 150, "Max HP should increase after level-up")
        self.assertEqual(self.character.hp, self.character.maxhp, "Hp should be equal to maxhp after level-up")
        self.assertEqual(self.character.dmg, 70, "Damage should increase after level-up")

if __name__ == "__main__":
    unittest.main()