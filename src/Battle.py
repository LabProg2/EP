from PokeIO import PokeIO
class Battle:
    ''' The battle between two pokemons'''
    def __init__(self, poke1_path, poke2_path):
        ''' Prepare battle between poke1 and poke2'''
        #verificar se poke1 e poke2 são pokemons e levantar exception
        pokeio = PokeIO()
        try:
            poke1_f = open(poke1_path, 'r')
        except FileNotFoundError:
            print("The first pokemon file couldn't be read")
        try:
            poke2_f = open(poke1_path, 'r')
        except FileNotFoundError:
            print("The second pokemon file couldn't be read")

        poke1 = pokeio.read_poke(poke1_f)
        poke2 = pokeio.read_poke(poke2_f)

        if poke1.stats.speed > poke2.stats.speed:
            self._active_poke, self._idle_poke = poke1, poke2
        else:
            self._active_poke, self._idle_poke = poke2, poke1

    def run_battle(self):
        ''' Start the battle'''
        while self._active_poke.is_alive() or self._idle_poke.is_alive():
            pokeio.print_poke_info(self._active_poke, True)
            pokeio.print_poke_info(self._idle_poke, False)
            pokeio.print_move_list(self._active_poke.move_list)
            move = pokeio.read_move()
            damage = self._active_poke.perform_move(move, self._idle_poke)
            self._idle_poke.receive_damage(damage)
            self._switch_turns()

    def _switch_turns(self):
        ''' Changes the turn of pokemons '''
        self._active_poke, self._idle_poke = self._idle_poke, self._active_poke
