class Stats:
	def __init__(hp, attack_power, defense_power, speed, special): # Se houvessem valores padroes deveriamos por? ou definir setters para se um dia houvessem 10 stats fosse mais facil de inicializar? x_x
		self._hp = hp
		self._attack_power = attack_power
		self._defense_power = defense_power
		self._speed = speed
		self._special = special

	def decrease_life(amount):
		self._hp = self._hp - amount

	def attack_force(level):
		return (2 * level + 10)*self._attack_power

	def defense_force():
		return 250 * self._defense_power

	def critical():
		return self._speed/512
