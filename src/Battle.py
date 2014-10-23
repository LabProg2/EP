class Battle:
    def __init__(self, poke1, poke2):
        ''' Prepare battle between poke1 and poke2 '''
        self._active_poke = self.whos_faster(poke1, poke2)
        if poke1 is self._active_poke: 
            self._idle_poke = poke2
        else:
            self._idle_poke = poke1

    def run_battle(self):
        ''' Start the battle '''
        pokeio = PokeIO()
        while self._active_poke.is_alive() or self._idle_poke.is_alive():
            pokeio.print_poke_info(self._active_poke, True)
            pokeio.print_poke_info(self._idle_poke, False)
            pokeio.print_attack_list(self._active_poke)
            attack = pokeio.read_attack
            damage = self._active_poke.perform_attack(attack, self._idle_poke)
            self._idle_poke.receive_damage(damage)
            self._switch_turns()

    def _switch_turns(self):
        ''' Changes the turn of pokemons '''
        temp = self._active_poke
        self._active_poke = self._idle_poke
        self._idle_poke = temp
