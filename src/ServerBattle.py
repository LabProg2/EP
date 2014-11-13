from bottle import Bottle, request
from Battle import Battle
from BattleIO import BattleIO
from Pokemon import Pokemon

class ServerBattle(Battle):
    '''The server player in a pokemon battle'''
    def __init__(self, server_poke, host = 'localhost', port = '5000'):
        '''Prepare the server to host the battle
        :param server_poke: The pokemon used by the server player
        :param host: The address of the server
        :param port: The port used in the server
        '''
        if not isinstance(server_poke, Pokemon):
            raise TypeError("server_poke must be a Pokemon instance")

        if type(host) is not str:
            raise TypeError("host name must be a string") 

        if type(port) is not int and type(port) is not str:
            raise TypeError("port must be an integer or a string")

        self._battleio = BattleIO()
        self._server_poke = server_poke

        #bottle things
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):
        '''This method is used to route requests to the server'''
        self._app.route('/battle', method = 'POST', callback = self._battle_start)
        self._app.route('/battle/attack/<idx>', method = 'POST', callback = self._client_attack)

    def start(self):
        '''Starts the server'''
        self._app.run(host=self._host, port=self._port, debug=True)

    def _battle_start(self):
        '''Callback for a post in a server at the path /battle'''
        f = request.files.get('xml')
        print(f)
        f.save('./tmp_poke_state.xml', overwrite = True)

        #transforma o xml recebido em um pokemon
         
        ###########
        #isso e totalmente temporario pra testar outras coisas antes#
        self._client_poke = self._server_poke
        ############

        if self._server_poke.speed >= self._client_poke.speed:
            move = self._select_move(self._server_poke)
            self._perform_play(self._server_poke, self._client_poke, move)
            #atualiza o xml
        return 'aqui eu devo mandar o xml como uma string'
        #return the_xml_after_start

    def _client_attack(self, idx):
        '''Callback for a post in a server at the path /battle/attack/<idx>'''
        try:
            idx = int(idx)
        except:
            raise TypeError("The client sent an invalid move")

        move = self._client_poke.moves.get_move(idx)
        self._perform_play(self._client_poke, self._server_poke, move)

        move = self._select_move(self._server_poke)
        self._perform_play(self._server_poke, self._client_poke, move)

        return 'aqui eu mando o xml atualizado de novo'
        #return the_xml_after_play
        