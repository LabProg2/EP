from PokeIO import PokeIO
from Stats import Stats
from time import sleep

class Battle:
    ''' The battle between two pokemons'''

    def __init__(self, poke1_path, poke2_path):
        ''' Prepare battle between poke1 and poke2'''
        self._pokeio = PokeIO()
        try:
            poke1_f = open(poke1_path, 'r')
        except FileNotFoundError:
            print("The first pokemon file couldn't be read")
            raise FileNotFoundError
        try:
            poke2_f = open(poke2_path, 'r')
        except FileNotFoundError:
            print("The second pokemon file couldn't be read")
            raise FileNotFoundError

        poke1 = self._pokeio.read_poke(poke1_f)
        poke2 = self._pokeio.read_poke(poke2_f)

        if poke1.spd >= poke2.spd:
            self._active_poke, self._idle_poke = poke1, poke2
        else:
            self._active_poke, self._idle_poke = poke2, poke1

    def run_battle(self):
        ''' Start the battle'''
        while self._active_poke.is_alive() or self._idle_poke.is_alive():
            self._pokeio.print_poke_info(self._idle_poke, False)
            self._pokeio.print_poke_info(self._active_poke, True)
            sleep(2)

            self._pokeio.print_move_list(self._active_poke.move_list)
            move = self._pokeio.read_move(self._active_poke.move_list)
            print(self._active_poke.name, "used", move._name)
            damage = self._active_poke.perform_move(move, self._idle_poke)
            if damage == -1:
                print("The attack was missed\n")
            else:
                print("It caused a damage of " + str(damage) + "\n") 
            sleep(2)
            self._switch_turns()

    def _switch_turns(self):
        ''' Changes the turn of pokemons'''
        self._active_poke, self._idle_poke = self._idle_poke, self._active_poke
