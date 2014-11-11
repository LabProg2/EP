import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../src/'))
from movelist import MoveList
from Move import Move
from Type import Type

class TestMoveList(unittest.TestCase):
    def setUp(self):
        self.valid_move = Move("Name", Type.Normal, 100, 50, 50)
        pass

    def test_init(self):
        # Test normally
        self.assertTrue(isinstance(MoveList(self.valid_move), MoveList))

if __name__ == "__main__":
    unittest.main()
