from BattleIO import BattleIO
from Battle import Battle
from Pokemon import Pokemon
from time import sleep

class OfflineBattle(Battle):
    ''' The offline battle '''
    def __init__(self, poke1, poke2, ai = False):
        super().__init__(ai)

        ''' Prepare battle between poke1 and poke2
        :param poke1: A Pokemon
        :param poke2: Another Pokemon
        '''
        self._battleio = BattleIO()
        if not isinstance(poke1, Pokemon):
            raise TypeError("poke1 must be a Pokemon instance")
        if not isinstance(poke2, Pokemon):
            raise TypeError("poke2 must be a Pokemon instance")
        self._active_poke, self._idle_poke = self._starting_poke(poke1, poke2)

    def run_battle(self):
        ''' Start the battle '''
        while self._active_poke.is_alive() and self._idle_poke.is_alive():
            self._inform_pokes_info(self._active_poke, self._idle_poke)

            sleep(0.5)
            move = self._select_move(self._active_poke, self._idle_poke, self._ai)
            self._perform_play(self._active_poke, self._idle_poke, move)
            self._switch_turns()    

            sleep(0.5)
        self._end_battle(self._idle_poke, self._active_poke)

    def _switch_turns(self):
        '''Changes the turn of pokemons'''
        self._active_poke, self._idle_poke = self._idle_poke, self._active_poke
