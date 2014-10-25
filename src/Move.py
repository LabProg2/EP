from Type import Type
from random import randrange
import re

class Move:
    '''
    Represents a Pokemon's move
    '''
    def __init__(self, name, elm_type, accuracy, power, pp):
        '''Move's constructor
        
        :param name: Move's name
        :param elm_type: Move's type
        :param accuracy: Move's accuracy
        :param pp: Move's power points. How many attacks you can use
        :returns: An Move instance with all attributes set
        '''
        try:
            name = str(name)
        except ValueError:
            raise ValueError('name must be a string')
        else:
            self._name = re.sub('[\s\t\n]*', '', name)

        if not isinstance(elm_type, Type):
            raise TypeError('elm_type must be an instance of Type')
        else:
            self._elm_type = elm_type

        try:
            accuracy = int(accuracy)
            if accuracy > 100 or accuracy < 0:
                raise ValueError
        except ValueError:
            raise ValueError('accuracy must be an int in interval [0 ; 100')
        else:
            self._accuracy = accuracy

        try:
            power = int(power)
            if power < 0:
                raise ValueError
        except ValueError:
            raise ValueError('power must be an int greater than or equal to 0')
        else:
            self._power = power

        try:
            pp = int(pp)
            if pp < 0:
                raise ValueError
        except ValueError:
            raise ValueError('pp must be an int greater than or equal to 0')
        else:
            self._pp = pp

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def pp(self):
        return self._pp

    def stab(self, poke_type1, poke_type2):
        ''' Same Type Attack Bonus

        :param poke_type1: A type to compare to the current Move type
        :param poke_type1: A type to compare to the current Move type
        :returns: The stab coefficient of the damage formula
        '''
        if not isinstance(poke_type1, Type) or not isinstance(poke_type2, Type):
            raise TypeError('Pokemon type must be an instance of Type')
        
        if self._elm_type == poke_type1 or self._elm_type == poke_type2:
            return 1.5
        return 1

    def missed(self):
        return randrange(0, 100) <= self._accuracy
