import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'))

from Pokemon import Pokemon
from Stats import Stats
from Type import Type
from Move import Move
from movelist import MoveList
from pokexmler import PokeXmler

class TestPokeXmler(unittest.TestCase):
    def setUp(self):
        self.valid_pokemon = Pokemon(\
            Type.Normal, Stats(100,100,100,100,100), MoveList(Move("move1",Type.Normal,3,2,1)))

    # def test_init(self):
    #     self.assertTrue(isinstance(PokeXmler(self.valid_pokemon), PokeXmler))
    #     # só pra ver que funciona depois vou tirar:
    #     print(PokeXmler(self.valid_pokemon).tostring())

    def test_str_to_pokes(self):
        f = open('../src/tmp_poke_state.xml', 'r')
        xmlstr = f.read()

        xmler = PokeXmler()
        a = xmler.str_to_pokes(xmlstr)
        print(a[0].moves)


        f.close()

if __name__ == "__main__":
    unittest.main()
