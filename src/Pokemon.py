class Pokemon:
	'''
	Class that defines the properties, attack and defense of the Pokemon
	'''
	def __init__(self, poke_type1, poke_type2 = 'none', stats, name = 'unknown', level = 1, move_list = []):
		''' Description TODO

		:param poke_type1: Pokemon's principal type
		:param poke_type2: Pokemon's secondary type (default: none)
		:param stats: Pokemon's stats, object of the Stats class.
		:param name: Pokemon's name (for example, a Zubat's name is 'Batman')
		:param level: Pokemon's level
		:param move_list: Pokemon's moves, object of the Move class.
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

	def is_alive():
		''' TODO: description

		:returns: TODO
		'''
		return stats.hp() > 0

	@property
	def defense_force(self):
		return stats.defense_force()
	
	def perform_attack(attack, onPokemon):
		''' Calculates the damage of Pokemon's attack over the onPokemon, based on http://bulbapedia.bulbagarden.net/wiki/Damage#Damage_formula
		
		:param attack: TODO
		:param onPokemon: TODO
		'''
		
		#compares all possibilities of primary and secondary types of Pokemon and onPokemon
		compare_modifier = poke_type1.compare_to(poke_type1.onPokemon) * poke_type1.compare_to(poke_type2.onPokemon) * poke_type2.compare_to(poke_type1.onPokemon) * poke_type2.compare_to(poke_type2.onPokemon)
							
		modifier = compare_modifier * attack.stab(type()) * stats.critical() * random.uniform(0.85,1)
		damage = ((stats.attack_force() * attack.base() / onPokemon.defense_force()) + 2) * modifier
		onPokemon.receive_damage(damage)

	def receive_damage(damage = 0):
		''' TODO: description

		:param damage: TODO
		:returns: TODO
		'''
		try:
			damage = int(damage)
		except ValueError:
			print ("ERROR: Tried to assign a not int value in damage")
		else:
			stats.decrease_life(damage)

