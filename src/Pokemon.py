from Move import Move
from Type import Type
from Stats import Stats
from random import random

class Pokemon:
    '''
    Class that defines the properties, attack and defense of the Pokemon
    '''
    def __init__(self, type_list, stats, name = 'unknown', level = 1, move_list = []):
        ''' Description TODO

        :param poke_type1: Pokemon's principal type
        :param poke_type2: Pokemon's secondary type (default: none)
        :param stats: Pokemon's stats, object of the Stats class.
        :param name: Pokemon's name (for example, a Zubat's name is 'Batman')
        :param level: Pokemon's level
        :param move_list: Pokemon's moves, object of the Move class.
        :returns: TODO
        '''

        self.name = name

        try:
            level = int(level)
        except ValueError:
            raise ValueError("level must be an int")
        else:
            if level < 1 or level > 100:
                raise ValueError("level must be in interval [1 ; 100]")
            self._level = level
        
        if not isinstance(stats, Stats):
            raise TypeError("stats must be a Stats's instance")
        self._stats = stats
    
        self._move_list = move_list


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
        except ValueError:
            raise ValueError("level must be an int")
        else:
            self._level = value 
    
    @property
    def move_list(self):
        return self._move_list
    @move_list.setter
    def move_list(self, move_list):
        if isinstance(move_list, Move):
            move_list = [move_list]
        else:
            raise TypeError("move_list must have only Move instances")
        move_list = move_list[0 : 4]
        if len(move_list) == 0:
            raise ValueError("move_list must have at least one move")
        for mov in move_list:
            if not isinstance(mov, Move):
                raise TypeError("move_list must have only Move instances")
        self._move_list = move_list

    @property
    def defense_force(self):
        return self._stats.defense_force()

########## METHODS ######################################################################
    
    def is_alive(self):
        ''' TODO: description

        :returns: TODO
        '''
        return self._stats.hp > 0

    def perform_move(self, move, onPokemon):
        ''' Calculates the damage of Pokemon's attack over the onPokemon
        
        :param move: TODO
        :param onPokemon: TODO
        :returns: The damage received by the pokemon. If the pokemon missed the attack it returns -1 
        '''
        if not isinstance(onPokemon, Pokemon):
            raise TypeError("onPokemon must be a Pokemon instance")

        damage = -1
        if not move.missed():
            compare_modifier = self.compare_types_to(onPokemon)
            modifier = compare_modifier * move.stab(self._poke_type) * stats.critical() * random.uniform(0.85,1)
            damage = (self._stats.attack_force() * move.power / onPokemon.defense_force() + 2) * modifier
            onPokemon.receive_damage(damage)

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
                type_coef *= type1.compare_to(type2)

        return type_coef

    def receive_damage(self, damage = 0):
        ''' TODO: description

        :param damage: TODO
        :returns: TODO
        '''
        try:
            damage = int(damage)
        except ValueError:
            raise ValueError("damage must be an int greater than 0") 
        else:
            stats.decrease_life(damage)
