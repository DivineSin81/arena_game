from io import StringIO
import unittest
from unittest.mock import patch
from enemy import Enemy
from character import Character


class TestEnemy(unittest.TestCase):
    """Test cases for the Enemy class."""

    def setUp(self):
        """Set up a test objects before each test."""
        self.enemy = Enemy("Test Enemy", 150, 75, 0.2, 0.2, 100, 100)
        self.character = Character("Test Character", 100, 100, 50, 0.2, 0.2, 0, 1, 0, 100)

    def test_enemy_initialization(self):
        """Test initialization of an Enemy instance."""
        self.assertEqual(self.enemy.hp, 150, "Enemy hp should be set correctly")
        self.assertEqual(self.enemy.dmg, 75, "Enemy damage should be set correctly")
        self.assertEqual(self.enemy.crit_chance, 0.2, "Enemy critical chance should be set correctly")
        self.assertEqual(self.enemy.dodge_chance, 0.2, "Enemy dodge chance should be set correctly")
        self.assertEqual(self.enemy.exp, 100, "Enemy experience points reward should be set correctly")
        self.assertEqual(self.enemy.gold, 100, "Enemy gold reward should be set correctly")
        self.assertTrue(self.enemy.is_alive, "Enemy should be alive initially")
        self.assertIn(self.enemy, Enemy.all_enemies, "Enemy should be added to all_enemies")

    def test_hp_validation(self):
        """Test HP validation. Not negative."""
        self.enemy.hp = -20
        self.assertEqual(self.enemy.hp, 0, "")
        self.enemy.hp = 20
        self.assertEqual(self.enemy.hp, 20, "")
    
    def test_dmg_validation(self):
        """Test damage validation. Not negative."""
        self.enemy.dmg = -10
        self.assertEqual(self.enemy.dmg, 0, "")
        self.enemy.dmg = 10
        self.assertEqual(self.enemy.dmg,  10, "")

    def test_crit_chance_validation(self):
        """Test critical chance validation. Not negative."""
        self.enemy.crit_chance = -0.2
        self.assertEqual(self.enemy.crit_chance, 0, "")
        self.enemy.crit_chance = 0.3
        self.assertEqual(self.enemy.crit_chance, 0.3, "")

    def test_dodge_chance_validation(self):
        """Test dodge chance validation. Not negative."""
        self.enemy.dodge_chance = -0.5
        self.assertEqual(self.enemy.dodge_chance, 0, "")
        self.enemy.dodge_chance = 0.7
        self.assertEqual(self.enemy.dodge_chance, 0.7, "")

    def test_perform_attack_no_dodge_no_crit(self):
        """Test _perform_attack when no dodge and no critical hit occurs."""
        with patch('random.random', side_effect=[0.3, 0.3]), patch('sys.stdout', new=StringIO()) as fake_out:
            Enemy._perform_attack(self.character, self.enemy, "Character", "Enemy")
        output = fake_out.getvalue()
        self.assertIn("Character deals 50 damage to Enemy.", output, "Should print correct damage message")
        self.assertEqual(self.enemy.hp, 100, "Enemy HP should decrease by character's damage")

    def test_perform_attack_dodge(self):
        """Test _perform_attack when target dodges."""
        with patch('random.random', side_effect=[0.2, 0.3]), patch('sys.stdout', new=StringIO()) as fake_out:
            Enemy._perform_attack(self.character, self.enemy, "Character", "Enemy")
        output = fake_out.getvalue()
        self.assertIn("Enemy dodged Character attack", output, "Should print dodge message")
        self.assertEqual(self.enemy.hp, 150, "Enemy HP should not chance on dodge")

    def test_perform_attack_critical_hit(self):
        """Test _perform_attack with critical hit."""
        with patch('random.random', side_effect=[0.3, 0.1]), patch('sys.stdout', new=StringIO()) as fake_out:
            Enemy._perform_attack(self.character, self.enemy, "Character", "Enemy")
        output = fake_out.getvalue()
        self.assertIn("Character lands a critical hit for 75 damage on Enemy", output, "Should print critical hit message")
        self.assertEqual(self.enemy.hp, 75, "Enemy HP should decrease by critical damage")

    def test_fight_enemy_defeated(self):
        """Test fight method when character defeats the enemy."""
        enemy = Enemy("Test Enemy", 10, 5, 0, 0, 20, 10)
        with patch('random.choice', return_value=enemy), patch('random.random', side_effect=[0.3, 0.3] * 10), patch('sys.stdout', new=StringIO()) as fake_out:
            Enemy.fight(self.character)
        output = fake_out.getvalue()
        self.assertIn("You defeated the Test Enemy", output, "Should print defeat message")
        self.assertEqual(self.character.gold, 10, "Character should gain enemy gold")
        self.assertEqual(self.character.exp, 20, "Character should gain enemy experience points")

    def test_fight_character_defeated(self):
        """Test fight method when character is defeated."""
        enemy = Enemy("Test Enemy", 1000, 1000, 0, 0.2, 100, 50)
        with patch('random.choice', return_value=enemy), patch('random.random', side_effect=[0.3, 0.3] * 10), patch('sys.stdout', new=StringIO()) as fake_out:
            Enemy.fight(self.character)
        output = fake_out.getvalue()
        self.assertIn("Test Enemy deals 1000 damage to You", output, "Should print damage message")
        self.assertEqual(self.character.hp, 0, "Character hp should be 0 when defeated")

if __name__ == "__main__":
    unittest.main()