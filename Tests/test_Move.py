import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Move import Move
from Type import Type

class TestMove(unittest.TestCase):
	def setUp(self):
		self.right_name="Tackle"
		self.right_elm_type = Type.Normal
		self.right_accuracy = 100 #Sera que isso não é um float de 0 ~ 1??
		self.right_power = 50
		self.right_pp = 35

	def test_stab(self):
		fire_type = Type.Fire
		water_type = Type.Water
		atk = Move(self.right_name, Type.Fire, \
				self.right_accuracy, self.right_power, self.right_pp)

		# Test results
		self.assertEqual(atk.stab(fire_type), 1.5)
		self.assertEqual(atk.stab(wate_type), 1)

		# Test exceptions
		self.assertRaises(TypeError, atk.stab("fire"))
		self.assertRaises(TypeError, atk.stab(0))

	def test_init(self):
		# Test wrong parameters passing
		self.assertRaises(ValueError, Move.__init__(self, self, self.right_elm_type, \
				self.right_accuracy, self.right_power, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, "forninho", \
				self.right_accuracy, self.right_power, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_elm_type, \
				"something", self.right_power, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_elm_type, \
				self.right_accuracy, "Catorze", self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_elm_type, \
				self.right_accuracy, self.right_power, "Catorze"))
		
		# Test right parameters passing
		self.assertRaises(None, Move.__init__(self, self.right_name, self.right_elm_type, \
				self.right_accuracy, self.right_power, self.right_pp))
		self.assertRaises(None, Move.__init__(self, name=1234, elm_type=self.right_elm_type, \
				accuracy="7", power="7", pp="7"))

		# Test absurds!
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, Type.Blank, \
				self.right_accuracy, self.right_power, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_type, \
				101, self.right_power, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_type, \
				-1, self.right_power, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_type, \
				self.right_accuracy, -1, self.right_pp))
		self.assertRaises(ValueError, Move.__init__(self, self.right_name, self.right_type, \
				self.right_accuracy, self.right_power, -1))

if __name__ == '__main__':
	unittest.main()
		
