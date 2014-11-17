import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../src/'))
from ServerBattle import ServerBattle
from Pokemon import Pokemon
from Type import Type
from Stats import Stats
from Move import Move

class TestServerBattle(unittest.TestCase):
    def setUp(self):
        self.valid_poke = Pokemon([Type(7),Type(8)], Stats(2, 3, 4, 5, 6), [Move("atk", Type(2), 100, 30, 5)], "teste", 5)
        self.valid_host = 'localhost'
        self.valid_port = 5000
        self.valid_address = 'http://' + self.valid_host + ':' + str(self.valid_port)
        self.valid_server = ServerBattle(self.valid_poke, self.valid_host, self.valid_port)

    def test_init(self):
        #regular use of constructor
        self.assertTrue(isinstance(ServerBattle(self.valid_poke, self.valid_host, self.valid_port), ServerBattle))

        #regular use of constructor with default values
        self.assertTrue(isinstance(ServerBattle(self.valid_poke), ServerBattle))

        #wrong pokemon parameter testing
        self.assertRaises(TypeError, ServerBattle, object(), self.valid_host, self.valid_port)

        #wrong host parameter
        self.assertRaises(TypeError, ServerBattle, self.valid_poke, object(), self.valid_port)

        #wrong port parameter
        self.assertRaises(TypeError, ServerBattle, self.valid_poke, self.valid_host, object())

    def test_start(self):
        #if the server couldn't be started an error should be raised
        invalid_host_server = ServerBattle(self.valid_poke, 'anythingbutavalidhost', '5000')
        self.assertRaises(RuntimeError, invalid_host_server.start)

if __name__ == '__main__':
    unittest.main()
