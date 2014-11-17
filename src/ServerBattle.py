from bottle import Bottle, request, FileUpload
from Battle import Battle
from BattleIO import BattleIO
from Pokemon import Pokemon

class ServerBattle(Battle):
    '''The server player in a client-server battle'''
    def __init__(self, server_poke, host = 'localhost', port = '5000'):
        '''Prepare the server to host the battle
        :param server_poke: The pokemon used by the server player
        :param host: The address of the server
        :param port: The port used in the server
        '''
        if not isinstance(server_poke, Pokemon):
            raise TypeError("server_poke must be a Pokemon instance")

        try:
            host = str(host)
        except:
            raise TypeError("host name must be a string") 

        try:
            port = int(port)
        except:
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
        self._app.route('/battle/attack/<idx>', method = 'POST', callback = self._receive_attack)
        self._app.route('/test', method = 'POST', callback = self._test_route)

    def start(self, muted = False):
        '''Starts the server'''
        try:
            self._app.run(host = self._host, port = self._port, debug = True, quiet = muted)
        except:
            raise RuntimeError("The server couldn't be started")

    def end(self):
        self._app.close()

    def _battle_start(self):
        '''Callback for a post in a server at the path /battle'''
        try:
            f = request.files.get('battle_state')
        except:
            raise RuntimeError("The server received a post without a battle_state")

        if not isinstance(f, FileUpload):
            raise RuntimeError("The server request couldn't create a FileUpload object")

        s = f.filename.split('.')
        if s[-1] != 'xml':
            raise NameError("The xml must be a '.xml' file")

        self._battle_state = f.file.read().decode()
        self._client_poke = self._updated_pokemons()[0]

        if self._server_poke.speed >= self._client_poke.speed:
            self._server_attack()
            
        if not self._client_poke.is_alive():
            self._battleio.print_winner(self._server_poke)

        self._update_battle_state(self._client_poke, self._server_poke)

        return self._battle_state

    def _receive_attack(self, idx):
        '''Callback for a post in a server at the path /battle/attack/<idx>
        :param idx: the id of the client move
        '''
        try:
            idx = int(idx)
        except:
            raise TypeError("The client sent an invalid move")

        self._inform_pokes_info(self._client_poke, self._server_poke)
        move = self._client_poke.moves.get_move(idx)
        self._perform_play(self._client_poke, self._server_poke, move)

        if not self._server_poke.is_alive():
            self._battleio.print_winner(self._client_poke)

        self._server_attack()
        self._update_battle_state(self._client_poke, self._server_poke)
        return self._battle_state
    
    def _server_attack(self):
        self._inform_pokes_info(self._server_poke, self._client_poke)
        move = self._select_move(self._server_poke)
        self._perform_play(self._server_poke, self._client_poke, move)
        
        self._update_battle_state(self._client_poke, self._server_poke)
        
        if not self._server_poke.is_alive():
            self._battleio.print_winner(self._client_poke)

    def _test_route(self):
        return 'ok'
