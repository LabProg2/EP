from random import random

class Stats:
    '''
    TODO: description
    '''
    def __init__(self, hp, attack_power, defense_power, speed, special): # Se houvessem valores padroes deveriamos por? ou definir setters para se um dia houvessem 10 stats fosse mais facil de inicializar? x_x
        '''TODO: description

        :param hp: TODO
        :param attack_power: TODO
        :param defense_power: TODO
        :param speed: TODO
        :param special: TODO
        :returns: TODO
        '''
        self._hp = hp
        self._attack_power = attack_power
        self._defense_power = defense_power
        self._speed = speed
        self._special = special

    def attack_force(self, level):
        '''TODO: description

        :param level: TODO
        :returns: TODO
        '''
        return (2 * level + 10) * self._attack_power

	@property
    def hp(self):
        '''Get the pokemon's hp'''
        return self._hp

    def attack_force(self, level):
        '''TODO: description

        :param level: TODO
        :returns: TODO
        '''
        return (2 * level + 10) * self._attack_power

    def defense_force():
        '''TODO: description

        :returns: TODO
        '''
        return 250 * self._defense_power

    def critical():
        '''TODO: description

        :returns: TODO
        '''
        if random() <= self._speed / 512:
            return True 
        return False
