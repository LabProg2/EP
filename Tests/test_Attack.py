import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Attack import Attack
from Type import Type

class TestAttack(unittest.TestCase):
	def setUp(self):
		self.right_name="Tackle"
		self.right_elm_type = Type.normal
		self.right_accuracy = 100 #Sera que isso não é um float de 0 ~ 1??
		self.right_power = 50
		self.right_pp = 35

	def test_stab(self):
		fire_type = Type.fire
		water_type = Type.water
		atk = Attack(elm_type=Type.fire, name=self.right_name, \
				self.right_accuracy, self.right_power, self.right_pp)

		# Test results
		self.assertEqual(atk.stab(fire_type), 1.5)
		self.assertEqual(atk.stab(wate_type), 1)

		# Test exceptions
		self.assertRaises(TypeError, atk.stab("fire"))
		self.assertRaises(TypeError, atk.stab(0))

	def test_init(self):
		# Test wrong parameters passing
		assertRaises(ValueError, Attack(self, self.right_elm_type, \
				self.right_accuracy, self.right_power, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, "forninho", \
				self.right_accuracy, self.right_power, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_elm_type, \
				"something", self.right_power, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_elm_type, \
				self.right_accuracy, "Catorze", self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_elm_type, \
				self.right_accuracy, self.right_power, "Catorze"))
		
		# Test right parameters passing
		assertRaises(None, self.right_name, self.right_elm_type, \
				self.right_accuracy, self.right_power, self.right_pp))
		assertRaises(None, Attack(Name=1234, elm_type=self.right_elm_type, \
				"7", "7", "7"))

		# Test absurds!
		assertRaises(ValueError, Attack(self.right_name, Type.blank, \
				self.right_accuracy, self.right_power, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_type, \
				101, self.right_power, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_type, \
				-1, self.right_power, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_type, \
				self.right_accuracy, -1, self.right_pp))
		assertRaises(ValueError, Attack(self.right_name, self.right_type, \
				self.right_accuracy, self.right_power, -1))

if __name__ == '__main__':
	unittest.main()
		
