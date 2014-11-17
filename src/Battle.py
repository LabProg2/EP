from BattleIO import BattleIO
from time import sleep
from Pokemon import Pokemon
from Move import Move
from pokexmler import PokeXmler

class Battle:
    '''The battle between two pokemons'''

    def _starting_poke(self, poke1, poke2):
        '''Decides whose pokemon starts to play
        :param poke1: A pokemon
        :param poke2: Another pokemon
        '''
        if poke1.speed >= poke2.speed:
            return (poke1, poke2)
        else:
            return (poke2, poke1)

    def _select_move(self, atking_poke):
        '''Let the atking_poke choose a move
        :param atking_poke: The pokemon that is attacking
        :param move_list: The move list of the pokemon
        '''
        self._battleio.print_moves_of(atking_poke)
        move = self._battleio.read_move_of(atking_poke)
        return move
    
    def _perform_play(self, atking_poke, atked_poke, move):
        '''The attacking poke attacks the attacked poke
        :param atking_poke: The pokemon that's attacking
        :param atked_poke: The pokemon that's being attacked
        :param move: The atking_poke move against the atked_poke
        '''
        damage = atking_poke.perform_move(move, atked_poke)
        self._battleio.print_move_result(atking_poke, move, damage)

    def _inform_pokes_info(self, pokemon_on_turn, idle_pokemon):
        '''Inform player the info about the two pokemon
        :param pokemon_on_turn: The pokemon that's attacking
        :param idle_pokemon: The pokemons that's being attacked
        '''
        self._battleio.print_poke_info(idle_pokemon, is_on_turn = False)
        self._battleio.print_poke_info(pokemon_on_turn, is_on_turn = True)

    def _update_battle_state(self, poke1, poke2 = None):
        '''This function receives two pokemons and update the battle_state of the battle
        :param poke1: A fighting pokemon
        :param poke2: Another fighting pokemon
        '''
        xmler = PokeXmler()
        if poke2 is None:
            self._battle_state = xmler.pokes_to_xml(poke1)  
        else:  
            self._battle_state = xmler.pokes_to_xml(poke1, poke2)

    def _updated_pokemons(self):
        '''This function returns the list of pokemons that's
           being represented by the battle_state'''
        xmler = PokeXmler()
        return xmler.str_to_pokes(self._battle_state)

    def _end_battle(self, poke1, poke2):
        '''Prints the winner of a Battle'''
        if poke1.is_alive():
            self._battleio.print_winner(poke1)
        else:
            self._battleio.print_winner(poke2)

    def pokeinfo_for_tests(self, poke):
        print('nome: ' + poke.name + ' | hp: ' + str(poke.hp))
