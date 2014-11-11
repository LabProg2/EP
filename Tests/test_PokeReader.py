import unittest
import sys
import os
from random import choice
sys.path.insert(0, os.path.abspath('../src/'))
import PokeReader
from Pokemon import Pokemon

class testPokeReader(unittest.TestCase):
    def setUp(self):
        self.entry_path = "../Entradas/Pokemons/"
        self.valid_entries = ["Name", 5, 45, 50, 50, 50, 50, 1, 2, 1, \
                "Name", 3, 100, 20, 25]

    def test_read_pokemons(self):
        # Test for for x random entry files in entry_path
        filenames = os.listdir(self.entry_path)
        pr = PokeReader.PokeReader()
        for n in range(len(filenames)): 
            tmp = open(".tmp", "w")
            for _ in range(n + 1):
                f = open(self.entry_path + filenames[n], "r")
                #f = open(self.entry_path + "Pikachu.pok", "r")
                tmp.write(f.read())
                f.close()
            tmp.close()
            PokeReader.stdin = open(".tmp", "r")
            poke_tuple = pr.read_pokemons(n = n + 1)
            self.assertEqual(len(poke_tuple), n + 1)
            for poke in poke_tuple:
                self.assertTrue(isinstance(poke, Pokemon))
            PokeReader.stdin.close()
        os.remove(".tmp")

        # Test arguments
        pr = PokeReader.PokeReader()
        PokeReader.stdin = self.open_valid_file(entries = self.valid_entries)
        poke_tuple = pr.read_pokemons(1)
        self.assertEqual(len(poke_tuple), 1)
        self.assertTrue(isinstance(poke_tuple[0], Pokemon))
        self.close_valid_file(PokeReader.stdin)

        PokeReader.stdin = self.open_valid_file(entries = self.valid_entries)
        poke_tuple = pr.read_pokemons(n = 1)
        self.assertEqual(len(poke_tuple), 1)
        self.assertTrue(isinstance(poke_tuple[0], Pokemon))
        self.close_valid_file(PokeReader.stdin)
        
        
        PokeReader.stdin = self.open_valid_file(entries = self.valid_entries, repeat = 2)
        poke_tuple = pr.read_pokemons()
        self.assertEqual(len(poke_tuple), 2)
        self.assertTrue(isinstance(poke_tuple[0], Pokemon))
        self.assertTrue(isinstance(poke_tuple[1], Pokemon))
        self.close_valid_file(PokeReader.stdin)

        # Test wrong files

        
    def open_valid_file(self, entries, repeat = 1):
        ''' 
        Generates a file with the entries from the list 'entries'
        repeated 'repeat' times.
        By default 'repeat' is 1
        '''
        if not isinstance(entries, list):
            raise TypeError("entires must be a list")

        f = open(".valid_file", "w")
        for _ in range(repeat):
            for stat in entries:
                f.write(str(stat) + "\n")
        f.close()

        return open(".valid_file", "r")

    def close_valid_file(self, valid_file):
        valid_file.close()
        os.remove(".valid_file")

if __name__ == "__main__":
    unittest.main()
