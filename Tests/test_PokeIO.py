import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Pokemon import Pokemon
from PokeIO import PokeIO
from Stats import Stats
from Move import Move
from Type import Type

class Test_PokeIO(unittest.TestCase):
	def setUp(self):
		v_stats = Stats(100, 50, 60, 70, 80)
		self.valid_poke_path = "../Entradas/aecio.pok"
		self.v_move_list = [Move("Movimento valido 1", Type.Normal, 70, 80, 10), Move("Movimento valido 2", Type.Normal, 70, 80, 10), Move("Movimento valido 3", Type.Normal, 70, 80, 10)]
		v_type_list = [Type.Normal, Type.Fighting]
		self.valid_poke = Pokemon(v_type_list, v_stats, "Validomon", 77, self.v_move_list)
		self.pokeio = PokeIO

	def test_read_poke(self):
		# Test wrong file name
		something = object()
		self.assertRaises(TypeError, self.pokeio.read_poke, self.pokeio, something)

		# Test valid parameters
		# self.assertRaises(None, self.pokeio.read_poke, self.pokeio, self.valid_poke_path)


if __name__ == '__main__':
    unittest.main()