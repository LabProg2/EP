from BattleIO import BattleIO
from time import sleep
from Pokemon import Pokemon
from Move import Move

class Battle:
    ''' The battle between two pokemons'''
    def __init__(self, poke1, poke2):
        ''' Prepare battle between poke1 and poke2'''
        self._battleio = BattleIO()
        if not isinstance(poke1, Pokemon):
            raise TypeError("poke1 must be a Pokemon instance")
        if not isinstance(poke2, Pokemon):
            raise TypeError("poke2 must be a Pokemon instance")
        self._active_poke, self._idle_poke = self._starting_poke(poke1, poke2)

    def run_battle(self):
        ''' Start the battle'''
        while self._active_poke.is_alive() and self._idle_poke.is_alive():
            self._battleio.print_poke_info(self._idle_poke, is_on_turn = False)
            self._battleio.print_poke_info(self._active_poke, is_on_turn = True)

            sleep(0.5)
            self._perform_play(self._active_poke, self._idle_poke, self._active_poke.move_list)
            self._switch_turns()    
            sleep(0.5)
        
        if self._idle_poke.is_alive():
            self._battleio.print_winner(self._idle_poke)
        else:
            self._battleio.print_winner(self._active_poke)

    def _switch_turns(self):
        ''' Changes the turn of pokemons'''
        self._active_poke, self._idle_poke = self._idle_poke, self._active_poke

    def _starting_poke(self, poke1, poke2):
        if poke1.speed >= poke2.speed:
            return (poke1, poke2)
        else:
            return (poke2, poke1)

    def _perform_play(self, atking_poke, atked_poke, move_list):
        self._battleio.print_move_list(atking_poke.move_list)
        move = self._battleio.read_move(atking_poke.move_list)
        damage = self._active_poke.perform_move(move, atked_poke)
        self._battleio.print_move_result(atking_poke, move, damage)
