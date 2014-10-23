import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Move import Move
from Type import Type

class TestMove(unittest.TestCase):
    def setUp(self):
        self.valid_name="Tackle"
        self.valid_elm_type = Type.Normal
        self.valid_accuracy = 100 #Sera que isso não é um float de 0 ~ 1??
        self.valid_power = 50
        self.valid_pp = 35

    def test_stab(self):
        fire_type = Type.Fire
        water_type = Type.Water
        atk = Move(self.valid_name, Type.Fire, \
                self.valid_accuracy, self.valid_power, self.valid_pp)

        # Test results
        self.assertEqual(atk.stab(fire_type), 1.5)
        self.assertEqual(atk.stab(water_type), 1)

        # Test exceptions
        self.assertRaises(TypeError, atk.stab, "fire")
        self.assertRaises(TypeError, atk.stab, 0)

    def test_init(self):
        a = Move(self.valid_name, self.valid_elm_type, self.valid_accuracy, \
                self.valid_power, self.valid_pp)
        # Test wrong parameters passing
        self.assertRaises(ValueError, Move.__init__, a, self, self.valid_elm_type, \
                self.valid_accuracy, self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, "forninho", \
                self.valid_accuracy, self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                "something", self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                self.valid_accuracy, "Catorze", self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                self.valid_accuracy, self.valid_power, "Catorze")
        
        # Test valid parameters passing
        self.assertRaises(None, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                self.valid_accuracy, self.valid_power, self.valid_pp)
        self.assertRaises(None, Move.__init__, a, name=1234, elm_type=self.valid_elm_type, \
                accuracy="7", power="7", pp="7")

        # Test absurds!
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, Type.Blank, \
                self.valid_accuracy, self.valid_power, self.valid_pp)

        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                101, self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                -1, self.valid_power, self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                self.valid_accuracy, -1, self.valid_pp)
        self.assertRaises(ValueError, Move.__init__, a, self.valid_name, self.valid_elm_type, \
                self.valid_accuracy, self.valid_power, -1)

if __name__ == '__main__':
    unittest.main()
        
