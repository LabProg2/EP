class Pokemon:
	def __init__(self, name = 'unknown', level = 1, poke_type, stats, attack_list = []):
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
	
	def is_alive():
		return self.health_power > 0

	@property
	def defense_force(self):
		return stats.defense_force()

	def perform_attack(attack, onPokemon):
		# modifier = attack.stab(type())*stats.critical()*random.uniform(0.85,1)*compare_to(onPokemon) ???
		# damage = ((stats.attack_force()*attack.base()/onPokemon.defense_force())+2)*modifier
		pass

	def receive_damage(damage = 0):
		pass

