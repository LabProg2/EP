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

        self._battleio = BattleIO()
        self._client_poke = client_poke
        self._server_adress = server_adress
        self._server_port = server_port

    def post_start(path = '/battle'):
        answer = post(server_adress + ':' + server_port + path, )
        pass