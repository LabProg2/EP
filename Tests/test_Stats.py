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
        pass

    def test_decrease_life(self):
        # Test valid values
        for _ in range(100):
            x = randrange(self.valid_hp + 1)
            valid_stats = Stats(self.valid_hp, self.valid_attack, \
                    self.valid_defense, self.valid_speed, self.valid_special)
            valid_stats.decrease_life(x)
            self.assertEquals(valid_stats._hp, self.valid_hp - x)

        # Test crazy values
        valid_stats = Stats(self.valid_hp, self.valid_attack, \
                self.valid_defense, self.valid_speed, self.valid_special)
        valid_stats.decrease_life(self.valid_hp)
        self.assertEquals(0, valid_stats._hp)
        
        valid_stats = Stats(self.valid_hp, self.valid_attack, \
                self.valid_defense, self.valid_speed, self.valid_special)



        

