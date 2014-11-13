from bottle import Bottle, request
from Battle import Battle
from BattleIO import BattleIO
from Pokemon import Pokemon

class ServerBattle(Battle):
    '''The server player in a pokemon battle'''
    def __init__(self, server_poke, host = 'localhost', port = '5000'):
        '''prepare the server to host the battle'''
        self._battleio = BattleIO()
        print(server_poke)
        if not isinstance(server_poke, Pokemon):
            raise TypeError("server_poke must be a Pokemon instance")
        self._server_poke = server_poke

        #bottle things
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):
        self._app.route('/battle', method = 'POST', callback = self._battle_start)
        self._app.route('/battle/attack/<idx>', method = 'POST', callback = self._client_attack)

    def start(self):
        self._app.run(host=self._host, port=self._port)

    def _battle_start(self):
        f = request.files.get('xml')
        print(f)
        f.save('./tmp_poke_state.xml', overwrite = True)

        #transforma o xml recebido em um pokemon
         
        ###########
        #isso e totalmente temporario pra testar outras coisas antes#
        client_poke = self._server_poke
        ############
        self._active_poke, self._idle_poke = self._starting_poke(self._server_poke, client_poke)
        if self._active_poke == self._server_poke:
            self._perform_play(self._active_poke, self._idle_poke, self._active_poke._move_list)
            #atualiza o xml
            self._switch_turns()
        return 'aqui eu devo mandar o xml como uma string'
        #return the_xml_final

    def _client_attack(self, idx):
        if idx not in 

        #perform user atk
        #perform server play
    
    def _valid_moves(self, move_list):
        