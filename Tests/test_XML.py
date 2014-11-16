import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'))

from src.Pokemon import Pokemon
from src.Stats import Stats
from src.Type import Type
from src.Move import Move
from src.movelist import MoveList
from src.pokexmler import pokexmler

class TestPokeXmler(unittest.TestCase):
    def setUp(self):
        self.valid_pokemon = Pokemon(\
            Type.Normal, Stats(100,100,100,100,100), MoveList(Move("move1",Type.Normal,3,2,1)))

    def test_init(self):
        self.assertTrue(isinstance(pokexmler(self.valid_pokemon), pokexmler))
        # só pra ver que funciona depois vou tirar:
        print(pokexmler(self.valid_pokemon).tostring())


    def test_PokeToXml(self):
        self.assertEqual(self.valid_pokemon.pokes_to_xml(), self.valid_pokemon)

    def test_Tree(self):
        self.assertEqual(self.valid_pokemon.tree(), self.valid_pokemon)

    def test_Tostring(self):
        self.assertTrue(self.valid_pokemon.tostring(), self.valid_pokemon)
        self.assertRaises(RuntimeError, self.valid_pokemon.tostring(), object())

    def test_SrtToPokes(self):
        self.assertRaises(TypeError, self.valid_pokemon.str_to_pokes(), self.valid_pokemon)


if __name__ == "__main__":
    unittest.main()
