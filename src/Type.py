from enum import Enum


class Type(Enum):
    # list of types
    Normal = 0
    Fighting = 1
    Flying = 2
    Poison = 3
    Ground = 4
    Rock = 5
    Bird = 6
    Bug = 7
    Ghost = 8
    Fire = 9
    Water = 10
    Grass = 11
    Electric = 12
    Psychic = 13
    Ice = 14
    Dragon = 15
    Blank = 16

    compare_table = [
        [   1,   1,   1,   1,   1, 0.5,   1,   1,   0,   1,   1,   1,   1,   1,   1,   1,   1], # row 1
        [   2,   1, 0.5, 0.5,   1,   2,   1, 0.5,   0,   1,   1,   1,   1, 0.5,   2,   1,   1], # row 2
        [   1,   2,   1,   1,   1, 0.5,   1,   2,   1,   1,   1,   2, 0.5,   1,   1,   1,   1], # row 3
        [   1,   1,   1, 0.5, 0.5, 0.5,   1,   2, 0.5,   1,   1,   2,   1,   1,   1,   1,   1], # row 4
        [   1,   1,   0,   2,   1,   2,   1, 0.5,   1,   2,   1, 0.5,   2,   1,   1,   1,   1], # row 5
        [   1, 0.5,   2,   1, 0.5,   1,   1,   2,   1,   2,   1,   1,   1,   1,   2,   1,   1], # row 6
        [   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1], # row 7
        [   1, 0.5, 0.5,   2,   1,   1,   1,   1, 0.5, 0.5,   1,   2,   1,   2,   1,   1,   1], # row 8
        [   0,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1,   1,   0,   1,   1,   1], # row 9
        [   1,   1,   1,   1,   1, 0.5,   1,   2,   1, 0.5, 0.5,   2,   1,   1,   2, 0.5,   1], # row 10
        [   1,   1,   1,   1,   2,   2,   1,   1,   1,   2, 0.5, 0.5,   1,   1,   1, 0.5,   1], # row 11
        [   1,   1, 0.5, 0.5,   2,   2,   1, 0.5,   1, 0.5,   2, 0.5,   1,   1,   1, 0.5,   1], # row 12
        [   1,   1,   2,   1,   0,   1,   1,   1,   1,   1,   2, 0.5, 0.5,   1,   1, 0.5,   1], # row 13
        [   1,   2,   1,   2,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1], # row 14
        [   1,   1,   2,   1,   2,   1,   1,   1,   1,   1, 0.5,   2,   1,   1, 0.5,   2,   1], # row 15
        [   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1], # row 16
        [   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1]  # row 17
    ]

    def compare_to(poke_type):
        ''' Calculates the **Type Effectiveness** from a type to another

        :param poke_type: Is the type to be compared to. Often this is the defensive pokemon's type
        :returns: The **Type Effectiveness**
        '''
        return compare_table[self.value][poke_type.value]
