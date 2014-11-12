class ServerBattle(Battle):
	'''The server player in a pokemon battle'''
	def __init__(self, server_poke):
		'''prepare the server to host the battle'''
		self._battleio = BattleIO()
		
