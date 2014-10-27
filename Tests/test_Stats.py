import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Stats import Stats 
from Type import Type
from random import randrange

class TestStats(unittest.TestCase):
    def setUp(self):
        self.valid_hp = 34
        self.valid_attack = 49
        self.valid_defense = 49
        self.valid_speed = 45
        self.valid_special = 65
        self.valid_stat = Stats(self.valid_hp, self.valid_attack, \
            self.valid_defense, self.valid_speed, self.valid_special)

    def test_attack_force(self):
        # Test for valid arguments
        level1 = 5
        level2 = 10
        self.assertEqual(self.valid_stat.attack_force(level1), (2 * level1 + 10) * self.valid_attack)
        self.assertEqual(self.valid_stat.attack_force(level2), (2 * level2 + 10) * self.valid_attack)

        # Test with absurd arguments
        self.assertRaises(ValueError, self.valid_stat.attack_force, -1)
        self.assertRaises(TypeError, self.valid_stat.attack_force, object())
        
    def test_defence_force(self):
        # Regular test
        self.assertEqual(self.valid_stat.defense_force(), self.valid_defense * 250)

    def test_critical(self):
        # Test with regular arguments
        self.assertTrue(self.valid_stat.critical(10) >= 1)

        # Test with absurd arguments
        self.assertRaises(ValueError, self.valid_stat.critical, -1)
        self.assertRaises(TypeError, self.valid_stat.critical, object())

    def test_decrease_life(self):
        # Test valid values
        for _ in range(100):
            x = randrange(self.valid_hp + 1)
            valid_stats = Stats(self.valid_hp, self.valid_attack, 
                    self.valid_defense, self.valid_speed, self.valid_special)
            valid_stats.decrease_life(x)
            self.assertEqual(valid_stats._hp, self.valid_hp - x)

        # Test crazy values
        valid_stats = Stats(self.valid_hp, self.valid_attack, \
                self.valid_defense, self.valid_speed, self.valid_special)
        valid_stats.decrease_life(self.valid_hp)
        self.assertEqual(0, valid_stats._hp)
        
        valid_stats = Stats(self.valid_hp, self.valid_attack, \
                self.valid_defense, self.valid_speed, self.valid_special)


if __name__ == '__main__':
    unittest.main()

