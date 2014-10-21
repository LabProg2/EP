class Attack:
	def __init__(self, name, elm_type, accuracy, power, pp):
		self._name = name
		self._elm_type = elm_type
		self._accuracy = accuracy
		self._power = power
		self._pp = pp

	@property
	def power(self):
		return self._power

	def stab(self, poke_type):
		if self._elm_type == poke_type :
			return 1.5
		return 1
	
