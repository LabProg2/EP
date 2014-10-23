class Pokemon:
    '''
    Class that defines the properties, attack and defense of the Pokemon
    '''
    def __init__(self, poke_type1, poke_type2 = 'none', stats, name = 'unknown', level = 1, move_list = []):
        ''' Description TODO

        :param poke_type1: Pokemon's principal type
        :param poke_type2: Pokemon's secondary type (default: none)
        :param stats: Pokemon's stats, object of the Stats class.
        :param name: Pokemon's name (for example, a Zubat's name is 'Batman')
        :param level: Pokemon's level
        :param move_list: Pokemon's moves, object of the Move class.
        :returns: TODO
        '''
        self._name = name
        self._level = level
        self._poke_type = poke_type
        self._stats = stats
        self._attack_list = attack_list

############# PROPERTIES ################################################################

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
#### TESTAR PARA AS OUTRAS PROPERTIES ASSIM COMO ESSE TRY: ######   
        try:
            value = int(value)
        except ValueError:
            print ("ERROR: Tried to assign a not int value to pokemon's level")
        else:
            self._level = value 
    
    @property
    def attack_list(self):
        '''Get pokemon's attack_list'''
        return self._attack_list
    @attack_list.setter
    def attack_list(self, value):
        self._attack_list = value

    @property
    def defense_force(self):
        return stats.defense_force()

########## METHODS ######################################################################
    
    def is_alive():
        ''' TODO: description

        :returns: TODO
        '''
        return self._stats.hp > 0

    def perform_move(move, onPokemon):
        ''' Calculates the damage of Pokemon's attack over the onPokemon
        
        :param move: TODO
        :param onPokemon: TODO
        :returns: The damage received by the pokemon 
        '''
        compare_modifier = self.compare_types_to(onPokemon)
        modifier = compare_modifier * move.stab(self._poke_type) * stats.critical() * random.uniform(0.85,1)
        damage = (self._stats.attack_force() * move.power / onPokemon.defense_force() + 2) * modifier
        onPokemon.receive_damage(damage)
        return damage

    def compare_types_to(pokemon):
        ''' Compare every combination between two pokemon's types. 

        :param pokemon: The deffensive pokemon.
        :returns: The **Type** coefficient to be used on damage formula
        '''
        # TODO: Verify if it is realy a pokemon?
        type_coef = 1
        for type1 in self._type_list:
            for type2 in pokemon.type_list:
                type_coef *= type1.compare_to(type2)

        return type_coef

    def receive_damage(damage = 0):
        ''' TODO: description

        :param damage: TODO
        :returns: TODO
        '''
        try:
            damage = int(damage)
        except ValueError:
            print ("ERROR: Tried to assign a not int value in damage")
        else:
            stats.decrease_life(damage)

