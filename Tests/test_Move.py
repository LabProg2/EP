import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Move import Move
from Type import Type

class TestMove(unittest.TestCase):
    def setUp(self):
        self.valid_name="Tackle"
        self.valid_elm_type = Type.Normal
        self.valid_accuracy = 100 
        self.valid_power = 50
        self.valid_pp = 35

    def test_stab(self):
        for i in range(0, 16):
            a_type = Type(i)
            dif_type = Type(i + 1)

            atk = Move(self.valid_name, a_type, \
                    self.valid_accuracy, self.valid_power, self.valid_pp)

            # Test results
            self.assertEqual(atk.stab(a_type, a_type), 1.5)
            self.assertEqual(atk.stab(a_type, dif_type), 1.5)
            self.assertEqual(atk.stab(dif_type, a_type), 1.5)
            self.assertEqual(atk.stab(dif_type, dif_type), 1)

            # Test exceptions
            self.assertRaises(TypeError, atk.stab, "fire")
            self.assertRaises(TypeError, atk.stab, 0)

    def test_init(self):
        # Test wrong parameters passing
        self.assertRaises(TypeError, Move, self.valid_name, "Abobora", self.valid_accuracy, \
                          self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, "Abobora", \
                          self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, self.valid_accuracy, \
                            "abobora", self.valid_pp)
        self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, self.valid_accuracy, \
                          self.valid_power, "abobora")

        for i in range(1, 100):
            self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, 0 - i, \
                              self.valid_power, self.valid_pp)
            self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, 100 + i, \
                              self.valid_power, self.valid_pp)
            self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, self.valid_accuracy, \
                          0 - i, self.valid_pp)
            self.assertRaises(ValueError, Move, self.valid_name, self.valid_elm_type, self.valid_accuracy, \
                          self.valid_power, 0 - i)

        self.assertRaises(ValueError, Move, self.valid_name, Type.Blank, self.valid_accuracy, \
                          self.valid_power, self.valid_pp)

        self.assertTrue(isinstance(Move(self.valid_name, self.valid_elm_type, self.valid_accuracy, \
                        self.valid_power, self.valid_pp), Move))
        self.assertTrue(isinstance(Move(1234, self.valid_elm_type, "7", "7", "7"), Move))


if __name__ == '__main__':
    unittest.main()
        
