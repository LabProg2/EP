import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../src/'));
from Attack import Attack

class TestAttack(unittest.TestCase):
	def setUp(self):
		pass

	def test_stab(self):
		atk = Attack(elm_type="Fire", name=None, accuracy=None, power=None, pp=None)
		self.assertEqual(atk.stab("Fire"), 1.5)

if __name__ == '__main__':
	unittest.main()
		
