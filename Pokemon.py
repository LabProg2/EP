class Pokemon:
	'''
	Pokemon description TODO
	'''
	def __init__(self, poke_type, stats, name = 'unknown', level = 1, attack_list = []):
		''' Description TODO

		:param poke_type: TODO
		:param stats: TODO
		:param name: TODO
		:param level: TODO
		:param attack_list: TODO
		:returns: TODO
		'''
		self._name = name
		self._level = level
		self._poke_type = poke_type
		self._stats = stats
		self._attack_list = attack_list

	@property 
	def name(self):
		'''Get pokemon's name'''
		return self._name
	@name.setter
	def name(self, value):
		'''Set pokemon's name'''
		self._name = value
	
	@property
	def level(self):
		'''Get pokemon's level'''
		return self._level
	@level.setter
	def level(self, value):
		'''Set pokemon's level'''
#### TESTAR PARA AS OUTRAS PROPERTIES ASSIM COMO ESSE TRY: ######	
		try:
			value = int(value)
		except ValueError:
			print ("ERROR: Tried to assign a not int value to pokemon's level")
		else:
			self._level = value 
	
	@property
	def attack_list(self):
		'''Get pokemon's attack_list'''
		return self._attack_list
	@attack_list.setter
	def attack_list(self, value):
		self.attack_list = value
	
#######################################################################################3

	def is_alive():
		''' TODO: description

		:returns: TODO
		'''
		return self.health_power > 0

	def perform_attack(attack, onPokemon):
		''' TODO: description
		
		:param attack: TODO
		:param onPokemon: TODO
		:returns: TODO
		'''
		pass

	def receive_damage(damage = 0):
		''' TODO: description

		:param damage: TODO
		:returns: TODO
		'''
		pass

