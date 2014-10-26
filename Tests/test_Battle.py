import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Battle import Battle

class Test_Battle(unittest.TestCase):
    def setUp(self):
        self.valid_path1 = "../Entradas/aecio.pok"
        self.valid_path2 = "../Entradas/dilma.pok"
        self.battle = Battle(self.valid_path1, self.valid_path2)

    def test_init(self):
        a = Battle(self.valid_path1, self.valid_path2)
        path1, path2 = object(), object()
        self.assertRaises(TypeError, Battle.__init__, a, path1, path2)


if __name__ == '__main__':

    unittest.main()