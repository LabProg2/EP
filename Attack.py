class Attack:
	def __init__(self, name, elm_type, accuracy, power, pp):
		self._name = name
		self._poke_type = poke_type
		self._accuracy = accuracy
		self._power = power
		self._pp = pp

	@property
	def stab(poke_type):
		if elm_type == poke_type :
			return 1.5
		return 1
	
	@property
	def base(self):
		return self._power