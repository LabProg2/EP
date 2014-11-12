from bottle import Bottle, request
from Battle import Battle
from BattleIO import BattleIO

class ServerBattle(Battle):
    '''The server player in a pokemon battle'''
    def __init__(self, server_poke, host = 'localhost', port = '5000'):
        '''prepare the server to host the battle'''
        self._battleio = BattleIO()
        self._server_poke = server_poke

        #bottle things
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):
        self._app.route('/battle', method = 'POST', callback = self._battle_start)
        self._app.route('/battle/<id>', method = 'POST', callback = self._client_attack)

    def start(self):
        self._app.run(host=self._host, port=self._port)

    def _battle_start(self):
        f = request.files.get('xml')
        print(f)
        f.save('./tmp_poke_state.xml', overwrite = True)
        return 'success'

    def _client_attack(self):
        return