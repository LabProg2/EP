import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../src/'));
from Pokemon import Pokemon
from Stats import Stats
from Type import Type
from Move import Move
from movelist import MoveList

class testPokemon(unittest.TestCase):
    def setUp(self):
        self.valid_pokemon1 = Pokemon([Type(7),Type(8)], Stats(2, 3, 4, 5, 6), [Move("atk", Type(2), 100, 30, 5), Move("atk", Type(2), 100, 30, 100)], "teste", 5)
        self.valid_pokemon2 = Pokemon([Type(3),Type(4)], Stats(10, 11, 3, 13, 14), [Move("atk", Type(1), 7, 8, 9)], "NameTest2", 1)

        self.valid_type_list = [Type(7),Type(8)]
        self.valid_stats = Stats(10, 3, 4, 5, 6)
        self.valid_name = "NameTest"
        self.valid_level = 5
        self.valid_move = [Move("atk", Type(2), 100, 30, 5), Move("atk2", Type(2), 100, 30, 100)]
        self.valid_movelist = MoveList([Move("atk", Type(2), 100, 30, 5), Move("atk2", Type(2), 100, 30, 100)])
        pass

    def test_is_alive(self):
        # Test regular use of function
        self.assertTrue(self.valid_pokemon1.is_alive())
        dead_pokemon = Pokemon([Type(7),Type(8)], Stats(0, 3, 4, 5, 6), [Move("atk", Type(2), 100, 30, 5)], "teste", 5)
        self.assertFalse(dead_pokemon.is_alive())

    def test_perform_move(self):
        # Test for a regular damage
        damage = self.valid_pokemon1.perform_move(self.valid_pokemon1.moves.get_move(0), self.valid_pokemon2)
        self.assertTrue(damage >= 0)
        self.assertTrue(type(damage) is int)
        
        # Test absurd parameters
        self.assertRaises(TypeError, self.valid_pokemon1.perform_move, self.valid_pokemon1, object(), self.valid_pokemon2)
        self.assertRaises(TypeError, self.valid_pokemon1.perform_move, self.valid_pokemon1, self.valid_pokemon1.moves.get_move(0), object())


    def test_compare_types_to(self):
        # Test valid entries
        self.assertEqual(self.valid_pokemon1.compare_types_to(self.valid_pokemon2), 2)
        self.assertEqual(self.valid_pokemon1.compare_types_to(self.valid_pokemon1), 1)
        self.assertEqual(self.valid_pokemon2.compare_types_to(self.valid_pokemon1), 0.5)

        # Test exceptions
        self.assertRaises(TypeError, self.valid_pokemon1.compare_types_to, self.valid_pokemon1, object())

    def test_receive_damage(self):
        # Test regular use of the function
        self.valid_pokemon2.receive_damage(5)
        self.assertEqual(self.valid_pokemon2.hp, 5)
        self.valid_pokemon2.receive_damage(0)
        self.assertEqual(self.valid_pokemon2.hp, 5)

        # Test absurds
        self.assertRaises(TypeError, self.valid_pokemon1.receive_damage, object())        
        self.assertRaises(ValueError, self.valid_pokemon1.receive_damage, -100)    

    def test_best_move(self):
        # Test regular use of the function
        self.assertEqual(self.valid_pokemon1.perform_move(self.valid_movelist.get_move(1), self.valid_pokemon2), self.valid_pokemon1.perform_move(self.valid_pokemon1.best_move(self.valid_pokemon2), self.valid_pokemon2))

if __name__ == '__main__':
    unittest.main()