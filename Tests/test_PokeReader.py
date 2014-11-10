import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../src/'))
import PokeReader
from Pokemon import Pokemon

class testPokeReader(unittest.TestCase):
    def setUp(self):
        self.entry_path = "../Entradas/Pokemons/"
        pass

    def test_read_pokemons(self):
        # Test for a signle file for every entry file
        filenames = os.listdir(self.entry_path)
        pr = PokeReader.PokeReader()
        for n in range(len(filenames)):
            tmp = open(".tmp", "w")
            for i in range(n + 1):
                f = open(self.entry_path + filenames[i], "r")
                tmp.write(f.read())
                f.close()
            tmp.close()
            PokeReader.stdin = open(".tmp", "r")
            poke_tuple = pr.read_pokemons(n + 1)
            self.assertEqual(len(poke_tuple), n + 1)
            for poke in poke_tuple:
                self.assertTrue(isinstance(poke, Pokemon))
            PokeReader.stdin.close()
        os.remove(".tmp")

if __name__ == "__main__":
    unittest.main()
