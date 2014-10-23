class Move:
    ''' Represents a pokemon's move'''
    def __init__(self, name, elm_type, accuracy, power, pp):
        '''Move's constructor
        
        :param name: Move's name
        :param elm_type: Move's type
        :param accuracy: Move's accuracy
        :param pp: Move's power points. How many attacks you can use
        :returns: An Move instance with all attributes set
        '''
        self._name = name
        self._elm_type = elm_type
        self._accuracy = accuracy
        self._power = power
        self._pp = pp

    @property
    def power(self):
        return self._power

    def stab(self, poke_type):
        ''' Same Type Attack Bonus

        :param poke_type: A type to compare to the current Move type
        :returns: The stab coefficient of the damage formula
        '''
        if self._elm_type == poke_type :
            return 1.5
        return 1
    
