from BattleIO import BattleIO
from time import sleep
from Pokemon import Pokemon
from Move import Move

class Battle:
    '''The battle between two pokemons'''
    
    def _switch_turns(self):
        '''Changes the turn of pokemons'''
        self._active_poke, self._idle_poke = self._idle_poke, self._active_poke

    def _starting_poke(self, poke1, poke2):
        '''Decides whose pokemon starts to play
        :param poke1: A pokemon
        :param poke2: Another pokemon
        '''
        if poke1.speed >= poke2.speed:
            return (poke1, poke2)
        else:
            return (poke2, poke1)

    def _select_move(self, atking_poke, move_list):
        '''Let the atking_poke choose a move
        :param atking_poke: The pokemon that is attacking
        :param move_list: The move list of the pokemon
        '''
        self._battleio.print_move_list(atking_poke.move_list)
        return self._battleio.read_move(atking_poke.move_list, atking_poke.available_moves())
    
    def _perform_play(self, atking_poke, atked_poke, move):
        '''The attacking poke attacks the attacked poke
        :param atking_poke: The pokemon that's attacking
        :param atked_poke: The pokemon that's being attacked
        '''
        damage = atking_poke.perform_move(move, atked_poke)
        self._battleio.print_move_result(atking_poke, move, damage)

    def _end_battle(self):
        '''Prints the winner of a Battle'''
        if self._idle_poke.is_alive():
            self._battleio.print_winner(self._idle_poke)
        else:
            self._battleio.print_winner(self._active_poke)
