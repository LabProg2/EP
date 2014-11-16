from requests import post
from pokexmler import PokeXmler
from Battle import Battle
from os import remove
from Pokemon import Pokemon
from BattleIO import BattleIO

class ClientBattle(Battle):
    '''The client in a client-server battle'''
    def __init__(self, client_poke, server_adress = 'http://localhost', server_port = '5000'):
        '''Prepare the client to communicate with the server'''
        if not isinstance(client_poke, Pokemon):
            raise TypeError("server_poke must be a Pokemon instance")

        if type(server_adress) is not str:
            raise TypeError("host name must be a string") 

        if type(server_port) is not int and type(server_port) is not str:
            raise TypeError("port must be an integer or a string")

        self._battleio = BattleIO()
        
        self._client_poke = client_poke
        self.prepare_starting_xml()

        self._server_adress = server_adress
        self._server_port = server_port

    def run_battle(self, start_path = '/battle', attack_path = '/battle/attack'):
        '''This method runs a battle between a client and a server from the client-side
        :param path: The path used to start a battle
        :param attack_path: The path used to send the cliend attacks
        '''
        answer = post(self._server_adress + ':' + self._server_port + start_path, files = {'battle_state' : open('tmp_xml.xml', 'rb')})
        remove('tmp_xml.xml')

        self._battle_state = answer.content
        self._client_poke, self._server_poke = self._updated_pokemons()
        
        while self._client_poke.is_alive() and self._server_poke.is_alive():
            self._inform_pokes_info(self._client_poke, self._server_poke)

            move = self._select_move(self._client_poke)
            move_id = self._client_poke.moves.get_move_id(move)
            move_path = self._server_adress + ':' + self._server_port + attack_path + '/' + str(move_id)
            move_answer = post(move_path)
            self._battle_state = move_answer.content
            self._client_poke, self._server_poke = self._updated_pokemons()
            ## achar um jeito de mostrar como sucedeu o ataque pela resposta do servidor

        self._end_battle(self._client_poke, self._server_poke)

    def prepare_starting_xml(self):
        '''Creates a xml containing data of the client poke'''
        self._update_battle_state(self._client_poke)
        f = open('tmp_xml.xml', 'w')
        f.write(self._battle_state)
        f.close()
