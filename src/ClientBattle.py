from requests import post

class ClientBattle(Battle):
    '''The client in a client-server battle'''
    def __init__(self, client_poke, server_adress = 'http://localhost', server_port = '5000'):
        '''Prepare the client to communicate with the server'''
        if not isinstance(server_poke, Pokemon):
            raise TypeError("server_poke must be a Pokemon instance")

        if type(host) is not str:
            raise TypeError("host name must be a string") 

        if type(port) is not int and type(port) is not str:
            raise TypeError("port must be an integer or a string")
        
        prepare_starting_xml()

        self._battleio = BattleIO()
        self._client_poke = client_poke
        self._server_adress = server_adress
        self._server_port = server_port

    def run_battle(path = '/battle', attack_path = '/battle/attack', xml_file):
        answer = post(self._server_adress + ':' + self._server_port + path, files = {'battle_state' : xml_file})
        battle_state = answer.content
        self._server_poke = self._build_oponent(battle_state)
        ####
        # atualiza os dados dos meus pokemons com o xml recebido
        self._update_pokemons(battle_state)
        ####

        while self._client_poke.is_alive() and self._server_poke.is_alive():
            self._inform_pokes_info(self._client_poke, self._server_poke)
            move = self._selct_move(self._client_poke)
            #move_id = self._client_poke.get_move_id(move)
            self._perform_play(self._client_poke, self._server_poke, move)
            move_path = self._server_adress + ':' + self._server_port + attack_path + '/' + move_id
            move_answer = post(move_path)
            battle_state = move_answer.content
            self._update_pokemons(battle_state)
        self._end_battle(self._client_poke, self._server_poke)

    def prepare_starting_xml(self):
        '''Creates a xml containing data of the client poke'''
        #xml.create_xml(self._client_poke)
        pass

    def _update_pokemons(self, battle_state):
        '''Update pokemons info with an xml string
        :param battle_state: the xml containing data of both, client and server pokemon
        '''
        #xml.update_pokes(self._client_poke, self._server_poke, battle_state)
        pass

    def _build_oponent(battle_state_str):
        '''Build the oponent pokemon
        :param battle_state_str: the string containing both, client and server pokemons (in a xml format)
        '''
        #xmler.string_to_xml(battle_state_str)
        #poke_list = xmler.xml_to_pokemon()
        #return poke_list[0]
        pass