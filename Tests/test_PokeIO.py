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
		self.poketest = Pokemon([Type(7),Type(8)], Stats(2, 3, 4, 5, 6), "teste", 1, [Move("atk", Type(2), 3, 4, 5)])
		self.poketest_path = "test.pok"
		v_stats = Stats(100, 50, 60, 70, 80)
		self.valid_poke_path = "../Entradas/aecio.pok"
		self.v_move_list = [Move("Movimento valido 1", Type.Normal, 70, 80, 10), Move("Movimento valido 2", Type.Normal, 70, 80, 10), Move("Movimento valido 3", Type.Normal, 70, 80, 10)]
		v_type_list = [Type.Normal, Type.Fighting]
		self.valid_poke = Pokemon(v_type_list, v_stats, "Validomon", 77, self.v_move_list)
		self.pokeio = PokeIO

	def test_read_poke(self):
		# Teste com um nome de arquivo que não é uma string
		something = object()
		self.assertRaises(TypeError, self.pokeio.read_poke, self.pokeio, something)

		# Teste se a função retorna o pokemon esperado do arquivo teste.pok
		# Esse teste verifica se todos os atributos são iguais
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).name, self.poketest.name)
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).level, self.poketest.level)
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).move_list[0].name, self.poketest.move_list[0].name)
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).move_list[0].pp, self.poketest.move_list[0].pp)
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).type_list[0], self.poketest.type_list[0])
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).type_list[1], self.poketest.type_list[1])
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).defense_force, self.poketest.defense_force)
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).spd, self.poketest.spd)
		self.assertEqual(self.pokeio.read_poke(self.pokeio, self.poketest_path).hp, self.poketest.hp)
	
	def test_read_move(self):
		# Teste com um lista de movimentos que não é uma lista de movimentos
		something = object()
		self.assertRaises(TypeError, self.pokeio.read_move, self.pokeio, something)
		somelist = [object()]
		self.assertRaises(TypeError, self.pokeio.read_move, self.pokeio, somelist)

		# Teste com uma lista de movimentos válidos
		print("Digite um inteiro entre 1 e 3")
		self.assertTrue(self.pokeio.read_move(self.pokeio, self.v_move_list) in self.v_move_list)

	def test_print_move_list(self):
		# Teste com um lista de movimentos que não é uma lista de movimentos
		something = object()
		self.assertRaises(TypeError, self.pokeio.print_move_list, self.pokeio, something)
		somelist = [object()]
		self.assertRaises(TypeError, self.pokeio.print_move_list, self.pokeio, somelist)

	def test_print_poke_info(self):
		# Teste com um pokemon que não é pokemon
		something = object()
		self.assertRaises(TypeError, self.pokeio.print_poke_info, self.pokeio, something)

if __name__ == '__main__':
    unittest.main()