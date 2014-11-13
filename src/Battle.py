from BattleIO import BattleIO
from time import sleep
from Pokemon import Pokemon
from Move import Move

class Battle:
    ''' The battle between two pokemons'''
    
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
        move = self._battleio.read_move(atking_poke.move_list, atking_poke.available_moves())
        damage = self._active_poke.perform_move(move, atked_poke)
        self._battleio.print_move_result(atking_poke, move, damage)

    def _end_battle(self):
        if self._idle_poke.is_alive():
            self._battleio.print_winner(self._idle_poke)
        else:
            self._battleio.print_winner(self._active_poke)
