import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('../src/'));
from src.Pokemon import Pokemon
from src.Stats import Stats
from src.Type import Type
from src.Move import Move

class testPokemon(unittest.TestCase):
    def setUp(self):
        self.valid_pokemon1 = Pokemon([Type(7), Type(8)], Stats(10, 3, 4, 5, 6), "NameTest", 5, [Move("atk", Type(2), 100, 30, 5)])
        self.valid_pokemon2 = Pokemon([Type(3), Type(4)], Stats(10, 11, 3, 13, 14), "NameTest2", 1, [Move("atk", Type(1), 7, 8, 9)])

        self.valid_type_list = [Type(7),Type(8)]
        self.valid_stats = Stats(10, 3, 4, 5, 6)
        self.valid_name = "NameTest"
        self.valid_level = 5
        self.valid_move = [Move("atk", Type(2), 100, 30, 5)]
        pass

    def test_is_alive(self):

        self.assertTrue(Pokemon.is_alive(self.valid_stats.hp))

        self.valid_stats.hp = 0
        self.assertFalse(Pokemon.is_alive(self.valid_stats.hp))

        self.valid_stats.hp = -10
        self.assertFalse(Pokemon.is_alive(self.valid_stats.hp))

    def test_perform_move(self):
       
        #Test for a valid damage

        self.assertAlmostEqual(Pokemon.perform_move(self.valid_move, self.valid_pokemon2), 10, 2)

        # compare_modifier = 1 * 1 * 2 * 2 = 4
        # move.stab() = 1
        # critical() = if is a critical 7 / 6 = 1.167 , else 1
        # attack_force = (2 * 5 + 10) * 3 = 60
        # move.power = 30
        # valid_pokemon2.defense_force = 250 * 3 = 750
        # minimum damage = 4 * 60 * 30 * 0.85 / 750 = 8.16
        # maximum damage = 4 * 60 * 30 * 1 * 1.167 / 750 = 11.2

        #Test if the moves fails for move.accuracy = 0
        self.valid_move = [Move("atk", Type(2), 0, 30, 5)]

        self.assertEqual(Pokemon.perform_move(self.valid_move,self.valid_pokemon2), 0)

    def test_compare_types_to(self):

        self.assertEqual(self.compare_types_to(self.valid_pokemon2),4)

        self.valid_pokemon1 = Pokemon([Type(1000),Type(8)], Stats(2, 3, 4, 5, 6), "NameTest", 5 ,[Move("atk", Type(2), 100, 30, 5)])
        self.assertRaises(ValueError, self.compare_types_to, self, self.valid_pokemon2)

        self.valid_pokemon1 = Pokemon([Type(7),Type(1000)], Stats(2, 3, 4, 5, 6), "NameTest", 5 ,[Move("atk", Type(2), 100, 30, 5)])
        self.assertRaises(ValueError, self.compare_types_to, self, self.valid_pokemon2)

        self.valid_pokemon2 = Pokemon([Type(-10),Type(4)], Stats(10, 11, 3, 13, 14), "NameTest2", 1 ,[Move("atk", Type(1), 7, 8, 9)])
        self.assertRaises(ValueError, self.compare_types_to, self, self.valid_pokemon2)

        self.valid_pokemon2 = Pokemon([Type(2),Type(10000)], Stats(10, 11, 3, 13, 14), "NameTest2", 1 ,[Move("atk", Type(1), 7, 8, 9)])
        self.assertRaises(ValueError, self.compare_types_to, self, self.valid_pokemon2)


    def test_receive_damage(self):
        self.valid_pokemon1.receive_damage(3)
        self.assertEqual(Stats.hp, 7)

        self.assertRaises(ValueError, self.valid_pokemon1.receive_damage, self, 1.23)

        self.assertRaises(ValueError, self.valid_pokemon1.receive_damage, self, -100)

if __name__ == '__main__':
    unittest.main()