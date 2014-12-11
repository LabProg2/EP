from requests import post
from pokexmler import PokeXmler
from Battle import Battle
from os import remove
from Pokemon import Pokemon
from BattleIO import BattleIO

class ClientBattle(Battle):
    '''The client in a client-server battle'''
    def __init__(self, client_poke, server_address = 'http://localhost', server_port = '5000', ai = False):
        super().__init__(ai)

        ''' Prepare the client to communicate with the server '''
        if not isinstance(client_poke, Pokemon):
            raise TypeError("server_poke must be a Pokemon instance")

        if type(server_address) is not str:
            raise TypeError("host name must be a string") 

        if type(server_port) is not int and type(server_port) is not str:
            raise TypeError("port must be an integer or a string")

        self._battleio = BattleIO()
        
        self._client_poke = client_poke
        self._prepare_starting_xml()

        self._server_address = server_address
        self._server_port = server_port

    def run_battle(self, start_path = '/battle', attack_path = '/battle/attack'):
        ''' This method runs a battle between a client and a server from the client-side
        
        :param path: The path used to start a battle
        :param attack_path: The path used to send the cliend attacks
        '''
        if type(start_path) is not str:
            raise TypeError("start_path must be a string")

        if type(attack_path) is not str:
            raise TypeError("attack_path must be a string")  
        try:
            answer = post(self._server_address + ':' + self._server_port + start_path, files = {'battle_state' : open('tmp_xml.xml', 'rb')})
        except:
            raise RuntimeError("Sorry. We couldn't post to the server")
        remove('tmp_xml.xml')

        self._battle_state = answer.content.decode()
        self._client_poke, self._server_poke = self._updated_pokemons()
        
        while self._client_poke.is_alive() and self._server_poke.is_alive():
            self._inform_pokes_info(self._client_poke, self._server_poke)

            print("**************\nvalores esperados de dano:")
            for move in self._client_poke.moves:
                print(move.name + " : " + str(self._client_poke.expected_damage(move, self._server_poke)))
            print("**************")

            move = self._select_move(self._client_poke, self._server_poke, self._ai)
            move_id = self._client_poke.moves.get_move_id(move)
            move_path = self._server_address + ':' + self._server_port + attack_path + '/' + str(move_id)
            try:
                move_answer = post(move_path)
            except:
                raise RuntimeError("Sorry. We couldn't post to the server")
            self._battle_state = move_answer.content.decode()
            self._client_poke, self._server_poke = self._updated_pokemons()

        self._end_battle(self._client_poke, self._server_poke)
        try:
            end_path = self._server_address + ':' + self._server_port + '/end'
            move_answer = post(end_path)
        except:
            raise RuntimeError("Sorry. We couldn't post to the server")

    def _prepare_starting_xml(self):
        ''' Creates a xml containing data of the client poke '''
        self._update_battle_state(self._client_poke)
        f = open('tmp_xml.xml', 'w')
        f.write(self._battle_state)
        f.close()
