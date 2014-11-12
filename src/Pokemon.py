from Move import Move
from Type import Type
from Stats import Stats
from random import uniform
import re

class Pokemon:
    '''
    Class that defines the properties, attack and defense of the Pokemon
    '''
    def __init__(self, type_list, stats, move_list, name = 'unknown', level = 1):
        '''Pokemon's constructor

        :param poke_type1: Pokemon's principal type
        :param poke_type2: Pokemon's secondary type (default: none)
        :param stats: Pokemon's stats, object of the Stats class.
        :param name: Pokemon's name (for example, a Zubat's name is 'Batman')
        :param level: Pokemon's level
        :param move_list: Pokemon's moves, object of the Move class.
        :returns: A Pokemon instance with all attributes set
        '''
        if type(name) is not str:
            raise TypeError("A pokemon name must be a string")

        self._name = re.sub('[\t\n]*', '', name)
        self.move_list = move_list

        self.level = level
        
        # Stats
        if not isinstance(stats, Stats):
            raise TypeError("stats must be a Stats's instance")
        self._stats = stats


        # Type
        if isinstance(type_list, Type):
            type_list = [type_list]
        if not isinstance(type_list, list):
            raise TypeError("type_list must be a list")
        type_list.append(Type.Blank)
        type_list = type_list[0 : 2]
        if len(type_list) == 1:
            raise ValueError("type_list must have at least one type")
        for typ in type_list:
            if not isinstance(typ, Type):
                raise TypeError("type_list must have only Type instances")
        self._type_list = type_list
############# PROPERTIES ################################################################

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        try:
            name = str(name)
        except ValueError:
            raise ValueError("name must be a string")
        else:
            self._name = name
    
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, level):
        try:
            level = int(level)
            if level < 1 or level > 100:
                raise ValueError
        except ValueError:
            raise ValueError("level must be an int in interval [1 ; 100]")
        else:
            self._level = level
    
    @property
    def move_list(self):
        return self._move_list
    @move_list.setter
    def move_list(self, move_list):
        if isinstance(move_list, Move):
            move_list = [move_list]
        struggle = Move("struggle", Type.Normal, 100, 50, 1)
        move_list = [struggle] + move_list[0 : 4]
        if len(move_list) == 1:
            raise ValueError("move_list must have at least one move")
        for mov in move_list:
            if not isinstance(mov, Move):
                raise TypeError("move_list must have only Move instances")
        self._move_list = move_list

    @property
    def type_list(self):
        return self._type_list

    @property
    def defense_force(self):
        return self._stats.defense_force()

    @property
    def spd(self):
        return self._stats.spd

    @property
    def hp(self):
        return self._stats.hp

########## METHODS ######################################################################
    
    def is_alive(self):
        ''' Tests if the Pokemon is alive, i.e. if it's hp is bigger than zero

        :returns: True or False if the hp is bigger or less than zero
        '''
        return self._stats.hp > 0

    def perform_move(self, move, onPokemon):
        ''' Calculates the damage of Pokemon's attack over the onPokemon
        
        :param move: Pokemon's move that will be performed, object of the Move class.
        :param onPokemon: The Pokemon's opponent in the battle
        :returns: The damage received by the pokemon. If the pokemon missed the attack it returns -1 
        '''

        if not isinstance(onPokemon, Pokemon):
            raise TypeError("onPokemon must be a Pokemon instance")

        if not isinstance(move, Move):
            raise TypeError("move must be a Move instance")
        if move.name == "struggle":
            damage = self._perform_struggle(move, onPokemon)
        else:
            damage = self._perform_regular_move(move, onPokemon)
        return damage

    def _perform_regular_move(self, move, onPokemon):
        damage = -1
        if not move.missed() and move.pp > 0:
            move.use_move()
            damage = self._calc_damage(move, onPokemon)
            onPokemon.receive_damage(damage)
        return damage

    def _perform_struggle(self, move, onPokemon):
        damage = self._calc_damage(move, onPokemon)
        if Type.Ghost in onPokemon.type_list:
            damage = 0
        elif Type.Rock in onPokemon.type_list:
            damage = damage / 2
        else:
            pass
        onPokemon.receive_damage(damage)
        self.receive_damage(damage / 2)
        return damage

    def _calc_damage(self, move, onPokemon):
        compare_modifier = self.compare_types_to(onPokemon)
        modifier = compare_modifier * move.stab(self._type_list[0], self._type_list[1]) * self._stats.critical(self._level) * uniform(0.85,1)
        damage = (self._stats.attack_force(self._level) * move.power / onPokemon.defense_force + 2) * modifier
        damage = int(damage)
        return damage

    def compare_types_to(self, pokemon):
        ''' Compare every combination between two pokemon's types. 

        :param pokemon: The deffensive pokemon.
        :returns: The **Type** coefficient to be used on damage formula
        '''
        if not isinstance(pokemon, Pokemon):
            raise TypeError("pokemon must be a Pokemon instance")

        type_coef = 1
        for type1 in self._type_list:
            for type2 in pokemon.type_list:
                type_coef = type_coef * type1.compare_to(type2)

        return type_coef

    def receive_damage(self, damage = 0):
        ''' Decreases the hp of the Pokemon of a damage.

        :param damage: Value of damage that will be received
        '''
        try:
            damage = int(damage)
        except TypeError:
            raise TypeError("damage must be of type int") 
        else:
            if damage < 0:
                raise ValueError("damage must be greater than 0")
            self._stats.decrease_life(damage)
