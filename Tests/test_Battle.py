import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Battle import Battle
from Pokemon import Pokemon
from Stats import Stats
from Move import Move
from Type import Type

class Test_Battle(unittest.TestCase):
    def setUp(self):
        self.valid_pokemon = Pokemon([Type(7),Type(8)], Stats(2, 3, 4, 5, 6), [Move("atk", Type(2), 3, 4, 5)], "teste", 1)
        self.valid_battle = Battle(self.valid_pokemon, self.valid_pokemon)

    def test_init(self):
        obj1, obj2 = object(), object()
        self.assertRaises(TypeError, Battle.__init__, self.valid_battle, obj1, obj2)
        self.assertRaises(TypeError, Battle.__init__, self.valid_battle, obj1, self.valid_pokemon)
        self.assertRaises(TypeError, Battle.__init__, self.valid_battle, self.valid_pokemon, obj2)


if __name__ == '__main__':

    unittest.main()