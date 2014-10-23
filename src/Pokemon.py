class Pokemon:
    '''
    TODO: descirption
    '''
    def __init__(self, poke_type, stats, name = 'unknown', level = 1, move_list = []):
        ''' TODO: Description

        :param poke_type: TODO
        :param stats: TODO
        :param name: TODO
        :param level: TODO
        :param move_list: TODO
        :returns: TODO
        '''
        self._name = name
        self._level = level
        self._poke_type = poke_type
        self._stats = stats
        self._move_list = move_list

    @property
    def name(self):
        '''Get pokemon's name'''
        return self._name
    @name.setter
    def name(self, value):
        '''Set pokemon's name'''
        self._name = value
    
    @property
    def level(self):
        '''Get pokemon's level'''
        return self._level
    @level.setter
    def level(self, value):
        '''Set pokemon's level'''
#### TESTAR PARA AS OUTRAS PROPERTIES ASSIM COMO ESSE TRY: ######   
        try:
            value = int(value)
        except ValueError:
            print ("ERROR: Tried to assign a not int value to pokemon's level")
        else:
            self._level = value 
    
    @property
    def move_list(self):
        '''Get pokemon's move_list'''
        return self._move_list
    @move_list.setter
    def move_list(self, value):
        self.move_list = value
    
#######################################################################################3

    def is_alive(self):
        ''' TODO: description

        :returns: TODO
        '''
        return self.health_power > 0

    @property
    def defense_force(self):
        return stats.defense_force()

    def perform_move(move, onPokemon):
        ''' TODO: description
        
        :param move: TODO
        :param onPokemon: TODO
        :returns: TODO
        '''
        # modifier = move.stab(type())*stats.critical()*random.uniform(0.85,1)*compare_to(onPokemon) ???
        # damage = ((stats.attack_force()*move.base()/onPokemon.defense_force())+2)*modifier
        pass

    def receive_damage(damage = 0):
        ''' TODO: description

        :param damage: TODO
        :returns: TODO
        '''
        pass

