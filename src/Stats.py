from random import random

class Stats:
    '''
    Pokemon's stats, including hp, attack, defense, etc.
    '''
    def __init__(self, hp, attack, defense, speed, special): # Se houvessem valores padroes deveriamos por? ou definir setters para se um dia houvessem 10 stats fosse mais facil de inicializar? x_x
        '''Stats constructor

        :param hp: Hp (health points) of the Pokemon
        :param attack: Attack of the Pokemon
        :param defense: Deffense of the Pokemon
        :param speed: Speed of the Pokemon
        :param special: Special points of the Pokemon
        :returns: A Stats instance with all attributes set
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
        '''Calculates the attack force of a Pokemon, based on it's stats. Used in Pokemon.perform_attack

        :param level: Level of the Pokemon (It's not a Stats attribute, It's a Pokemon attribute)
        :returns: returns the attack force = (2 * level + 10) * attack
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
        '''Calculates the defence force of a Pokemon, based on it's stats. Used in Pokemon.perform_attack

        :returns: returns the defence force = 250 * defense
        '''
        return 250 * self._defense

    def critical(self, level):
        '''Verifies if the attack is critical or not. Used in Pokemon.perform_attack

        :param level: The pokemon's level
        :returns: True or False, if is a critical attack or not.
        '''
        if random() <= self._speed / 512:
            print("It was a critical hit!")
            return (2 * level + 5) / (level + 5)
        return 1

    def decrease_life(self, amount):
        '''Decreases the hp (health points) of the Pokemon by the value of amount

        :param amount: Value that hp (health points) will be decreased
        '''
        if amount < 0:
            raise ValueError("amount must be greater than or equal to 0")
        self._hp -= amount

