from BattleIO import BattleIO
from time import sleep
from Pokemon import Pokemon

class Battle:
    ''' The battle between two pokemons'''

    def __init__(self, poke1, poke2):
        ''' Prepare battle between poke1 and poke2'''
        self._battleio = BattleIO()
        if not isinstance(poke1, Pokemon):
            raise TypeError("poke1 must be a Pokemon instance")
        if not isinstance(poke2, Pokemon):
            raise TypeError("poke2 must be a Pokemon instance")

        if poke1.spd >= poke2.spd:
            self._active_poke, self._idle_poke = poke1, poke2
        else:
            self._active_poke, self._idle_poke = poke2, poke1

    def run_battle(self):
        ''' Start the battle'''
        while self._active_poke.is_alive() or self._idle_poke.is_alive():
            self._battleio.print_poke_info(self._idle_poke, is_on_turn = False)
            self._battleio.print_poke_info(self._active_poke, is_on_turn = True)

            sleep(0.5)

            self._battleio.print_move_list(self._active_poke.move_list)
            move = self._battleio.read_move(self._active_poke.move_list)
            if move == None:
                self._battleio.print_winner(self._idle_poke)
                return
            print(self._active_poke.name, "used", move._name)
            damage = self._active_poke.perform_move(move, self._idle_poke)
            if damage == -1:
                print("The attack was missed\n")
            else:
                print("It caused a damage of " + str(damage) + "\n") 
            sleep(0.5)
            self._switch_turns()
        
        if self._active_poke.is_alive():
            self._battleio.print_winner(self._active_poke)
        else:
            self._battleio.print_winner(self._idle_poke)

    def _switch_turns(self):
        ''' Changes the turn of pokemons'''
        self._active_poke, self._idle_poke = self._idle_poke, self._active_poke
