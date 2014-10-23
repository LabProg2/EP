class Battle:
	def __init__(self, poke1, poke2):
		''' Make poke1 and poke2 battle	'''
		self._poke1 = poke1
		self._poke2 = poke2
		self._turn = self.whos_faster(poke1, poke2)

	def whos_faster(poke1, poke2):
		''' Decides which pokemon is faster '''
		if poke1.get_spd() > poke2.get_spd(): 
			return poke1
		else:
			return poke2

	def run_battle():
		''' Start the battle '''
		pokeio = PokeIO()
		active_poke = whos_faster(self._poke1, self._poke2)
		while self._poke1.is_alive() or self._poke2.is_alive():
			pokeio.print_poke_info(self._poke1, active_poke is self._poke1)
			pokeio.print_poke_info(self._poke2, active_poke is self._poke2)
			pokeio.print_attack_list(active_poke)
			attack = pokeio.read_attack
			if active_poke is self._poke1:
				next_poke = self._poke2
			else:
				next_poke = self._poke1
			damage = active_poke.perform_attack(attack, next_poke)
			next_poke.receive_damage(damage)
			active_poke = next_poke


