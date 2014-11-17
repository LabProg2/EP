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

    def test_init(self):
        # Test normally
        self.assertTrue(isinstance(MoveList(self.valid_move), MoveList))

        
        # Test init with MoveList instance
        ml = MoveList(self.valid_move, self.valid_move)
        self.assertTrue(isinstance(MoveList(ml), MoveList))

        # Test init with list
        l = [self.valid_move, self.valid_move, self.valid_move]
        self.assertTrue(isinstance(MoveList(l), MoveList))

        # Test mixed
        self.assertTrue(isinstance(MoveList(ml, l, self.valid_move), MoveList))

        # Test empty
        self.assertTrue(isinstance(MoveList(), MoveList))
        

    def test_iterator(self):
        ml = MoveList(self.valid_move, self.valid_move, self.valid_move)
        for move in ml:
            self.assertTrue(isinstance(move, Move))

    def test_add_move(self):
        for maxi in range(20):
            ml = MoveList(max_moves=maxi)
            for _ in range(maxi):
                ml.add_move(self.valid_move)
            self.assertRaises(OverflowError, ml.add_move, self.valid_move)

    def test_get_move(self):
        ml = MoveList(self.valid_move, self.valid_move, self.valid_move)
        self.assertTrue(isinstance(ml.get_move(1), Move))

    def test_get_move_id(self):
        ml = MoveList(self.valid_move, self.valid_move, self.valid_move)
        # print("AQUI: " + str(ml.get_move_id(self.valid_move)))

    def test_is_move_available(self):
        ml = MoveList(self.valid_move, self.valid_move, self.valid_move)
        self.assertTrue(ml.is_move_available(1))
        self.assertTrue(ml.is_move_available(2))
        self.assertTrue(ml.is_move_available(3))
        self.assertFalse(ml.is_move_available(0))
        self.assertFalse(ml.is_move_available(-1))
        self.assertFalse(ml.is_move_available(4))

    def test_enumerate(self):
        ml = MoveList(self.valid_move, self.valid_move, self.valid_move)
        i = 1
        for idx, move in ml.enumerate():
            self.assertEqual(idx, i)
            self.assertTrue(isinstance(move, Move))
            i += 1


if __name__ == "__main__":
    unittest.main()
