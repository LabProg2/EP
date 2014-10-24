from Type import Type

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
        try:
            name = str(name)
        except ValueError:
            raise ValueError('name must be a string')
        else:
            self._name = name

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
    def accuracy(self):
         ''' Get the accuracy of the move 
         :returns: returns the accuracy of the move
        '''
        return self._accuracy

    def stab(self, poke_type):
        ''' Same Type Attack Bonus

        :param poke_type: A type to compare to the current Move type
        :returns: The stab coefficient of the damage formula
        '''
        if not isinstance(poke_type, Type):
            raise TypeError('poke_type must be an instance of Type')
        
        if self._elm_type == poke_type :
            return 1.5
        return 1
