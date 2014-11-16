import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'))
from Pokemon import Pokemon
from Stats import Stats
from Type import Type
from Move import Move
from movelist import MoveList
from pokexmler import PokeXmler
from re import sub

class TestPokeXmler(unittest.TestCase):
    def setUp(self):
        self.valid_pokemon = Pokemon(\
            Type.Normal, Stats(100,100,100,100,100), MoveList(Move("move1",Type.Normal,3,2,1)))

        # in entrada1.xml file there's a Pikachu and a Marill
        self.valid_pikachu = Pokemon(\
            Type.Fighting, Stats(200,100,100,100,100), MoveList(Move("Thunderbolt",Type.Fighting,90,90,15), Move("Slam",Type.Flying,70,80,20)), "Pikachu", 50)

        self.valid_marill = Pokemon(\
            Type.Flying, Stats(200,100,100,100,100), MoveList(Move("Surf",Type.Flying,100,90,15), Move("Hidro Pump",Type.Flying,70,100,5)), "Marill", 50)

        
    # def test_init(self):
    #     self.assertTrue(isinstance(PokeXmler(self.valid_pokemon), PokeXmler))
    #     # só pra ver que funciona depois vou tirar:
    #     print(PokeXmler(self.valid_pokemon).tostring())

    def test_compares_pokes_to_xml(self, *pokemons):

        valid_xml = open("entrada1.xml","r").read()
        valid_xml = sub(r'\s+', '', valid_xml)  # removes \t and spaces from valid_xml

        tested_xml = PokeXmler.pokes_to_xml(self.valid_pikachu,self.valid_marill)
    
        self.assertEqual(valid_xml, tested_xml)

    # def test_str_to_pokes(self):
    #     f = open('../src/tmp_poke_state.xml', 'r')
    #     xmlstr = f.read()

    #     xmler = PokeXmler()
    #     a = xmler.str_to_pokes(xmlstr)
    #     print(a[0].moves)


    #     f.close()

if __name__ == "__main__":
    unittest.main()
