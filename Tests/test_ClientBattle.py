import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../src/'))
from ClientBattle import ClientBattle
from Pokemon import Pokemon
from Type import Type
from Stats import Stats
from Move import Move

class TestClientBattle(unittest.TestCase):
    def setUp(self):
        self.valid_start_path = '/battle'
        self.valid_attack_path = '/battle/attack/'
        self.valid_poke = Pokemon([Type(7),Type(8)], Stats(2, 3, 4, 5, 6), [Move("atk", Type(2), 100, 30, 5)], "teste", 5)
        self.valid_server_address = 'http://localhost'
        self.valid_server_port = '5000'
        self.valid_clientbattle = ClientBattle(self.valid_poke, self.valid_server_address, self.valid_server_port)

    def test_init(self):
        #regular use of constructor
        self.assertTrue(isinstance(ClientBattle(self.valid_poke, self.valid_server_address, self.valid_server_port), ClientBattle))

        #regular use of constructor with default values
        self.assertTrue(isinstance(ClientBattle(self.valid_poke), ClientBattle))

        #wrong pokemon parameter testing
        self.assertRaises(TypeError, ClientBattle, object(), self.valid_server_address, self.valid_server_port)

        #wrong host parameter
        self.assertRaises(TypeError, ClientBattle, self.valid_poke, object(), self.valid_server_port)

        #wrong port parameter
        self.assertRaises(TypeError, ClientBattle, self.valid_poke, self.valid_server_address, object())
        
    def test_run_battle(self):
        #test wrong parameters passing
        self.assertRaises(TypeError, self.valid_clientbattle.run_battle, object(), self.valid_attack_path)
        self.assertRaises(TypeError, self.valid_clientbattle.run_battle, self.valid_start_path, object())



if __name__ == '__main__':
    unittest.main()
