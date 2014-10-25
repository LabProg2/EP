from random import random

class Stats:
    '''
    TODO: description
    '''
    def __init__(self, hp, attack, defense, speed, special): # Se houvessem valores padroes deveriamos por? ou definir setters para se um dia houvessem 10 stats fosse mais facil de inicializar? x_x
        '''TODO: description

        :param hp: TODO
        :param attack: TODO
        :param defense: TODO
        :param speed: TODO
        :param special: TODO
        :returns: TODO
        '''

        try:
            hp = int(hp)
            if hp < 0:
                raise ValueError
        except ValueError:
            raise ValueError('hp must be an int greater than or equal to 0')
        else:
            self._hp = hp

        try:
            attack = int(attack)
            if attack < 0:
                raise ValueError
        except ValueError:
            raise ValueError('attack must be an int greater than or equal to 0')
        else:
            self._attack = attack

        try:
            defense = int(defense)
            if defense < 0:
                raise ValueError
        except ValueError:
            raise ValueError('defense mut be an int greater than or equal to 0')
        else:
            self._defense = defense

        try:
            speed = int(speed)
            if speed < 0:
                raise ValueError
        except ValueError:
            raise ValueError('speed mut be an int greater than or equal to 0')
        else:
            self._speed = speed
            
        try:
            special = int(special)
            if special < 0:
                raise ValueError
        except ValueError:
            raise ValueError('special mut be an int greater than or equal to 0')
        else:
            self._special = special

######### PROPERTIES ####################################################################

    @property
    def hp(self):
        '''Get the pokemon's hp'''
        return self._hp

    @property
    def spd(self):
        ''' Get the pokemon's spd'''
        return self._speed

######### METHODS #######################################################################

    def attack_force(self, level):
        '''TODO: description

        :param level: TODO
        :returns: TODO
        '''
        try:
            level = int(level)
            if level < 0:
                raise ValueError
        except ValueError:
            raise ValueError('level must be an int greater than or equal to 0')
        else:
            return (2 * level + 10) * self._attack

    def defense_force(self):
        '''TODO: description

        :returns: TODO
        '''
        return 250 * self._defense

    def critical(self):
        '''TODO: description

        :returns: TODO
        '''
        if random() <= self._speed / 512:
            return True 
        return False

    def decrease_life(self, amount):
        '''TODO: description

        :param amount: TODO
        :returns: TODO
        '''
        if amount < 0:
            raise ValueError("amount must be greater than or equal to 0")
        self._hp -= amount

