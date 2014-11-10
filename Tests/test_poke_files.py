import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../src/'))
from Type import Type


class testPokeFiles(unittest.TestCase):
    def setUp(self):
        self.entry_path = "../Entradas/Pokemons/"

    def test_files(self):
        filenames = os.listdir(self.entry_path)

        for filename in filenames:
            f = open(self.entry_path + filename, "r")
            
            # Name
            line = f.readline()
            # Level
            try:
                int(f.readline())
            except ValueError:
                raise ValueError("Error reading level of: " + filename)
            # HP
            try:
                int(f.readline())
            except ValueError:
                raise ValueError("Error reading hp of: " + filename)
            # atk
            try:
                int(f.readline())
            except ValueError:
                raise ValueError("Error reading atk of: " + filename)
            # def
            try:
                int(f.readline())
            except ValueError:
                raise ValueError("Error reading def of: " + filename)
            # spd
            try:
                int(f.readline())
            except ValueError:
                raise ValueError("Error reading spd of: " + filename)
            # spc
            try:
                int(f.readline())
            except ValueError:
                raise ValueError("Error reading spc of: " + filename)
            # type
            try:
                Type(int(f.readline()))
                Type(int(f.readline()))
            except ValueError:
                raise ValueError("Error reading type of: " + filename)
            # n attacks
            try:
                n = int(f.readline())
            except ValueError:
                raise ValueError("Error reading number of attacks of: " + filename)
            # attack
            for _ in range(n):
                f.readline()
                # Type
                try:
                    Type(int(f.readline()))
                except ValueError:
                    raise ValueError("Error reading type of: " + filename)
                # acu
                try:
                    int(f.readline())
                except ValueError:
                    raise ValueError("Error reading accuracy of: " + filename)
                # power
                try:
                    int(f.readline())
                except ValueError:
                    raise ValueError("Error reading power of: " + filename)
                # pp
                try:
                    int(f.readline())
                except ValueError:
                    raise ValueError("Error reading pp of: " + filename)

if __name__ == "__main__":
    unittest.main()
