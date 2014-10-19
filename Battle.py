class Battle:
	def __init__(self, poke1, poke2):
		self.poke1 = poke1
		self.poke2 = poke2
		self.turn = self.whos_faster(poke1, poke2)

	def whos_faster(poke1, poke2):
		return poke1 if poke1.get_spd() > poke2.get_spd() else return poke2

	def run_battle():
		pokeio = PokeIO()
		active_poke = whos_faster(poke1, poke2)
		while poke1.is_alive() or poke2.is_alive():
			pokeio.print_poke_info(self.poke1, self.turn == 1)
			pokeio.print_poke_info(self.poke2, self.turn == 2)
			pokeio.print_attack_list(active_poke)
			attack = pokeio.read_attack
			if active_poke is poke1:
				next_poke = poke2
			else:
				next_poke = poke1
			damage = active_poke.perform_attack(attack, next_poke)
			next_poke.receive_damage(damage)
			active_poke = next_poke




