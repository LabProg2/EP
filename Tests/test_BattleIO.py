import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Pokemon import Pokemon
from BattleIO import BattleIO
from Stats import Stats
from Move import Move
from movelist import MoveList
from Type import Type

class Test_BattleIO(unittest.TestCase):
    def setUp(self):
        self.valid_move1 = Move("Name1", Type.Normal, 100, 50, 50)
        self.valid_move2 = Move("Name2", Type.Normal, 100, 50, 50)
        self.valid_move3 = Move("Name3", Type.Normal, 100, 50, 50)

        self.valid_movelist = MoveList(self.valid_move1, self.valid_move2, self.valid_move3)

        self.valid_stats = Stats(100, 100, 100, 100, 100)

        self.valid_pokemon = Pokemon(name="Pokemon", level=5, moves=self.valid_movelist, type_list=Type.Normal, stats=self.valid_stats)

        self.poketest = Pokemon([Type(7),Type(8)], Stats(2, 3, 4, 5, 6), [Move("atk", Type(2), 3, 4, 5)], "teste", 1)
        self.poketest_path = "test.pok"
        v_stats = Stats(100, 50, 60, 70, 80)
        self.valid_poke_path = "../Entradas/aecio.pok"
        self.v_move_list = [Move("Movimento valido 1", Type.Normal, 70, 80, 10), Move("Movimento valido 2", Type.Normal, 70, 80, 10), Move("Movimento valido 3", Type.Normal, 70, 80, 10)]
        v_type_list = [Type.Normal, Type.Fighting]
        self.valid_poke = Pokemon(v_type_list, v_stats, self.v_move_list, "Validomon", 77)
        self.pokeio = BattleIO

    def test_read_move_of(self):
        battleio = BattleIO()
        # __builtins__.input = lambda : "1\n"
        # self.assertTrue(isinstance(battleio.read_move_of(self.valid_pokemon), Move))
        # self.assertEqual(self.valid_move1, battleio.read_move_of(self.valid_pokemon))

        # __builtins__.input = lambda : "2\n"
        # self.assertTrue(isinstance(battleio.read_move_of(self.valid_pokemon), Move))
        # self.assertEqual(self.valid_move2, battleio.read_move_of(self.valid_pokemon))

        # __builtins__.input = lambda : "3\n"
        # self.assertTrue(isinstance(battleio.read_move_of(self.valid_pokemon), Move))
        # self.assertEqual(self.valid_move3, battleio.read_move_of(self.valid_pokemon)) 

        self.assertRaises(TypeError, battleio.read_move_of, object())

    def test_print_move_list(self):
        battleio = BattleIO()
        self.assertRaises(TypeError, battleio.print_moves_of, object())

if __name__ == '__main__':
    unittest.main()